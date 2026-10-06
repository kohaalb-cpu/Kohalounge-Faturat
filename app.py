import streamlit as st
import pandas as pd

# Load or initialize data
if "db" not in st.session_state:
    st.session_state.db = pd.DataFrame(columns=["Kodi", "Artikulli", "Paketimi", "Sasia", "Cmimi_Kaluar", "Cmimi_Konkurrences"])

st.title("Sistemi i Kontrollit të Faturave")

# Input section
artikujt = ["Kafe Espresso", "Lëng Portokalli", "Ujë 0.25l"]
art_ri = st.selectbox("Zgjidh Artikullin:", artikujt)

# Example placeholder row data
row = {"Sasia": 10, "Cmimi_Kaluar": 1.40}

st.info(f"Paketimi standard: Pako ({row['Sasia']} copë) | Çmimi i kaluar për copë: {row['Cmimi_Kaluar']} €")

cmimi_fatures_pakete = st.number_input("Fut çmimin total të faturës për këtë paketë (€):", value=15.00, step=0.10)

if st.button("Llogarit dhe Kontrollo Çmimin"):
    cmimi_per_cope = cmimi_fatures_pakete / row["Sasia"]
    diferenca = cmimi_per_cope - row["Cmimi_Kaluar"]
    pind = (
        (diferenca / row["Cmimi_Kaluar"]) * 100
        if row["Cmimi_Kaluar"] > 0
        else 0
    )
    st.metric(
        label="Çmimi i Ri për Copë",
        value=f"{cmimi_per_cope:.2f} €",
        delta=f"{diferenca:.2f} €",
        delta_color="inverse"
    )
    if diferenca > 0:
        st.error("⚠️ KUJDES: Çmimi është rritur krahasuar me blerjen e kaluar.")
    elif diferenca < 0:
        st.success("🎉 KURSIM: Çmimi ka rënë krahasuar me herën e kaluar.")
    else:
        st.info("ℹ️ Çmimi ka mbetur i pandryshuar.")
