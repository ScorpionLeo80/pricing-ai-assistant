# 💼 AI Assistant per il Pricing di Obbligazioni

Questo progetto implementa un assistente AI che, data una descrizione testuale di un'obbligazione a cedola fissa, calcola il suo prezzo teorico usando formule di finanza classica.

## 🧪 Esempio di utilizzo
```
> Bond EUR, 5 anni, cedola fissa 2.5%, valore facciale 100, rendimento 3%
💰 Prezzo teorico: 97.71 EUR
📊 Parametri estratti: {'coupon': 2.5, 'durata': 5, 'ytm': 3.0, 'face_value': 100.0}
```

## ▶️ Come eseguire
```bash
python main.py
```

## 📁 Struttura
- `src/nlp_parser.py` → parsing testo naturale
- `src/pricing_engine.py` → formula di pricing
- `main.py` → interfaccia CLI

## 📦 Requisiti
- Python 3.7+
- Nessuna libreria esterna (solo standard library)
