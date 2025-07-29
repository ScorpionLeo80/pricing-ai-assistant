
import re

def estrai_parametri(testo):
    coupon = float(re.search(r'cedola.*?(\d+\.?\d*)%', testo).group(1))
    durata = int(re.search(r'(\d+)\s*(anni|year)', testo).group(1))
    rendimento = float(re.search(r'rendimento.*?(\d+\.?\d*)%', testo).group(1))
    valore_facciale = float(re.search(r'valore.*?(\d+)', testo).group(1))
    return {
        "coupon": coupon,
        "durata": durata,
        "ytm": rendimento,
        "face_value": valore_facciale
    }
