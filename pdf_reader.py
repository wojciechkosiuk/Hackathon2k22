import pdfplumber

def extract(file_name):
    # podajesz nazwe pliku i otrzymujesz string z calej zawartosci i NAZWE_SUBFUNDUSZU znaleziona w pliku

    pdf = pdfplumber.open(file_name)
    
    
    
    full_text = ""
    for page in pdf.pages:
        full_text += page.extract_text()
        full_text += "\n"

    return full_text



def main():
    # test
    file_name = "KIID_BNP_Paribas_DI_2022-09-21.pdf"
    print(extract(file_name))
    

if __name__ == "__main__":
    main()
