import hashlib
import os
from tkinter import filedialog
from tkinter import Tk
from tkinter import messagebox
from tkinter import Text

def calculate_hash(directory):
    sha256_hash = hashlib.sha256()
    for root, dirs, files in os.walk(directory):
        for file in files:
            with open(os.path.join(root, file),"rb") as f:
                for byte_block in iter(lambda: f.read(4096),b""):
                    sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def browse_directory():
    directory = filedialog.askdirectory()
    hash_result = calculate_hash(directory)
    root = Tk()
    text = Text(root)
    text.insert('1.0', hash_result)
    text.pack()
    root.mainloop()

root = Tk()
root.withdraw()
browse_directory()