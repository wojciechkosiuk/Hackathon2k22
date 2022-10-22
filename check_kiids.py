import os
import pdfplumber

def check_kiid(file_name):
    # podajesz nazwe pliku i zwraca TRUE gdy tekst zaczyna sie od "kluczowe informacje dla inwestorow"

    pdf = pdfplumber.open(file_name)
    text = pdf.pages[0].extract_text().lower()[1:200]
    return "kluczowe informacje dla inwestorów" in text

def get_true_kiids():
    listaFolderow = []
    dir_path= os.path.join(os.path.abspath(os.getcwd()), 'webscrapping')
    for path in os.listdir(dir_path):
        # check if current path is a file
        if not os.path.isfile(os.path.join(dir_path, path)):
            listaFolderow.append(path)
    if ".idea" in listaFolderow:
        listaFolderow.remove(".idea")

    listaPlikow=[]
    for folder in listaFolderow:
        folder_path = os.path.join(dir_path, folder)
        dir = os.listdir(folder_path)
        for path_ in dir:
            # # check if current path is a file
            file_path = os.path.join(folder_path,path_)
            if os.path.isfile(file_path):
                listaPlikow.append(file_path)

    kiids = []
    i = 1
    print("checking if files are KIIDs")
    for plik in listaPlikow:
        try:
            if (check_kiid(plik)):
                kiids.append(plik)
            else:
                os.remove(plik)
        except:
            os.remove(plik)
            i+=1
    return kiids
        
# if __name__ == "__main__":
#     print(get_true_kiids())


