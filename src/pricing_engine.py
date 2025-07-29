
def prezzo_obbligazione(coupon, durata, ytm, face_value):
    r = ytm / 100
    prezzo = sum([coupon / (1 + r) ** t for t in range(1, durata + 1)])
    prezzo += face_value / (1 + r) ** durata
    return round(prezzo, 2)
