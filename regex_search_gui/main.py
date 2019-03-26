from tkinter import filedialog
from tkinter import *
from utilities import regex_search


class RegexFileSearch:

    def __init__(self, main_window):
        self.file_content = ''
        self.search_result = ''
        self.create_widgets(main_window)

    def create_widgets(self, main_window):
        # create main frame window
        self.main_window = main_window
        self.main_window.title('Regex File Searcher')
        self.main_window.columnconfigure(0, weight=1)
        self.main_window.rowconfigure(0, weight=1)

        # create frame for a textbox and scrollbar
        self.txt_frame = Frame(self.main_window, width=800, height=600)
        self.txt_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.txt_frame.grid_rowconfigure(0, weight=100)
        self.txt_frame.grid_columnconfigure(0, weight=100)

        # create label for input screen
        self.input_screen_label = Label(self.txt_frame, text='Input file screen')
        self.input_screen_label.grid(row=0, column=0, sticky='w')

        # create textbox for printing file content
        self.input_screen = Text(self.txt_frame, state='disabled', width=80, height=30)
        self.input_screen.grid(row=1, column=0, sticky='nsew')
        self.input_screen.configure(state='normal')

        # create scrollbar for textbox
        self.scrollbar = Scrollbar(self.txt_frame, command=self.input_screen.yview)
        self.scrollbar.grid(row=1, column=1, sticky='nsew')
        self.input_screen['yscrollcommand'] = self.scrollbar.set

        # create label for result screen
        self.result_screen_label = Label(self.txt_frame, text='Search result screen')
        self.result_screen_label.grid(row=2, column=0, sticky='w')

        # create textbox for search result
        self.result_screen = Text(self.txt_frame, state='disabled', width=80, height=20)
        self.result_screen.grid(row=3, column=0, sticky='nsew')
        self.result_screen.configure(state='normal')
        self.result_scrollbar = Scrollbar(self.txt_frame, command=self.result_screen.yview)
        self.result_scrollbar.grid(row=3, column=1, sticky='nsew')
        self.result_screen['yscrollcommand'] = self.result_scrollbar.set

        # create load file button
        self.load_file_button = Button(self.main_window, text='Wczytaj plik', command=lambda: self.load_file(),
                                       width=10, height=1)
        self.load_file_button.grid(row=1, column=0, sticky='w')

        # create frame for a regex
        self.regex_frame = Frame(self.main_window, width=800, height=600)
        self.regex_frame.grid(row=0, column=1, padx=5, pady=5, sticky='n')
        self.regex_frame.grid_rowconfigure(0, weight=100)
        self.regex_frame.grid_columnconfigure(0, weight=100)

        # create label for result screen
        self.regex_screen_label = Label(self.regex_frame, text='Regex')
        self.regex_screen_label.grid(row=0, column=0, sticky='w')

        # create regex textbox
        self.regex_screen = Text(self.regex_frame, state='disabled', width=20, height=1)
        self.regex_screen.grid(row=1, column=0, sticky='w')
        self.regex_screen.configure(state='normal')

        # create regex button
        self.execute_search_buton = Button(self.regex_frame, text='Szukaj', command=lambda: self.search())
        self.execute_search_buton.grid(padx=5, pady=5, sticky='e')

    def load_file(self):
        self.main_window.filename = filedialog.askopenfilename(
            title='Select file', filetypes=(('all files', '*.*'), ('log files','*.log'), ('txt files', '*.txt')))
        with open(self.main_window.filename, 'r') as f:
            self.file_content = f.read()
            self.input_screen.delete('1.0', END)
            self.input_screen.insert(INSERT, self.file_content)
            self.result_screen.delete('1.0',END)

    def search(self):
        result = regex_search(self.file_content, self.regex_screen.get('1.0', END))
        self.result_screen.delete('1.0', END)
        self.result_screen.insert('1.0', result)


root_window = Tk()
RegexFileSearch(root_window)
root_window.mainloop()
