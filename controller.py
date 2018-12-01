class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_listener(self.change)

    def change(self, value):
        fahrenheit = self.model.calc_fahrenheit(value)
        celsius = self.model.calc_celsius(value)
        self.view.set_values(fahrenheit, celsius)

    def start(self):
        self.change(0)
        self.view.show()