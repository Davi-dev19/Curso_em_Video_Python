try:
    a = int(input('Digite o Númerador: '))
    b = int(input('Digite o Denominador: '))
    r = a / b
except:
    print('Infelizmente ocorreu um erro :(')
else:
    print(f'O resultado foi {r}')
finally:
    print('Volte sempre! Muito obrigado!')