class arrayNumbers:
    #SE USO EL METODO DE SUMATORIA DE SERIE (SE DEBE TENER CUIDADO PARA SERIES MAS LARGAS YA QUE PUEDE PROVOCAR OVERFLOW DE LA MEMORIA)
    def extract(self, number):
        lst = list(range(1, 101))
        if number <= 100 and number > 0:
            lst.remove(number)
            print("Conjunto de numeros despues de extracción:")
            print(lst)
            n = len(lst)
            total = (n + 1) * (n + 2) / 2
            sum_of_A = sum(lst)
            return print("El numero que se extrajo fue: {}".format(total - sum_of_A))
        else:
            print("El  numero debe ser igual o menor a 100 y mayor a cero")

if __name__ == '__main__':
    print("Por favor introduce un numero entre 1 y 100:")
    num = int(input())
    api = arrayNumbers()
    api.extract(num)
