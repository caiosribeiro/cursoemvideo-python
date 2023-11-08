'''try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não interferir os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')'''
def leiaint(msg):
    while True:
        try:
            x = int(input(msg))
            return x
        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar esse número\033[m')
            return 0

        except:
            print('\033[0;31mERRO: por favor, digite um número válido.\033[m')



def leiafloat(msg):
    while True:
        try:
            x = float(input(msg))
            return x
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número\033[m')
            return 0
        except:
            print('\033[0;31mERRO: por favor, digite um número válido.\033[m')



n1 = leiaint('Digite um número inteiro:')
n2 = leiafloat('Digite um número real:')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')