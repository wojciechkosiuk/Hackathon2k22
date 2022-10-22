import pdfplumber

def check_kiid(file_name):
    # podajesz nazwe pliku i zwraca TRUE gdy tekst zaczyna sie od "kluczowe informacje dla inwestorow"

    
    pdf = pdfplumber.open(file_name)
    text = pdf.pages[0].extract_text().lower()[1:200]
    return "kluczowe informacje dla inwestorów" in text

if __name__ == "__main__":
    #test
    file_name = "be4dbbf2-4e25-4053-87ba-52f13e939a48.pdf" 
    print(check_kiid(file_name))
