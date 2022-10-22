import os
import pdfplumber

if not os.path.isdir("KIID"):
    os.mkdir("KIID")

def check_kiid(file_name):
    # podajesz nazwe pliku i zwraca TRUE gdy tekst zaczyna sie od "kluczowe informacje dla inwestorow"

    pdf = pdfplumber.open(file_name)
    text = pdf.pages[0].extract_text().lower()[1:200]
    pdf.close()
    return "kluczowe informacje dla inwestorów" in text



def get_kiids():
    listaFolderow = []
    dir_path= 'download/'
    for path in os.listdir(dir_path):
        # check if current path is a file
        if not os.path.isfile(os.path.join(dir_path, path)):
            listaFolderow.append(path)



    listaPlikow=[]
    for folder in listaFolderow:
        for path in os.listdir(dir_path + folder):
            # check if current path is a file
            if  os.path.isfile(os.path.join(dir_path + folder, path)):
                listaPlikow.append(dir_path + folder + "/" + path)


    if (len(listaPlikow)>0):
        kiids = []
        i = 1
        for plik in listaPlikow:
            indexDir = "{0:<10} {1:<10}".format(str(i)+"/"+ str(len(listaPlikow))+": ", plik)

            try:
                if (check_kiid(plik)):

                    nazwa_pliku=plik.split("/")[len(plik.split("/"))-1]
                    os.rename(plik, "KIID/" + nazwa_pliku)

                    lenght = 125
                    kiids.append(plik)
                    print("{:7s} {:125s} {:10s}".format(str(i)+"/"+ str(len(listaPlikow))+": ", plik, "!!!!!!to KIID!!!!!!"), end=" ")
                else:
                    print("{:7s} {:125s} {:10s}".format(str(i)+"/"+ str(len(listaPlikow))+": ", plik, "to nie KIID - usuwam"), end = " ")
                    os.remove(plik)
            except:
                try:
                    os.remove(plik)
                    print("{:7s} {:125s} {:10s}".format(str(i) + "/" + str(len(listaPlikow)) + ": ", plik, "blad - usuwam"), end=" ")
                except:
                    print("{:7s} {:125s} {:10s}".format(str(i) + "/" + str(len(listaPlikow)) + ": ", plik, "blad przy usuwaniu"), end=" ")


            i+=1
            print("")


        print(len(kiids))
    else:
        print("jest tyle samo plikow")
    return kiids
