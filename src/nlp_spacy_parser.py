import spacy
import re

# Carica il modello spaCy inglese
nlp = spacy.load("en_core_web_sm")

def estrai_parametri_spacy(testo):
    doc = nlp(testo)

    parametri = {
        "coupon": None,
        "durata": None,
        "ytm": None,
        "face_value": None
    }

    for i, token in enumerate(doc):
        # Cedola / interesse
        if token.lemma_.lower() in ["cedola", "interesse", "coupon", "paga"]:
            next_val = _get_percent_value(doc, i)
            if next_val: parametri["coupon"] = next_val

        # Durata
        if token.lemma_ in ["anno", "anni", "durata", "termine", "scade", "maturare"]:
            next_val = _get_numeric_value(doc, i)
            if next_val: parametri["durata"] = next_val

        # Rendimento
        if token.lemma_ in ["ytm", "rendimento", "yield", "interesse", "tasso"]:
            next_val = _get_percent_value(doc, i)
            if next_val: parametri["ytm"] = next_val

        # Valore facciale
        if token.lemma_ in ["valore", "faccia", "facciale", "nominale", "importo"]:
            next_val = _get_numeric_value(doc, i)
            if next_val: parametri["face_value"] = next_val

    # Check finale
    for key in parametri:
        if parametri[key] is None:
            raise ValueError(f"Parametro mancante o non riconosciuto: {key}")

    return parametri

def _get_percent_value(doc, index):
    for token in doc[index:index+5]:
        m = re.search(r"(\d+\.?\d*)\s*%", token.text)
        if m:
            return float(m.group(1))
    return None

def _get_numeric_value(doc, index):
    for token in doc[index:index+5]:
        try:
            return int(token.text)
        except ValueError:
            try:
                return float(token.text)
            except ValueError:
                continue
    return None
