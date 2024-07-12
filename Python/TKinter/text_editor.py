import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename

class Editor(tk.Tk):
    """A simple text editor application using Tkinter."""

    def __init__(self):
        """Initialize the Editor."""
        super().__init__()
        self.title('GlobalMentoring.com.mx - Text Editor')
        # Configure minimum window size
        self.rowconfigure(0, minsize=600, weight=1)
        # Configure minimum size for the second column
        self.columnconfigure(1, minsize=600, weight=1)
        # Text field attribute
        self.text_field = tk.Text(self, wrap=tk.WORD)
        # File attribute
        self.file = None
        # Attribute to check if a file has been previously opened
        self.file_opened = False
        # Create components
        self._create_components()
        # Create menu
        self._create_menu()

    def _create_components(self):
        """Create the components of the editor."""
        button_frame = tk.Frame(self, relief=tk.RAISED, bd=2)
        open_button = tk.Button(button_frame, text='Open', command=self._open_file)
        save_button = tk.Button(button_frame, text='Save', command=self._save)
        save_as_button = tk.Button(button_frame, text='Save As...', command=self._save_as)
        # Expand buttons horizontally (sticky='we')
        open_button.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        save_button.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        save_as_button.grid(row=2, column=0, sticky='we', padx=5, pady=5)
        # Place the frame vertically
        button_frame.grid(row=0, column=0, sticky='ns')
        # Add the text field, expand it to fill the available space
        self.text_field.grid(row=0, column=1, sticky='nswe')

    def _create_menu(self):
        """Create the menu for the editor."""
        # Create the app menu
        app_menu = tk.Menu(self)
        self.config(menu=app_menu)
        # Add options to our menu
        # Add file menu
        file_menu = tk.Menu(app_menu, tearoff=False)
        app_menu.add_cascade(label='File', menu=file_menu)
        # Add options to the file menu
        file_menu.add_command(label='Open', command=self._open_file)
        file_menu.add_command(label='Save', command=self._save)
        file_menu.add_command(label='Save As...', command=self._save_as)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.quit)

    def _open_file(self):
        """Open a file for editing (read-write)."""
        self.file_opened = askopenfile(mode='r+')
        # Clear previous text
        self.text_field.delete(1.0, tk.END)
        # Check if there is a file
        if not self.file_opened:
            return
        # Open the file in read-write mode as a resource
        with open(self.file_opened.name, 'r+') as self.file:
            # Read the file content
            text = self.file.read()
            # Insert the file content
            self.text_field.insert(1.0, text)
            # Modify the application title
            self.title(f'*Text Editor - {self.file.name}')

    def _save(self):
        """Save the currently opened file."""
        # If a file has been previously opened, overwrite it
        if self.file_opened:
            # Save the file (open it in write mode)
            with open(self.file_opened.name, 'w') as self.file:
                # Read the content of the text box
                text = self.text_field.get(1.0, tk.END)
                # Write the content to the same file
                self.file.write(text)
                # Change the app title
                self.title(f'Text Editor - {self.file.name}')
        else:
            self._save_as()

    def _save_as(self):
        """Save the current file as a new file."""
        self.file = asksaveasfilename(
            defaultextension='.txt',
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
        )
        if not self.file:
            return
        # Ensure the file has the .txt extension
        if not self.file.endswith('.txt'):
            self.file += '.txt'
        # Open the file in write mode
        with open(self.file, 'w') as file:
            # Read the content of the text box
            text = self.text_field.get(1.0, tk.END)
            # Write the content to the new file
            file.write(text)
            # Change the file name
            self.title(f'Text Editor - {file.name}')
            # Indicate that a file has been opened
            self.file_opened = file

if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()
