try:
    a = int(input('Digite o Númerador: '))
    b = int(input('Digite o Denominador: '))
    r = a / b
except Exception as erro:
    print(f'O erro encontrado foi: {erro.__class__}')
else:
    print(f'O resultado foi {r}')
finally:
    print('Volte sempre! Muito obrigado!')