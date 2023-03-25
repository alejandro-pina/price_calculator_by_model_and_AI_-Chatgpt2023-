# coding: utf-8
from token_pricing import TokenPricing

model = "gpt-3.5-turbo" # por ejemplo
tokens_in = 5000
tokens_out = 3000
pricing = TokenPricing(model)
input_price = pricing.input_price(tokens_in)
output_price = pricing.output_price(tokens_out)
total_price = pricing.total_price(tokens_in, tokens_out)
print("Input price: {:.2f} $".format(input_price))
print("Output price: {:.2f} $".format(output_price))
print("Total price:  {:.2f} $".format(total_price))


model = "gpt-3.5-turbo" # por ejemplo
pricing = TokenPricing(model)
tokens = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.'
tokens_in = pricing.calculate_tokens(tokens)
print('Tokens: {}'.format(tokens_in))
tokens_out = 3000
input_price = pricing.input_price(tokens_in)
output_price = pricing.output_price(tokens_out)
total_price = pricing.total_price(tokens_in, tokens_out)
print("Input price: {:.2f} $".format(input_price))
print("Output price: {:.2f} $".format(output_price))
print("Total price:  {:.2f} $".format(total_price))


model = "gpt-4-32k" # por ejemplo
pricing = TokenPricing(model)
input_tokens = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.'
output_tokens = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 5 ALEX PIÑA'

tokens_in = pricing.calculate_tokens(input_tokens)
print('Tokens: {}'.format(tokens_in))
tokens_out = pricing.calculate_tokens(output_tokens)
input_price = pricing.input_price(tokens_in)
output_price = pricing.output_price(tokens_out)
total_price = pricing.total_price(tokens_in, tokens_out)
print("Input price: {:.2f} $".format(input_price))
print("Output price: {:.2f} $".format(output_price))
print("Total price:  {:.2f} $".format(total_price))

pricing.save_token(tokens_in,tokens_out)

pricing.result_ia()