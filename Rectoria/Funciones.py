def calcularPromedio(lista):
    """
        :parametro lista: list
        :return float
    """
    if not lista:
        return 0
    sum = 0
    for valor in lista:
        if type(valor) is list:
            sum += calcularPromedio(valor)
        else:
            sum += valor
    return sum/len(lista)