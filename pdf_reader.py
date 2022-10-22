import re
import pdfplumber
import pandas as pd
# from stempel import StempelStemmer



def extract(file_name):
    # podajesz nazwe pliku i otrzymujesz string z calej zawartosci i NAZWE_SUBFUNDUSZU znaleziona w pliku

    pdf = pdfplumber.open(file_name)
    
    
    
    full_text = ""
    for page in pdf.pages:
        full_text += page.extract_text()
        full_text += "\n"

    return full_text


def get_list_of_currencies():
    # returns df of abbreviations and iso of currencies
    currencies = pd.read_csv("List_of_circulating_currencies_1.csv",sep=',')[['Symbol or\nAbbrev.', 'ISO code']]
    currencies.columns = ['abbr','iso']
    currencies.drop_duplicates(subset = "abbr", inplace = True)
    return currencies


def _55(full_text,stemmer):
    # returnuje adres jaki tam znajdzie w pliku
    inf_prak = full_text.lower().split("informacje praktyczne")[1]
    
    #wywalić go potem z funkcji bo nie ma sensu go ladowac za kazdym razem

    # stemmer = StempelStemmer.polimorf()
    try:
        adres = re.findall(r'ul\. \w+ \d+,{0,1} \d+-\d+ \w+',inf_prak)
        adres_split = adres[0].split()
        adres_split[1] = stemmer.stem(adres_split[1])
    except:
        return None
    return  " ".join(adres_split)


def _56(full_text):
    try:
        return float(re.findall(r'\W[0-9 ]{3,}[,.]{1}[\d]+\w',full_text)[0].replace(',','.'))
    except:
        return None

def _57(full_text):
    # returnuje walute kapitału (ostatni akapit)
    try:
        currencies = get_list_of_currencies()
        inf_prak = full_text.lower().split("informacje praktyczne")[1].split()
        indices = [i for i, x in enumerate(inf_prak) if x in currencies.abbr.values]
        for i in indices:
            abbr = (inf_prak[i])    
        ISO = currencies[currencies['abbr'] == abbr].iso.values[0]
        return ISO
    except:
        return None

def _59(full_text):
    # dostaje caly text zwraca _59 - SFIO/FIO/None

    try:
        if len(re.findall("SFIO",full_text)) > 0:
            return "SFIO"
        elif len(re.findall("FIO",full_text)) > 0:
            return "FIO"
    except:
        return None
    return None




def main():
    # test
    # file_name = "be4dbbf2-4e25-4053-87ba-52f13e939a48.pdf"
    # text = extract(file_name) 
    # print(text)
    
    pass
    

if __name__ == "__main__":
    main()