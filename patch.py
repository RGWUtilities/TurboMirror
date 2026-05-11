import os
import glob
import shutil

for path in glob.glob('scratch-gui/build/*.html'):
  print(f'Patching HTML {path}')
  with open(path, 'r') as f:
    contents = f.read()
    contents = contents.replace('</head>', '<meta name="robots" content="noindex"></head>')
    contents = contents.replace('<link rel="manifest" href="manifest.webmanifest">', '')
  with open(path, 'w') as f:
    f.write(contents)

for path in glob.glob('scratch-gui/build/**/*.js', recursive=True):
  print(f'Patching JS {path}')
  with open(path, 'r') as f:
    contents = f.read()
    contents = contents.replace('https://trampoline.turbowarp.org', 'https://trampoline.turbowarp.xyz')
  with open(path, 'w') as f:
    f.write(contents)

# Open the main file
with open('scratch-gui/build/index.html', 'r') as f:
    content = f.read()

# 1. Change the Tab Title
content = content.replace('<title>TurboWarp</title>', '<title>OurCloud.buzz</title>')

# 2. Change the Meta Description (what shows in history/search)
content = content.replace('A high speed Scratch mod', 'A faster project version that makes learning for kids better')

# 3. Global replacement for any other mentions in the HTML
content = content.replace('TurboWarp', 'OurCloud.buzz')

# Save the changes back to the file
with open('scratch-gui/build/index.html', 'w') as f:
    f.write(content)


os.remove('scratch-gui/build/sw.js')
os.remove('scratch-gui/build/manifest.webmanifest')
os.remove('scratch-gui/build/fullscreen.html')
os.remove('scratch-gui/build/index.html')

shutil.copy('scratch-gui/build/editor.html', 'scratch-gui/build/index.html')
shutil.copy('robots.txt', 'scratch-gui/build/robots.txt')
