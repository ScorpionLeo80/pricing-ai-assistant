
from src.nlp_parser import estrai_parametri
from src.pricing_engine import prezzo_obbligazione

def main():
    testo_input = input("Inserisci la descrizione del bond:\n")
    parametri = estrai_parametri(testo_input)
    prezzo = prezzo_obbligazione(**parametri)
    print(f"\n📊 Parametri estratti: {parametri}")
    print(f"💰 Prezzo teorico: {prezzo} EUR")

if __name__ == "__main__":
    main()
