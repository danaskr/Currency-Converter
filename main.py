import tkinter as tk

from forex_python.converter import CurrencyRates

common_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'NZD']


class CurrencyConverter:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Currency Converter')
        self.root.geometry('240x180')

        self.from_var = tk.StringVar(self.root)
        self.from_var.set('USD')
        self.from_menu = tk.OptionMenu(self.root, self.from_var, *common_currencies)
        self.from_menu.pack(pady=1)

        self.to_var = tk.StringVar(self.root)
        self.to_var.set('EUR')
        self.to_menu = tk.OptionMenu(self.root, self.to_var, *common_currencies)
        self.to_menu.pack(pady=1)

        self.amount_label = tk.Label(self.root, text='Amount:')
        self.amount_label.pack(pady=1)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=1)

        self.convert_button = tk.Button(self.root, text='Convert', command=self.convert_currency)
        self.convert_button.pack(pady=1)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=1)

        self.root.mainloop()

    def convert_currency(self):

        try:
            from_currency = self.from_var.get()
            print(from_currency)
            to_currency = self.to_var.get()
            print(to_currency)
            amount = float(self.amount_entry.get())
            print(amount)

            c = CurrencyRates()
            
            c_rates = CurrencyRates()

            rate = c_rates.get_rate(from_currency, to_currency)
            converted_amount = amount * rate

            self.result_label.config(text=f'{amount} {from_currency} = {converted_amount}{to_currency}')

        except ValueError:
            self.result_label.config(text='Please enter a valid number!')

        except Exception:
            self.result_label.config(text='Error Occurred!')
            print('error')


if __name__ == '__main__':
    CurrencyConverter()