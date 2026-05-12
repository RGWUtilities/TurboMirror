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


os.remove('scratch-gui/build/sw.js')
os.remove('scratch-gui/build/manifest.webmanifest')
os.remove('scratch-gui/build/fullscreen.html')
os.remove('scratch-gui/build/index.html')

shutil.copy('scratch-gui/build/editor.html', 'scratch-gui/build/index.html')
shutil.copy('robots.txt', 'scratch-gui/build/robots.txt')

import os
import re

# New Branding
NEW_NAME = "RGWarp"
FULL_TITLE = "RGWarp - Run projects with power" 

for root, dirs, files in os.walk('scratch-gui/build'):
    for file in files:
        if file.endswith(('.html', '.js', '.json')):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 1. Swap every mention of TurboWarp to RGWarp
            if 'TurboWarp' in content:
                content = content.replace('TurboWarp', NEW_NAME)
                
                # 2. Specifically force the browser tab title
                if '<title>' in content:
                    content = re.sub(r'<title>.*?</title>', f'<title>{FULL_TITLE}</title>', content)
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)


