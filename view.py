import tkinter as tk

class View:
    def __init__(self):
        self.listener = None

        self.window = tk.Tk()
        self.window.title("F/C Umrechnung")
        self.window.resizable(False, False)

        self.heading = tk.Label(self.window, text="Celsius/Fahrenheit Umrechnung", font="Helvetica 11 bold")
        self.heading.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.entry = tk.Scale(self.window, command=self.trigger_event, from_=-200, to=200, orient=tk.HORIZONTAL)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=tk.W + tk.E, padx=20)

        self.fahrenheit = tk.Label(self.window, font="Helvetica 9 bold")
        self.fahrenheit.grid(row=2, column=0, pady=10)

        self.celsius = tk.Label(self.window, font="Helvetica 9 bold")
        self.celsius.grid(row=2, column=1, pady=10)

    def trigger_event(self, value):
        if self.listener:
            self.listener(int(value))

    def set_listener(self, listener):
        self.listener = listener

    @property
    def value(self):
        return self.entry.get()

    def set_values(self, fahrenheit, celsius):
        self.fahrenheit['text'] = "{:.2f}° C ist\n {:.2f}° F".format(self.value, fahrenheit)
        self.celsius['text'] = "{:.2f}° F ist\n {:.2f}° C".format(self.value, celsius)

    def show(self):
        self.window.mainloop()
