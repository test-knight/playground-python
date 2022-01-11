from pathlib import Path

path = Path()
files = []
for file in path.rglob('*.xlsx'):
    files.append(file)

for name in files:
    print(name.name)