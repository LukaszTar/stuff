from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from utilities import regex_search


class RegexFileSearch:

    def __init__(self, main_window):
        self.file_content = ''
        self.search_result = ''
        self.num_of_result_screens = 0
        self.create_widgets(main_window)

    def create_widgets(self, main_window):
        # create main frame window
        self.main_window = main_window
        self.main_window.title('Regex File Searcher')
        self.main_window.columnconfigure(0, weight=1)
        self.main_window.rowconfigure(0, weight=1)

        # create frame for a textbox and scrollbar
        self.input_screen_frame = Frame(self.main_window, width=800, height=600)
        self.input_screen_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.input_screen_frame.grid_rowconfigure(0, weight=100)
        self.input_screen_frame.grid_columnconfigure(0, weight=100)

        # create label for input screen
        self.input_screen_label = Label(self.input_screen_frame, text='Input file screen')
        self.input_screen_label.grid(row=0, column=0, sticky='w')

        # create textbox for printing file content
        self.input_screen = Text(self.input_screen_frame, state='disabled', width=80, height=30)
        self.input_screen.grid(row=1, column=0, sticky='nsew')
        self.input_screen.configure(state='normal')

        # create scrollbar for textbox
        self.scrollbar = Scrollbar(self.input_screen_frame, command=self.input_screen.yview)
        self.scrollbar.grid(row=1, column=1, sticky='nsew')
        self.input_screen['yscrollcommand'] = self.scrollbar.set

        self.nb = ttk.Notebook(self.main_window)

        # create label for result screen
#        self.result_screen_frame = Frame(self.main_window, width=800, height=600)
        self.nb.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        self.nb.grid_rowconfigure(0, weight=100)
        self.nb.grid_columnconfigure(0, weight=100)

        self.create_result_screen()

        # create load file button
        self.load_file_button = Button(self.main_window, text='Wczytaj plik', command=lambda: self.load_file(),
                                       width=10, height=1)
        self.load_file_button.grid(row=2, column=0, sticky='w')

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
            #getattr(self, 'result_screen'+str(self.num_of_result_screens)).delete('1.0',END)

    def search(self):
        result = regex_search(self.file_content, self.regex_screen.get('1.0', END))
        self.create_result_screen()
        getattr(self, 'result_screen'+str(self.num_of_result_screens)).delete('1.0', END)
        getattr(self, 'result_screen'+str(self.num_of_result_screens)).insert('1.0', result)


    def create_result_screen(self):
        self.num_of_result_screens += 1
        setattr(self, 'result_screen_frame'+str(self.num_of_result_screens), Frame(self.nb))
        self.nb.add(getattr(self, 'result_screen_frame'+str(self.num_of_result_screens)), text='Search result')
        setattr(self, 'result_screen'+str(self.num_of_result_screens), Text(getattr(self, 'result_screen_frame'+str(self.num_of_result_screens)), state='disabled', width=80, height=20))
        getattr(self, 'result_screen'+str(self.num_of_result_screens)).grid(row=3, column=0, sticky='nsew')
        getattr(self, 'result_screen'+str(self.num_of_result_screens)).configure(state='normal')

        setattr(self, 'result_scrollbar'+str(self.num_of_result_screens), Scrollbar(getattr(self, 'result_screen_frame'+str(self.num_of_result_screens)), command=getattr(self, 'result_screen'+str(self.num_of_result_screens)).yview))

        getattr(self, 'result_scrollbar'+str(self.num_of_result_screens)).grid(row=3, column=1, sticky='nsew')
        getattr(self, 'result_screen' + str(self.num_of_result_screens))['yscrollcommand'] = getattr(self, 'result_scrollbar'+str(self.num_of_result_screens)).set
        self.nb.select(getattr(self, 'result_screen_frame' + str(self.num_of_result_screens)))
        #getattr(self, 'result_screen_frame' + str(self.num_of_result_screens)).select()
        # self.result_screen.grid(row=3, column=0, sticky='nsew')
        # self.result_screen.configure(state='normal')
        # self.result_scrollbar = Scrollbar(getattr(self, 'result_screen_frame'+str(self.num_of_result_screens)), command=self.result_screen.yview)
        # self.result_scrollbar.grid(row=3, column=1, sticky='nsew')
        # self.result_screen['yscrollcommand'] = self.result_scrollbar.set

root_window = Tk()
RegexFileSearch(root_window)
root_window.mainloop()
