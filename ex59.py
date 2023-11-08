n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
      print('=' * 25)
      print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos '
            'números\n[5] Sair do programa')
      print('=' * 25)
      menu = int(input('Qual o número do menu que desejas? '))
      if menu == 1:
            print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
      elif menu == 2:
            print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
      elif menu == 3:
            if n1 > n2:
                  print('O maior número entre {} e {} é o {}'.format(n1, n2, n1))
            else:
                  print('O maior número entre {} e {} é o {}'.format(n1, n2, n2))
      elif menu == 4:
            print('Digite os novos números')
            n1 = float(input('Digite o primeiro valor: '))
            n2 = float(input('Digite o segundo valor: '))
      elif menu == 5:
            print('Saindo do programa...')
      else:
            print('Digito inválido, digite novamente!')

