import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_skills import check


def no_tag(root):
    return None


class CheckSkills(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.write_skill('tiny-slice', 'Focused pairing.')
        self.claude = {'name': 'm', 'plugins': [{'name': 'p', 'source': './', 'skills': ['./skills/tiny-slice']}]}
        self.codex = {'name': 'p', 'version': '1.0.0', 'skills': './skills/'}
        self.codex_market = {'name': 'm', 'plugins': [{'name': 'p', 'source': {'source': 'local', 'path': './'}}]}
        self.readme = '| Skill | What |\n| --- | --- |\n| `tiny-slice` | Focused pairing. |\n'
        self.save()

    def tearDown(self):
        self.tmp.cleanup()

    def write_skill(self, name, description, folder=None):
        path = self.root/'skills'/(folder or name)
        path.mkdir(parents=True, exist_ok=True)
        (path/'SKILL.md').write_text(f'---\nname: {name}\ndescription: {description}\n---\n\nBody.\n')
        (path/'README.md').write_text(f'# {name}\n')

    def save(self):
        for path, data in (('.claude-plugin/marketplace.json', self.claude), ('.codex-plugin/plugin.json', self.codex),
                           ('.agents/plugins/marketplace.json', self.codex_market)):
            (self.root/path).parent.mkdir(parents=True, exist_ok=True)
            (self.root/path).write_text(json.dumps(data))
        (self.root/'README.md').write_text(self.readme)

    def problems(self, tag=no_tag):
        return check(self.root, tag)

    def test_consistent_repo_passes(self):
        self.assertEqual(self.problems(), [])

    def test_new_skill_must_be_listed_everywhere(self):
        self.write_skill('afk', 'Away mode.')
        self.assertEqual(self.problems(), [
            '.claude-plugin/marketplace.json: skills/afk is not listed',
            'README.md: skill table is missing afk',
        ])

    def test_removed_skill_must_be_unlisted(self):
        self.claude['plugins'][0]['skills'].append('./skills/gone')
        self.readme += '| `gone` | Gone. |\n'
        self.save()
        self.assertEqual(self.problems(), [
            '.claude-plugin/marketplace.json: lists missing skill gone',
            'README.md: skill table lists missing skill gone',
        ])

    def test_frontmatter_name_matches_folder(self):
        self.write_skill('tiny', 'Focused pairing.', folder='tiny-slice')
        self.assertEqual(self.problems(), ["skills/tiny-slice/SKILL.md: name 'tiny' does not match the folder"])

    def test_description_required_and_bounded(self):
        self.write_skill('tiny-slice', '')
        self.assertEqual(self.problems(), ['skills/tiny-slice/SKILL.md: no description'])
        self.write_skill('tiny-slice', 'x' * 1025)
        self.assertEqual(self.problems(), ['skills/tiny-slice/SKILL.md: description is 1025 characters, over 1024'])

    def test_readme_required(self):
        (self.root/'skills/tiny-slice/README.md').unlink()
        self.assertEqual(self.problems(), ['skills/tiny-slice: no README.md'])

    def test_absolute_home_paths_rejected(self):
        (self.root/'skills/tiny-slice/notes.md').write_text('See ~/notes and\nopen /Users/someone/file\n')
        self.assertEqual(self.problems(), ['skills/tiny-slice/notes.md:2: absolute home path'])

    def test_claude_manifest_has_no_version(self):
        self.claude['plugins'][0]['version'] = '1.0.0'
        self.save()
        self.assertEqual(self.problems(), [
            '.claude-plugin/marketplace.json: leave version out so Claude Code tracks the commit'])

    def test_codex_version_not_older_than_latest_tag(self):
        self.assertEqual(self.problems(tag=lambda root: 'v1.0.0'), [])
        self.assertEqual(self.problems(tag=lambda root: 'v0.9.0'), [])
        self.assertEqual(self.problems(tag=lambda root: 'v1.0.10'), [
            '.codex-plugin/plugin.json: version 1.0.0 is older than the latest tag v1.0.10'])

    def test_codex_version_is_semver(self):
        self.codex['version'] = 'local'
        self.save()
        self.assertEqual(self.problems(), [".codex-plugin/plugin.json: version 'local' is not MAJOR.MINOR.PATCH"])

    def test_plugin_and_marketplace_names_agree(self):
        self.codex['name'] = 'other'
        self.codex_market['name'] = 'other-market'
        self.save()
        self.assertEqual(self.problems(), [
            '.codex-plugin/plugin.json: name differs from the Claude plugin name',
            '.agents/plugins/marketplace.json: name differs from the Claude marketplace name',
            '.agents/plugins/marketplace.json: expected one plugin named like .codex-plugin/plugin.json',
        ])

    def test_broken_json_reported(self):
        (self.root/'.codex-plugin/plugin.json').write_text('{')
        problems = self.problems()
        self.assertEqual(len(problems), 1)
        self.assertTrue(problems[0].startswith('.codex-plugin/plugin.json: invalid JSON'))


if __name__ == '__main__':
    unittest.main()
