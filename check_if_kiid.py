import PyPDF2 as pdf

def check_kiid(file_name):
    # podajesz nazwe pliku i zwraca TRUE gdy tekst zaczyna sie od "kluczowe informacje dla inwestorow"

    file = open(file_name,'rb')
    reader = pdf.PdfFileReader(file)
    pageObj = reader.getPage(0)
    text = pageObj.extract_text()
    text_ = text.lower()[1:200]
    return "kluczowe informacje dla inwestorów" in text_   

if __name__ == "__main__":
    #test
    file_name = "KIID_BNP_Paribas_DI_2022-09-21.pdf" 
    print(check_kiid(file_name))
