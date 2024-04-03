import tkinter
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        self.num_fib = 0
        self.num_fib0 = 1
        self.счётчик = 0
        self.string_ch = ""

        super().__init__()
        self.iconbitmap("./icon/icon.ico")
        self.title("Pr 3")
        self.geometry("300x300")
        self.grid_columnconfigure((0, 1), weight=1)

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Tab 1")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.add("Tab 4")
        self.tabview.tab("Tab 1").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Tab 3").grid_columnconfigure((0, 1, 2), weight=1)
        self.tabview.tab("Tab 4").grid_columnconfigure(0, weight=1)

        # create "Tab 1"
        self.lable_fib = customtkinter.CTkLabel(self.tabview.tab("Tab 1"),
                                                text="Число фибоначи: {}".format(self.num_fib))
        self.lable_fib.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Tab 1"),
                                                           text="Нажатий: {}".format(self.счётчик),
                                                           command=self.on_button_fib)
        self.string_input_button.grid(row=1, column=0, padx=20, pady=(10, 10))

        # create tab 2
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="Утка")
        self.label_tab_2.grid(row=0, column=0, padx=3, pady=3)

        self.Enter = customtkinter.CTkEntry(self.tabview.tab("Tab 2"), placeholder_text="Пароль")
        self.Enter.grid(row=1, column=0, padx=3, pady=3)

        self.button_tab_2 = customtkinter.CTkButton(self.tabview.tab("Tab 2"), text="проверка",
                                                    command=self.on_checbox)
        self.button_tab_2.grid(row=2, column=0, padx=3, pady=3)

        self.label_tab_20 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="")
        self.label_tab_20.grid(row=3, column=0, padx=3, pady=3)

        # create tab 3
        self.label_tab_3 = customtkinter.CTkLabel(self.tabview.tab("Tab 3"), text="нажато: ")
        self.label_tab_3.grid(row=0, column=0, padx=3, pady=3, sticky="ew", columnspan=3)

        self.checbox_3_1 = customtkinter.CTkCheckBox(self.tabview.tab("Tab 3"), text="Й",
                                                     command=self.on_checbox)
        self.checbox_3_1.grid(row=1, column=0, padx=3, pady=3, sticky="w")

        self.checbox_3_2 = customtkinter.CTkCheckBox(self.tabview.tab("Tab 3"), text="Н",
                                                     command=self.on_checbox)
        self.checbox_3_2.grid(row=1, column=1, padx=3, pady=3, sticky="w")

        self.checbox_3_3 = customtkinter.CTkCheckBox(self.tabview.tab("Tab 3"), text="Х",
                                                     command=self.on_checbox)
        self.checbox_3_3.grid(row=1, column=2, padx=3, pady=3, sticky="w")

        self.checbox_3_4 = customtkinter.CTkCheckBox(self.tabview.tab("Tab 3"), text="Ч",
                                                     command=self.on_checbox)
        self.checbox_3_4.grid(row=2, column=0, padx=3, pady=3, sticky="w")

        self.checbox_3_5 = customtkinter.CTkCheckBox(self.tabview.tab("Tab 3"), text="у",
                                                     command=self.on_checbox)
        self.checbox_3_5.grid(row=2, column=1, padx=3, pady=3, sticky="w")

        # create tab 4
        self.radio_var = tkinter.IntVar(value=0)
        self.radiobutton_1 = customtkinter.CTkRadioButton(self.tabview.tab("Tab 4"), text="1",
                                                          command=self.radiobutton_event, variable=self.radio_var,
                                                          value=1)
        self.radiobutton_1.grid(row=0, column=0, padx=3, pady=3, sticky="w")

        self.radiobutton_2 = customtkinter.CTkRadioButton(self.tabview.tab("Tab 4"), text="2",
                                                          command=self.radiobutton_event, variable=self.radio_var,
                                                          value=2)
        self.radiobutton_2.grid(row=1, column=0, padx=3, pady=3, sticky="w")

        self.radiobutton_3 = customtkinter.CTkRadioButton(self.tabview.tab("Tab 4"), text="3",
                                                          command=self.radiobutton_event, variable=self.radio_var,
                                                          value=3)
        self.radiobutton_3.grid(row=2, column=0, padx=3, pady=3, sticky="w")

        self.label_tab_4 = customtkinter.CTkLabel(self.tabview.tab("Tab 4"),
                                                  text="Радиобатон нажата: {}".format(self.radio_var.get()))
        self.label_tab_4.grid(row=3, column=0, padx=3, pady=3, sticky="w")

    def on_button_fib(self):
        self.num_fib, self.num_fib0 = self.num_fib0, self.num_fib + self.num_fib0
        self.счётчик += 1
        self.lable_fib.configure(self, text="Число фибоначи: {}".format(self.num_fib))
        self.string_input_button.configure(self, text="Нажатий: {}".format(self.счётчик))

    def on_button_pass(self):
        passw = "123"
        check = self.Enter.get()

        if passw == check:
            self.label_tab_20.configure(text="выжила")
        else:
            self.label_tab_20.configure(text="сдохла")

    def on_checbox(self):
        self.string_ch = ""

        if self.checbox_3_1.get() == 1:
            self.string_ch = self.string_ch + "Й"

        if self.checbox_3_2.get() == 1:
            self.string_ch = self.string_ch + "Н"

        if self.checbox_3_3.get() == 1:
            self.string_ch = self.string_ch + "Х"

        if self.checbox_3_4.get() == 1:
            self.string_ch = self.string_ch + "Ч"

        if self.checbox_3_5.get() == 1:
            self.string_ch = self.string_ch + "У"

        self.label_tab_3.configure(text="нажато: {}".format(self.string_ch))

    def radiobutton_event(self):
        self.label_tab_4.configure(text="Радиобатон нажата: {}".format(self.radio_var.get()))


app = App()
app.mainloop()
