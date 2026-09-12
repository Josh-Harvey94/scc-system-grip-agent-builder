"""Check the reusable kit without dependencies. Does not test Copilot behaviour."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
HTML = ROOT / 'SCC_System_Grip_Agent_Build_Companion.html'


def read(path):
    return (ROOT / path).read_text(encoding='utf-8').rstrip('\n')


def main():
    source = HTML.read_text(encoding='utf-8')
    configuration = {
        'description': read('agent/description.txt'),
        'productionInstructions': read('agent/instructions.txt'),
        'starterPrompts': {p['title']: p['prompt'] for p in json.loads(read('agent/starter-prompts.json'))},
    }
    decoder = json.JSONDecoder()
    if '--sync' in sys.argv:
        for variable, value in configuration.items():
            start = source.index('const ' + variable + '=') + len('const ' + variable + '=')
            _, length = decoder.raw_decode(source[start:])
            source = source[:start] + json.dumps(value, ensure_ascii=False) + source[start + length:]
        HTML.write_text(source, encoding='utf-8', newline='\n')
    for variable, expected in configuration.items():
        start = source.index('const ' + variable + '=') + len('const ' + variable + '=')
        actual, _ = decoder.raw_decode(source[start:])
        assert actual == expected, 'HTML differs from canonical ' + variable
    for name, limit in [('name', 30), ('description', 1000), ('instructions', 8000)]:
        value = read('agent/' + name + '.txt')
        assert len(value) <= limit, name + ' exceeds documented field limit'
        print(f'{name}: {len(value)} / {limit} characters')
    assert read('agent/name.txt') == 'SCC System Grip Agent'
    for md in ROOT.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', md.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):
                continue
            path = (md.parent / target.split('#')[0]).resolve()
            assert path.exists(), f'Broken local link in {md.name}: {target}'
    sums = (ROOT / 'reference/SHA256SUMS.txt').read_text(encoding='utf-8')
    for line in sums.splitlines():
        digest, filename = line.split('  ', 1)
        actual = hashlib.sha256((ROOT / 'reference' / filename).read_bytes()).hexdigest()
        assert actual == digest, 'Historical source changed: ' + filename
    print('PASS: canonical copy kit, field limits, local document links and reference-file hashes')
    print('Microsoft 365 behavioural tests: NOT RUN by this script.')


if __name__ == '__main__':
    main()
