def calcular_area(largura, comprimento):
    '''Calculando Área do terreno'''
    area = largura * comprimento
    print(f"A área do terreno: {largura:.1f}x{comprimento:.1f} é de: {area:.2f}m²")


print("-=" * 20)
print(f"{'-----Calculador de Área do terreno-----'}")
print("-=" * 20)
l = float(input("Qual a Largura do terreno? (m): "))
c = float(input("Qual o comprimento do terreno? (m): "))
calcular_area(l, c)