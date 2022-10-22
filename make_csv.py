import pdf_reader as pr
import check_kiids as ck
import pandas as pd
from stempel import StempelStemmer

def make_df():
    return pd.DataFrame(columns=[
    "ID_KIID",
    "ID_ZESPOLU",
    "NAZWA_SUBFUNDUSZU",
    "NAZWA_FUNDUSZU",
    "ISIN",
    "IDENTYFIKATOR_KRAJOWY",
    "NUMER_RFI",
    "PODMIOT_ZARZADZAJACY",
    "DATA_AKTUALIZACJI_KIID",
    "KATEGORIE_JEDNOSTEK_UCZESTNICTWA",
    "CEL_INWESTYCYJNY",
    "POLITKA_INWESTYCYJNA",
    "MINIMALNY_POZIOM_INWESTYCJI",
    "MAKSYMALNY_POZIOM_INWESTYCJI_UDZIALOWE",
    "MINIMALNY_POZIOM_INWESTYCJI_DLUZNE",
    "MAKSYMALNY_POZIOM_INWESTYCJI_DLUZNE",
    "MINIMALNY_POZIOM_INWESTYCJI_TYTULY_UCZESTNICTWA",
    "MINIMALNY_POZIOM_INWESTYCJI_TYTULY_UCZESTNICTWA",
    "CZESTOTLIWOSC_ZBYWANIA_I_ODKUPOWANIA_JEDNOSTEK_UCZESTNICTWA",
    "CZY_FUNDUSZ_WYPLACA_DYWIDENTE",
    "BENCHMARK",
    "ZALECANY_OKRES_INWESTYCJI",
    "PROFIL_RYZYKA_I_ZYSKU",
    "SRRI",
    "OPLATY",
    "OPLATA_ZA_NABYCIE",
    "OPLATA_ZA_ODKUPIENIE",
    "OPLATY_BIEZACE",
    "OPLATY_ZA_WYNIKI",
    "WYNIKI_OSIAGNIETE_W_PRZESZLOSCI",
    "STOPA_ZWROTU_2012",
    "STOPA_ZWROTU_2012_BENCHMARK",
    "STOPA_ZWROTU_2013",
    "STOPA_ZWROTU_2013_BENCHMARK",
    "STOPA_ZWROTU_2014",
    "STOPA_ZWROTU_2014_BENCHMARK",
    "STOPA_ZWROTU_2015",
    "STOPA_ZWROTU_2015_BENCHMARK",
    "STOPA_ZWROTU_2016",
    "STOPA_ZWROTU_2016_BENCHMARK",
    "STOPA_ZWROTU_2017",
    "STOPA_ZWROTU_2017_BENCHMARK",
    "STOPA_ZWROTU_2018",
    "STOPA_ZWROTU_2018_BENCHMARK",
    "STOPA_ZWROTU_2019",
    "STOPA_ZWROTU_2019_BENCHMARK",
    "STOPA_ZWROTU_2020",
    "STOPA_ZWROTU_2020_BENCHMARK",
    "STOPA_ZWROTU_2021",
    "STOPA_ZWROTU_2021_BENCHMARK",
    "DATA_PIERWSZEJ_WYCENY",
    "DEPOZYTARIUSZ",
    "KRS_TOWARZYSTWA",
    "NIP_TOWARZYSTWA",
    "SIEDZIBA_TOWARZYSTWA",
    "KAPITAL_ZAKLADOWAY_TOWARZYSTWA",
    "WALUTA_KAPITALU_ZAKLADOWEGO_TOWARZYSTWA",
    "CZY_ESG",
    "TYP_FUNDUSZ"    
])


if __name__ == "__main__":
    stemmer = StempelStemmer.polimorf()
    kiid_paths = ck.get_true_kiids()

    

full_df = make_df()
i = 1
for row,kiid_path in enumerate(kiid_paths):
    full_text = pr.extract(kiid_path)
    print(i)
    full_df.loc[row,:] = [
        i,
        28,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,#        pr._55(full_text,stemmer),
        pr._56(full_text),
        pr._57(full_text),
        None,
        pr._59(full_text)
    ] 
    i += 1
    
