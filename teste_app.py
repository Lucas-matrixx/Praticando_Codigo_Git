import app

a = 5
b = 4

soma = app.somar(a, b)
print(f'{a} + {b} = {soma}')


subtracao = app.subtrair(a, b)
print(f'{a} - {b} = {subtracao}')

multiplicacao = app.multiplicar(a, b)
print(f'{a} x {b} = {multiplicacao}')

divisao = app.dividir(a, b)
print(f'{a} / {b} = {divisao}')

radiciacao = app.potenciar(a, b)
print(f'{a} ^ {b} = {radiciacao}')

raiz_quadrada = app.raiz_sqrt(a)
print(f'sqrt({b}) = {raiz_quadrada}')

porcentagem = app.porcentagem(a, b)
print(f'{porcentagem}%')