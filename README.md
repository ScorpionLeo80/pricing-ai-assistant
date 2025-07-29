
# 💼 AI Assistant per il Pricing di Obbligazioni

Questo progetto mostra un semplice assistente AI che, a partire da una descrizione testuale di un'obbligazione, calcola il suo prezzo teorico.

## 🔧 Esecuzione

```bash
pip install -r requirements.txt
python main.py
```

## 📥 Esempio input

```
Bond EUR, 5 anni, cedola fissa 2.5%, valore facciale 100, rendimento 3%
```

## 📤 Output atteso

```
📊 Parametri estratti: {'coupon': 2.5, 'durata': 5, 'ytm': 3.0, 'face_value': 100.0}
💰 Prezzo teorico: 97.71 EUR
```
