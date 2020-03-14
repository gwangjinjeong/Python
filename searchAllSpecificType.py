import os
from tkinter import filedialog

def search(dirname,extension):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == extension:
                    print(full_filename)
    except PermissionError:
        pass
imageDir = filedialog.askdirectory(title="Select a Directory")

# ex) type of .JPG file
search(imageDir,'.JPG')
  
