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



# Define the path to the main index file
index_path = 'scratch-gui/build/index.html'

if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the EXACT title tag you found
    content = content.replace(
        '<title>TurboWarp - Run Scratch projects faster</title>', 
        '<title>OurCloud.buzz - Educational Learning Platform</title>'
    )

    # 2. Update the meta description to your custom version
    content = content.replace(
        'A high speed Scratch mod', 
        'A faster project version that makes learning for kids better'
    )

    # 3. Global Replacement: Catch every other mention of TurboWarp
    # This cleans up the loading screen, footer, and help menus
    content = content.replace('TurboWarp', 'OurCloud.buzz')

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
else:
    print(f"Warning: {index_path} not found. Skipping stealth patch.")


os.remove('scratch-gui/build/sw.js')
os.remove('scratch-gui/build/manifest.webmanifest')
os.remove('scratch-gui/build/fullscreen.html')
os.remove('scratch-gui/build/index.html')

shutil.copy('scratch-gui/build/editor.html', 'scratch-gui/build/index.html')
shutil.copy('robots.txt', 'scratch-gui/build/robots.txt')
