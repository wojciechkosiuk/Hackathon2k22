import os
import pdfplumber


def check_kiid(file_name):
    # podajesz nazwe pliku i zwraca TRUE gdy tekst zaczyna sie od "kluczowe informacje dla inwestorow"

    pdf = pdfplumber.open(file_name)
    text = pdf.pages[0].extract_text().lower()[1:200]
    return "kluczowe informacje dla inwestorów" in text

if __name__ == "__main__":
    listaFolderow = []
    dir_path= '/Users/adammajczyk/PycharmProjects/websraping/'
    for path in os.listdir(dir_path):
        # check if current path is a file
        if not os.path.isfile(os.path.join(dir_path, path)):
            listaFolderow.append(path)
    listaFolderow.remove(".idea")

    listaPlikow=[]
    for folder in listaFolderow:
        for path in os.listdir(dir_path + folder):
            # check if current path is a file
            if  os.path.isfile(os.path.join(dir_path + folder, path)):
                listaPlikow.append(dir_path + folder + "/" + path)


    kiids = []
    i = 1
    for plik in listaPlikow:
        print (i,":", plik, end = " ")
        try:
            if (check_kiid(plik)):
                kiids.append(plik)
                print("to KIID", end="")
            else:
                print("to nie KIID - usuwam", end = "")
                os.remove(plik)
        except:
            os.remove(plik)
            print("blad - usuwam")
        i+=1
        print("")


    print(kiids)
