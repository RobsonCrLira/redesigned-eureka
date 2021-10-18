import re


class Util():
    def findHTML(tag, nameClass, str):
        if str.find(tag, attrs={'class': nameClass}) is not None:
            valor = str.find(tag, attrs={'class': nameClass}).text
            return valor.replace("\n", "").strip().replace("\xa0", " ")
        else:
            return "Informação não encontrado"

    def findValores(tag, nameClass, str):
        if str.find(tag, attrs={'class': nameClass}) is not None:
            valor = str.find(tag, attrs={'class': nameClass}).text
            return re.findall('[0-9]+', valor)
        else:
            return "Informação não encontrado"
