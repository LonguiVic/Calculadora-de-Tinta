# Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
# O usuário deverá fornecer as seguintes informações: Rendimento; Altura; Largura.
# O programa deve mostrar na tela a mensagem 'Você necessita de X latas de tinta.'


rendimento = float(input('Qual é o rendimento da lata? '))
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))


def calc_tinta():
    area = altura * largura
    total = area / rendimento
    print(f'Você precisa de {total} latas de tinta')


calc_tinta()
