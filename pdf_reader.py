import PyPDF2 as pdf

def extract(file_name):
    # podajesz nazwe pliku i otrzymujesz string z calej zawartosci i NAZWE_SUBFUNDUSZU znaleziona w pliku
    # jest troche problem, ze wystepuja spacje dzielace niektore slowa (?)
    file = open(file_name,'rb')
    reader = pdf.PdfFileReader(file)
    
    
    
    full_text = ""
    for page_nr in range(reader.numPages):
        page = reader.getPage(page_nr)
        full_text += page.extract_text()

    NAZWA_SUBFUNDUSZU = text.split("inwestycyjną.\n")[1].split("\n")[0]
    
    full_text = full_text.replace('\n', ' ')
    return full_text, NAZWA_SUBFUNDUSZU



def main():
    # test
    file_name = "KIID_BNP_Paribas_DI_2022-09-21.pdf"
    print(extract(file_name))
    

if __name__ == "__main__":
    main()
