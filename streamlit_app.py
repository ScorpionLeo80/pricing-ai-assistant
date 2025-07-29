import streamlit as st
from src.nlp_parser import estrai_parametri
from src.pricing_engine import prezzo_obbligazione

st.set_page_config(page_title="AI Pricing Assistant", page_icon="💼")

st.title("💼 AI Assistant per il Pricing di Obbligazioni")
st.markdown("Inserisci una descrizione testuale dell'obbligazione e ottieni il prezzo teorico.")

# Campo input
input_text = st.text_area("📄 Descrizione obbligazione:", 
                          "Bond EUR, 5 anni, cedola fissa 2.5%, valore facciale 100, rendimento 3%")

# Calcolo
if st.button("📈 Calcola Prezzo"):
    try:
        parametri = estrai_parametri(input_text)
        prezzo = prezzo_obbligazione(**parametri)

        st.success(f"💰 Prezzo teorico: {prezzo} EUR")
        st.json(parametri)
    except Exception as e:
        st.error("⚠️ Errore nella lettura della descrizione. Controlla il formato del testo.")
        st.exception(e)
