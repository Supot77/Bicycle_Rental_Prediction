"""Refresh the web hub's planned tasks from CSV; never exports team progress."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    metadata = json.loads((ROOT / 'apps-script/project-data.json').read_text(encoding='utf-8'))
    with (ROOT / 'evidence/task_board.csv').open(encoding='utf-8', newline='') as handle:
        rows = list(csv.DictReader(handle))
    tasks = []
    for row in rows:
        extra = metadata['taskDetails'][row['task_id']]
        tasks.append({
            'id': row['task_id'], 'title': extra['title'], 'description': row['task'],
            'owners': re.findall(r'M[1-5]', row['owner']) or ['M1', 'M2', 'M3', 'M4', 'M5'],
            'reviewer': row['reviewer'], 'deliverable': row['deliverable'],
            'dependencies': list(filter(None, row['dependency'].split('|'))),
            'phase': extra['phase'], 'notebook': extra['notebook'],
            'steps': extra['steps'], 'check': extra['check'],
        })
    data = {key: metadata[key] for key in ('roles', 'phases', 'resources', 'gates')}
    data['tasks'] = tasks
    code_path = ROOT / 'apps-script/Code.gs'
    code = code_path.read_text(encoding='utf-8')
    line = 'const PROJECT_ = /* PROJECT_DATA */ ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';'
    code, count = re.subn(r'^const PROJECT_ = /\* PROJECT_DATA \*/ .*?;$', lambda _: line, code, count=1, flags=re.M)
    if count != 1:
        raise ValueError('The PROJECT_DATA marker is missing or ambiguous')
    code_path.write_text(code, encoding='utf-8', newline='\n')
    print(f'Updated web hub definitions: {len(tasks)} tasks; no real progress exported.')


if __name__ == '__main__':
    main()
