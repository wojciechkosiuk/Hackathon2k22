import re
import pdfplumber
import pandas as pd


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


def _56(full_text):
    return float(re.findall(r'\W[0-9 ]{3,}[,.]{1}[\d]+\w',full_text)[0].replace(',','.'))

def _57(full_text):
    # returnuje walute kapitału (ostatni akapit)
    currencies = get_list_of_currencies()
    inf_prak = full_text.lower().split("informacje praktyczne")[1].split()
    indices = [i for i, x in enumerate(inf_prak) if x in currencies.abbr.values]
    for i in indices:
        abbr = (inf_prak[i])    
    ISO = currencies[currencies['abbr'] == abbr].iso.values[0]
    return ISO

def _59(full_text):
    # dostaje caly text zwraca _59 - SFIO/FIO/None
    if len(re.findall("SFIO",full_text)) > 0:
        return "SFIO"
    elif len(re.findall("FIO",full_text)) > 0:
        return "FIO"
    return None




def main():
    # test
    # file_name = "KIID_BNP_Paribas_DI_2022-09-21.pdf"
    # text, subfundusz = extract(file_name) 
    # print(_59(text))
    pass
    

if __name__ == "__main__":
    main()
