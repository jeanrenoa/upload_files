import fnmatch
import os
  
rootPath = '//panda.autodesk.com/BRE_MASTERS_PSEB/ADSK_Materials/Longbow/px86x64'
pattern = '*.zip'
  
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(root, filename))
