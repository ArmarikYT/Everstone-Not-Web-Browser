import os
import tkinter as tk
from tkinter import scrolledtext, messagebox

class FileBrowserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Everstone Not Web Browser")
        
        # Welcome message
        self.welcome_label = tk.Label(self.root, text="Welcome to Everstone Not Web Borwser by Armarik", font=("Arial", 14))
        self.welcome_label.pack(pady=10)

        # File name entry
        self.filename_label = tk.Label(self.root, text="Enter page name:", font=("Arial", 12))
        self.filename_label.pack(pady=5)
        
        self.filename_entry = tk.Entry(self.root, width=50)
        self.filename_entry.pack(pady=5)
        
        # Search button
        self.search_button = tk.Button(self.root, text="Search", command=self.search_file)
        self.search_button.pack(pady=10)
        
        # Text area to display file content
        self.file_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=20)
        self.file_text.pack(pady=10)
        
    def search_file(self):
        filename = self.filename_entry.get()
        directory = "C:/EverstoneNWB/Pages"
        file_path = os.path.join(directory, filename)
        
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    self.file_text.delete('1.0', tk.END)  # Clear previous content
                    self.file_text.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Error", f"Error reading file: {str(e)}")
        else:
            messagebox.showerror("File Not Found", f"File '{filename}' not found in {directory}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileBrowserApp(root)
    root.mainloop()
