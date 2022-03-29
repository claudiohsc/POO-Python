class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
        print(f'O retângulo foi criado com os lados: {self.lado_a} e {self.lado_b}.')
    
    def mudar_lado(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
        print(f'O retângulo foi modificado com os novos lados: {self.lado_a} e {self.lado_b}.')

    def valor_lados(self):
         print(f'Lado a vale: {self.lado_a} e o lado b vale: {self.lado_b}')
    
    def calcular_area(self):
        area = self.lado_a * self.lado_b
        print(f'A área do retângulo é: {area}')
    
    def calcular_perimetro(self):
        perimetro = (self.lado_a * 2) + (self.lado_b * 2)
        print(f'O perímetro do retângulo é: {perimetro}')
    

retangulo = Retangulo(10, 7)
retangulo.mudar_lado(15, 10)
retangulo.valor_lados()
retangulo.calcular_area()
retangulo.calcular_perimetro()


