gasto = maismil = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: ')).upper()
    preco = float(input('Preço: R$'))
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    gasto += preco
    if preco > 1000:
        maismil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
        print('-' * 20)
    if resp == 'N':
        break
print('----------FIM DO PROGRAMA----------')
print(f'O total da compra foi R${gasto:.2f}')
print(f'Temos {maismil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')