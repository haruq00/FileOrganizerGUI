import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text=folder_path)
        global target_folder
        target_folder = folder_path

def organize_files():
    if not target_folder:
        messagebox.showwarning("Warning", "Please select a folder first.")
        return

    status_text.delete('1.0', tk.END)  

    
    extension_folders = {
        '.jpeg': 'Images',
        '.jpg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.mp3': 'Music',
        '.wav': 'Music',
        '.pdf': 'Documents',
        '.docx': 'Documents',
        '.txt': 'TextFiles',
    }

    
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(filename)
            extension = extension.lower()  

            if not extension or extension not in extension_folders:
                continue
            elif extension in extension_folders:
                folder_name = extension_folders[extension]

            destination_folder = os.path.join(target_folder, folder_name)

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            shutil.move(file_path, os.path.join(destination_folder, filename))
            status_text.insert(tk.END, f'Moved {filename} to {folder_name}\n')

    status_text.insert(tk.END, '======================\n')
    status_text.insert(tk.END, '整理完了！\n')
    status_text.insert(tk.END, '======================\n')

# GUI設定
root = tk.Tk()
root.title("ファイル自動整理ツール")

target_folder = ''

select_button = tk.Button(root, text="整理したいフォルダを選択", command=select_folder)
select_button.pack(pady=10)

folder_label = tk.Label(root, text="フォルダが選択されていません")
folder_label.pack()

start_button = tk.Button(root, text="整理開始", command=organize_files)
start_button.pack(pady=10)

status_text = tk.Text(root, height=15, width=60)
status_text.pack()

root.mainloop()