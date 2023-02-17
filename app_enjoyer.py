from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

from randomize_app import RandomizeForColleage


class GUI_interface:
    #variables
    root = ''
    entry_est = ''
    entry_avg = ''
    isBool = False

    values = []

    def __init__(self, title = 'Рандомайзер', win_geometry= '300x300'):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(win_geometry)
        self.root.resizable(False, False)
        self.root.iconbitmap(default="./images/zxc.ico")
        #self.root.iconbitmap('/test/zxc.ico')

        self.entry_est = ttk.Entry(width=10)
        self.entry_avg = ttk.Entry(width=10)

    
    def run(self):
        self.__draw_widgets()
        self.root.mainloop()
    
    def __draw_widgets(self):
        ttk.Label(self.root, text="Количество оценок: ", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=15)
        #self.entry_est = ttk.Entry(self.root, width=10).grid(row=0, column=1)
        self.entry_est.grid(row=0, column=1)

        ttk.Label(self.root, text="Среднее арифметическое: ", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=15)
        #entry = ttk.Entry(self.root, width=10).grid(row=1, column=1)
        self.entry_avg.grid(row=1, column=1)

        btn = ttk.Button(text="Начать генерировать", command=self.check_entry_fields, width=20).grid(row=3, column=0, columnspan=2, pady=25)

    def check_entry_fields(self):
        global values

        if self.entry_est.get().isdigit() and self.entry_avg.get().isdigit():
            values = [int(self.entry_est.get()), int(self.entry_avg.get())]

            if values[0] > 0:
                if values[1] >= 50 and values[1] <= 100:
                    self.__randomize_object(values)
                    values = []
        else:
            self.__clear_entry_fields()

    def __clear_entry_fields(self):
        self.entry_est.delete(0, END)
        self.entry_avg.delete(0, END)

    def __draw_download_widgets(self):
        image = PhotoImage(file="./images/excel.ico")
        Button(self.root, image=image, command=lambda: print('click'), relief = 'flat').grid(row=4, column=1)


    def __write_numbers(self, writing_array, number):
        reading_info = ''

        with open('C:\\Users\\kv\Desktop\\right_combos.txt', 'r') as file:
            reading_info = file.read()
            if reading_info:
                number = int(reading_info.split('\n')[-1][1]) + 1

        with open('C:\\Users\\kv\Desktop\\right_combos.txt', 'w') as file:
            if not reading_info:
                file.write(f'#{str(number)} | ')
            else:
                file.write(f'{reading_info} \n#{str(number)} | ')
            for i in writing_array:
                file.write(f'{str(i)} ')


    def __randomize_object(self, values):
        tk = RandomizeForColleage(values)
        result = tk.run()
        line = ''

        for i in result:
            line = line + str(i) + ' '


        del tk
        ttk.Label(self.root, text="["+line+"]").grid(row=4, column=0,columnspan=2)
        self.__draw_download_widgets()