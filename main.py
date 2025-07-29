# from src.nlp_parser import estrai_parametri
from src.nlp_spacy_parser import estrai_parametri_spacy
from src.pricing_engine import prezzo_obbligazione

if __name__ == "__main__":
    testo_input = input("Inserisci la descrizione dell'obbligazione:\n> ")
    # parametri = estrai_parametri(testo_input)
    parametri = estrai_parametri_spacy(testo_input)
    prezzo = prezzo_obbligazione(**parametri)

    print(f"\n💰 Prezzo teorico: {prezzo} EUR")
    print(f"📊 Parametri estratti: {parametri}")
