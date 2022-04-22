import glob
from tark.tark import process_file

files = glob.glob('./website' + '/**/*.md', recursive=True)
print(f"Processing {len(files)} files")

for file in files:
    output_location = file.replace('/website/', '/generated/').replace('.md', '.html')
    with open(output_location, 'w') as f:
        print("compiling: " + file)
        result = process_file(file)
        f.write(result)