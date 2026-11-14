"""Check that skills, plugin manifests and the README agree.

Run from anywhere: `python3 tools/check_skills.py`. Exits 1 and lists every problem found.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
SEMVER = re.compile(r'^\d+\.\d+\.\d+$')
ABSOLUTE = re.compile(r'(?<![\w.~])(?:/Users/|/home/)\w')
README_ROW = re.compile(r'^\| `([^`]+)` \|', re.M)


def frontmatter(text):
    lines = text.split('\n')
    if not lines or lines[0].strip() != '---':
        return None
    fields = {}
    for line in lines[1:]:
        if line.strip() == '---':
            return fields
        match = re.match(r'^([A-Za-z_-]+):\s*(.*)$', line)
        if match:
            value = match.group(2).strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in '"\'':
                value = value[1:-1]
            fields[match.group(1)] = value
    return None


def load_json(root, path, problems):
    try:
        return json.loads((root/path).read_text())
    except FileNotFoundError:
        problems.append(f'{path}: missing')
    except json.JSONDecodeError as error:
        problems.append(f'{path}: invalid JSON: {error}')
    return None


def parse(version):
    return tuple(int(part) for part in version.split('.'))


def latest_tag(root):
    result = subprocess.run(['git', 'tag', '--list', 'v*', '--sort=-v:refname'],
                            cwd=root, capture_output=True, text=True)
    tags = result.stdout.split()
    return tags[0] if tags else None


def check(root=ROOT, tag=latest_tag):
    problems = []
    skills = sorted(p.name for p in (root/'skills').iterdir() if p.is_dir())

    for name in skills:
        skill = root/'skills'/name/'SKILL.md'
        if not skill.is_file():
            problems.append(f'skills/{name}: no SKILL.md')
            continue
        fields = frontmatter(skill.read_text())
        if fields is None:
            problems.append(f'skills/{name}/SKILL.md: no frontmatter')
            continue
        if fields.get('name') != name:
            problems.append(f'skills/{name}/SKILL.md: name {fields.get("name")!r} does not match the folder')
        if not NAME.match(name) or len(name) > 64:
            problems.append(f'skills/{name}: name must be lowercase words joined by hyphens, at most 64 characters')
        description = fields.get('description', '')
        if not description:
            problems.append(f'skills/{name}/SKILL.md: no description')
        elif len(description) > 1024:
            problems.append(f'skills/{name}/SKILL.md: description is {len(description)} characters, over 1024')
        for path in sorted((root/'skills'/name).rglob('*')):
            if path.is_file() and path.suffix in ('.md', '.sh', '.py', '.json', '.yml', '.yaml'):
                for number, line in enumerate(path.read_text(errors='replace').split('\n'), 1):
                    if ABSOLUTE.search(line):
                        problems.append(f'{path.relative_to(root)}:{number}: absolute home path')

    claude = load_json(root, '.claude-plugin/marketplace.json', problems)
    codex = load_json(root, '.codex-plugin/plugin.json', problems)
    codex_market = load_json(root, '.agents/plugins/marketplace.json', problems)

    if claude:
        plugins = claude.get('plugins', [])
        if len(plugins) != 1:
            problems.append('.claude-plugin/marketplace.json: expected exactly one plugin')
        else:
            plugin = plugins[0]
            listed = sorted(p.removeprefix('./skills/') for p in plugin.get('skills', []))
            for name in sorted(set(skills) - set(listed)):
                problems.append(f'.claude-plugin/marketplace.json: skills/{name} is not listed')
            for name in sorted(set(listed) - set(skills)):
                problems.append(f'.claude-plugin/marketplace.json: lists missing skill {name}')
            if 'version' in plugin:
                problems.append('.claude-plugin/marketplace.json: leave version out so Claude Code tracks the commit')
            if codex and codex.get('name') != plugin.get('name'):
                problems.append('.codex-plugin/plugin.json: name differs from the Claude plugin name')
        if codex_market and codex_market.get('name') != claude.get('name'):
            problems.append('.agents/plugins/marketplace.json: name differs from the Claude marketplace name')

    if codex:
        version = codex.get('version', '')
        if not SEMVER.match(version):
            problems.append(f'.codex-plugin/plugin.json: version {version!r} is not MAJOR.MINOR.PATCH')
        released = tag(root)
        # Not older than the latest tag: a release bumps it before tagging.
        if released and SEMVER.match(version) and parse(version) < parse(released[1:]):
            problems.append(f'.codex-plugin/plugin.json: version {version} is older than the latest tag {released}')

    if codex_market:
        names = [p.get('name') for p in codex_market.get('plugins', [])]
        if codex and names != [codex.get('name')]:
            problems.append('.agents/plugins/marketplace.json: expected one plugin named like .codex-plugin/plugin.json')

    readme = (root/'README.md').read_text() if (root/'README.md').is_file() else ''
    rows = README_ROW.findall(readme)
    for name in sorted(set(skills) - set(rows)):
        problems.append(f'README.md: skill table is missing {name}')
    for name in sorted(set(rows) - set(skills)):
        problems.append(f'README.md: skill table lists missing skill {name}')

    return problems


def main():
    problems = check()
    for problem in problems:
        print(problem)
    print(f'{len(problems)} problem(s)' if problems else 'skills OK')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
