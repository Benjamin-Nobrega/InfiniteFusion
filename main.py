from bs4 import BeautifulSoup
import requests

def getListaPkmn():
    lista = []
    with open("./fusioncalc.html") as fusion:
        soup = BeautifulSoup(fusion, "html.parser")
        datalist = soup.find("datalist", id="dlPkmn")
        options = datalist.find_all("option")
        for option in options:
            lista.append(option.get("value"))
    return lista

def fusoes(lista):
    lista_usados = []
    num = 1
    for i in lista:
        numPkmn = num
        for j in lista:
            if j not in lista_usados:
                print(i,num,j,numPkmn)
                numPkmn+=1
        num +=1
        lista_usados.append(i)

def getImagePkmn():
    x = requests.get("""
https://fusioncalc.com/wp-content/themes/twentytwentyone/pokemon/custom-fusion-sprites-main/CustomBattlers/420.1.png""")
    print(x.raw)

def main():
    #lista = getListaPkmn()
    #fusoes(lista)
    getImagePkmn()
if __name__ == "__main__":
    main()
