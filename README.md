# Price calculator by model and AI (Chatgpt 2023)

Token Pricing is a Python application for calculating the number of tokens, input price per entry and output according to the model, and the total price. It also has the ability to save tokens along with the price and date in a CSV and includes a function to display the results.

## Installation

```bash
pip csv
```

## Usage

To use Token Pricing, you will need to import the TokenPricing class from the token_pricing.py file.
```python
from token_pricing import TokenPricing

```

### Example
```python
from token_pricing import TokenPricing
model = "gpt-4-32k" # por ejemplo
pricing = TokenPricing(model)
input_tokens = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.'
output_tokens = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen ALEX PIÑA.'

tokens_in = pricing.calculate_tokens(input_tokens)
print('Tokens: {}'.format(tokens_in))
tokens_out = pricing.calculate_tokens(output_tokens)
input_price = pricing.input_price(tokens_in)
output_price = pricing.output_price(tokens_out)
total_price = pricing.total_price(tokens_in, tokens_out)
print("Input price: {:.2f} $".format(input_price))
print("Output price: {:.2f} $".format(output_price))
print("Total price:  {:.2f} $".format(total_price))


pricing.result_ia()
```

## CSV Saving

Token Pricing also has the ability to save tokens along with the price and date in a CSV. To save the data, you can use the save_tokens method of the TokenPricing class.
```python
pricing.save_token(tokens_in,tokens_out)
```

### Results
To display the results of all the saved tokens, you can use the result_ia method of the TokenPricing class.

```python
pricing.result_ia()
```

## Files
The Token Pricing application consists of three files:

### token_pricing.py

This file contains the TokenPricing class, which includes all the methods for calculating the number of tokens, input price per entry and output according to the model, and the total price. It also includes the methods for saving tokens and displaying the results.

### prices.py
This file contains the TOKEN_PRICES dictionary, which includes the constant prices for each model.

### examples.py
This file contains example usage of the TokenPricing class.

Models and Prices
Here's a list of the models currently supported by Token Pricing and their respective prices:

```ssh
gpt-4-8k: Input: 0.03$, Output: 0.06$
gpt-4-32k: Input: 0.06$, Output: 0.12$
gpt-3.5-turbo: Input: 0.002$, Output: 0.002$
ada: Input: 0.0004$, Output: 0.0016$
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
