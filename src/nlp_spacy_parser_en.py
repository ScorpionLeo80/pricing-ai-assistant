import spacy
import re

# Load English model
nlp = spacy.load("en_core_web_sm")

def estrai_parametri_spacy(testo):
    doc = nlp(testo)

    parametri = {
        "coupon": None,
        "durata": None,
        "ytm": None,
        "face_value": None
    }

    percentuali_trovate = []

    for i, token in enumerate(doc):
        lemma = token.lemma_.lower()

        # Coupon / interest
        if lemma in ["coupon", "interest", "pays", "fixed"]:
            next_val = _get_percent_value(doc, i)
            if next_val:
                parametri["coupon"] = next_val
                percentuali_trovate.append(next_val)

        # Duration / maturity
        if lemma in ["year", "term", "maturity", "duration", "expire", "mature"]:
            next_val = _get_numeric_value(doc, i)
            if next_val:
                parametri["durata"] = next_val

        # Yield / YTM
        if lemma in ["ytm", "yield", "return", "rate"]:
            next_val = _get_percent_value(doc, i)
            if next_val:
                parametri["ytm"] = next_val
                percentuali_trovate.append(next_val)

        # Face value / nominal
        if lemma in ["value", "face", "nominal", "amount"]:
            next_val = _get_numeric_value(doc, i)
            if next_val:
                parametri["face_value"] = next_val

    # Fallback if coupon or ytm not explicitly found
    if (parametri["coupon"] is None or parametri["ytm"] is None) and len(percentuali_trovate) >= 1:
        if parametri["coupon"] is None:
            parametri["coupon"] = percentuali_trovate[0]
        if len(percentuali_trovate) >= 2 and parametri["ytm"] is None:
            parametri["ytm"] = percentuali_trovate[1]

    # Final check
    for key in parametri:
        if parametri[key] is None:
            raise ValueError(f"Missing or unrecognized parameter: {key}")

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
