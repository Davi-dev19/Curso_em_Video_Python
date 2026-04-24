try:
    a = int(input('Digite o Númerador: '))
    b = int(input('Digite o Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você informou.')
except ZeroDivisionError:
    print('não é possivel dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário decidiu não informar informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi: {erro.__cause__}')
else:
    print(f'O resultado foi {r:.2f}')
finally:
    print('Volte sempre! Muito obrigado!')