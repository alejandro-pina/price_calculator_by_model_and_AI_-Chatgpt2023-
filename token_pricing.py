# coding: utf-8
from prices import TOKEN_PRICES
import re
import os
import csv
import datetime

class TokenPricing:
    def __init__(self, model):
        import prices
        self.model = model
        self.prices = prices.TOKEN_PRICES[model]

    def calculate_tokens(self, prompt):
        prompt = prompt.strip()
        tokens = re.findall(r'\w+', prompt)
        num_tokens = len(tokens)
        return num_tokens

    def calculate_all_tokens(self, input_tokens, output_tokens):
        # Eliminar espacios al principio y fin
        prompt = prompt.strip()
        
        # Obtenemos todas las palabras
        input_tokens = re.findall(r'\w+', input_tokens)
        output_tokens = re.findall(r'\w+', output_tokens)

        # Tokens input y output
        num_input_tokens = len(input_tokens)
        num_output_tokens = len(output_tokens)
    
        # Tokens input y output en tupla
        return num_input_tokens + num_output_tokens
    
    def input_price(self, num_tokens):
        return num_tokens / 1000 * self.prices['input']

    def output_price(self, num_tokens):
        return num_tokens / 1000 * self.prices['output']

    def total_price(self, input_tokens, output_tokens):
        return self.input_price(input_tokens) + self.output_price(output_tokens)
    
    def save_token(self, num_input_tokens, num_output_tokens):
        header = ["fecha/hora", "modelo", "input token", "output token", "precio"]
        file_exists = os.path.isfile('tokens.csv') # True si el archivo existe
        # Para windows
        #with open('tokens.csv', 'a', newline='\n') as csvfile: 
        with open('tokens.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if not file_exists or os.stat('tokens.csv').st_size == 0:
                writer.writerow(header)
            timestamp = datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S')
            input_price = self.input_price(num_input_tokens)
            output_price = self.output_price(num_output_tokens)
            total_price = input_price + output_price
            writer.writerow([timestamp, self.model, num_input_tokens, num_output_tokens, total_price])

    def result_ia(self):
        with open('tokens.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            models = {}
            total_tokens = 0
            total_price = 0.0
            for row in reader:
                model = row['modelo']
                input_tokens = float(row['input token'])
                output_tokens = float(row['output token'])
                input_price = TOKEN_PRICES[model]['input'] / 1000 * input_tokens
                output_price = TOKEN_PRICES[model]['output'] / 1000 * output_tokens
                price = input_price + output_price
                if model not in models:
                    models[model] = {'tokens': 0, 'price': 0.0}
                models[model]['tokens'] += input_tokens + output_tokens
                models[model]['price'] += price
                total_tokens += input_tokens + output_tokens
                total_price += price
            print('\033[0m')
            print('\033[93m ***********************************************************************')
            print('\033[93m 💰 AI token price calculator')
            print('\033[93m ***********************************************************************')
            print('\033[0m')
            print('\033[96m[+] Results by model:\033[0m')
            for model, data in models.items():
                print("\033[94m[i] -> {}: \033[0m{} tokens, {} $".format(model,data["tokens"],data["price"]))
            print("\033[96m[+]\033[0m Tokens used: \033[92m{}\033[0m ".format(total_tokens))
            print("\033[96m[+]\033[0m Amount to pay: \033[0m \033[92m\033[1m{:.2f} $\033[0m ".format(total_price))


