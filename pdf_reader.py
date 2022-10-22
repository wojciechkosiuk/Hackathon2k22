import PyPDF2 as pdf

def extract_text(file_name):
    # podajesz nazwe pliku i otrzymujesz string z calej zawartosci
    # jest troche problem, ze wystepuja spacje dzielace niektore slowa (?)
    file = open(file_name,'rb')
    reader = pdf.PdfFileReader(file)
    
    full_text = ""
    for page_nr in range(reader.numPages):
        page = reader.getPage(page_nr)
        full_text += page.extract_text()

    full_text = full_text.replace('\n', ' ')
    return full_text



def main():
    # test
    file_name = "KIID_BNP_Paribas_DI_2022-09-21.pdf"
    print(extract_text(file_name))
    

if __name__ == "__main__":
    main()