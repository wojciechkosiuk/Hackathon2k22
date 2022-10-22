import re
import pdfplumber
import pandas as pd
import numpy as np
from stempel import StempelStemmer



def extract(file_name):
    # podajesz nazwe pliku i otrzymujesz string z calej zawartosci i NAZWE_SUBFUNDUSZU znaleziona w pliku

    pdf = pdfplumber.open(file_name)
    
    
    
    full_text = ""
    for page in pdf.pages:
        full_text += page.extract_text()
        full_text += "\n"

    return full_text



    

def _3(full_text):
    start_vec = full_text.split("inwestycyjną")[1].split("\n")
    NAZWA_SUBFUNDUSZU = [x for x in start_vec  if len(x)>2][0]
    return NAZWA_SUBFUNDUSZU


def _8(full_text):
    text_stemmed = full_text.lower().split("cele i polityka inwestycyjna")[0].split()
    tmp = [stemmer.stem(x)=="zarządzać" for x in full_text.lower().split("cele i polityka inwestycyjna")[0].split()]

    df = pd.DataFrame({'text':text_stemmed, 'boolvec':tmp})
    word = df[df['boolvec']==True]['text']

    if word.empty:
        return None
    else:
        stemmed = full_text.split(np.array(word)[0])[1].split("\n")[0].split('S.A.')[0] + "S.A."
        upper_words = [x[0].isupper() for x in stemmed.split()]
        words = np.array(stemmed.split())[upper_words]
        return " ".join(words)


def _9(full_text):
    DATA_AKTUALIZACJI_KIID = full_text.split("dzień")[-1].split("\n")[0]
    return DATA_AKTUALIZACJI_KIID


def _26(full_text):
    OPLATA_ZA_NABYCIE = full_text.lower().split("opłata za nabycie")[1].split()[0]
    return OPLATA_ZA_NABYCIE


def _27(full_text):
    if len(full_text.lower().split("opłata za odkupienie"))==1:
        if len(full_text.lower().split("opłata za umorzenie"))==1:
            return None
        else:
            OPLATA = full_text.lower().split("opłata za umorzenie")[1].split()[0]
    else:
        OPLATA = full_text.lower().split("opłata za odkupienie")[1].split()[0]
    return OPLATA



def _28(full_text):
    try:
        OPLATY_BIEZACE = full_text.lower().split("opłaty bieżące")[1].split()[0]
    except:
        return None
    return OPLATY_BIEZACE


def _29(full_text):
    try:
        OPLATY_ZA_WYNIKI = full_text.lower().split("opłaty za wyniki")[1].split()[0]
    except:
        return None
    return OPLATY_ZA_WYNIKI 


def _3150(full_text): 
    #bo od 31 do 50
    if len(re.split(r'\n[0-9]{4} ',full_text))<2:
        return None
    
    tmp = re.split(r'\n[0-9]{4} ',full_text)[1].split("\n")[0:6]
    tmp = [re.sub("[a-z]|[A-Z]", "", x) for x in tmp]
    tmp = [re.sub("[.?!]", "", x) for x in tmp]
    years = re.findall(r"[0-9]{4}",tmp[0])
    values = []
    for row in tmp[1:]:
        if len(re.findall('%',row))!=0:
            values.append(row)

    years.insert(0,int(years[0])-1)

    values = [x.split() for x in values]
    return pd.DataFrame({'Years':years,'Values':values[0],'Values_benchmark':values[1]})



def _52(full_text):
    try:
        name = full_text.lower().split("depozytariuszem")[1].split(". ")[0].split("jest")[1]
    except:
        return None
    return name



def _53(full_text):
    try:
        krs = re.findall(r'[0-9]{10}',full_text.lower().split("informacje praktyczne")[1])
    except:
        return None
    return krs


def _54(full_text):
    try:
        nip = re.findall(r'[0-9]{3}-[0-9]{2}-[0-9]{2}-[0-9]{3}',full_text.lower().split("informacje praktyczne")[1])
    except:
        return None
    return nip



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

def get_list_of_currencies():
    # returns df of abbreviations and iso of currencies
    # used in _57()
    currencies = pd.read_csv("List_of_circulating_currencies_1.csv",sep=',')[['Symbol or\nAbbrev.', 'ISO code']]
    currencies.columns = ['abbr','iso']
    currencies.drop_duplicates(subset = "abbr", inplace = True)
    return currencies

def _57(full_text,currencies):
    # returnuje walute kapitału (ostatni akapit)
    try:
        # currencies = get_list_of_currencies()
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
    stemmer = StempelStemmer.polimorf()
    currencies = get_list_of_currencies()
    

if __name__ == "__main__":
    main()
