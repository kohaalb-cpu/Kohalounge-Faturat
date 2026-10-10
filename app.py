import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Koha Lounge - Kontrolli i Faturave", layout="wide"
)

st.title("🍹 Koha Lounge - Skanimi i Faturës & Kontrolli i Çmimeve")
st.write(
    "Fotografo faturën, zgjidh furnitorin dhe kontrollo çmimet e të gjithë"
    " artikujve njëherësh."
)

if "db" not in st.session_state:
  st.session_state.db = pd.DataFrame([
      {
          "Furnitori": "Viva Fresh Store",
          "Artikulli": "Supe gjeli Podravka 62gr",
          "Kategoria": "Ushqimore",
          "Njesia": "Copë",
          "Sasia": 35.0,
          "Cmimi_Kaluar": 0.42,
      },
      {
          "Furnitori": "Viva Fresh Store",
          "Artikulli": "Detergjent per ene Det Lemon 900 ml",
          "Kategoria": "Sanitative",
          "Njesia": "Litër",
          "Sasia": 36.0,
          "Cmimi_Kaluar": 0.89,
      },
      {
          "Furnitori": "Viva Fresh Store",
          "Artikulli": "Pule e ngrire Dippy 900gr",
          "Kategoria": "Mish/Ushqim",
          "Njesia": "Kg",
          "Sasia": 50.0,
          "Cmimi_Kaluar": 2.24,
      },
      {
          "Furnitori": "Kosmonte Foods",
          "Artikulli": "Kaqkavall Edamer",
          "Kategoria": "Ushqimore",
          "Njesia": "Kg",
          "Sasia": 1.0,
          "Cmimi_Kaluar": 4.90,
      },
      {
          "Furnitori": "Kosmonte Foods",
          "Artikulli": "Cheese Burger",
          "Kategoria": "Ushqimore",
          "Njesia": "Komplet",
          "Sasia": 10.0,
          "Cmimi_Kaluar": 1.10,
      },
      {
          "Furnitori": "Kosmonte Foods",
          "Artikulli": "Ajvar",
          "Kategoria": "Ushqimore",
          "Njesia": "Kg",
          "Sasia": 1.0,
          "Cmimi_Kaluar": 2.90,
      },
      {
          "Furnitori": "Dauti - Komerc",
          "Artikulli": "Krip",
          "Kategoria": "Ushqimore",
          "Njesia": "Kg",
          "Sasia": 1.0,
          "Cmimi_Kaluar": 0.456,
      },
      {
          "Furnitori": "Dauti - Komerc",
          "Artikulli": "Uthull e bardhë",
          "Kategoria": "Ushqimore",
          "Njesia": "Litër",
          "Sasia": 1.0,
          "Cmimi_Kaluar": 0.59,
      },
      {
          "Furnitori": "N.T.P. 1Maji-X",
          "Artikulli": "Qumësht",
          "Kategoria": "Banak",
          "Njesia": "Komplet",
          "Sasia": 12.0,
          "Cmimi_Kaluar": 8.00,
      },
      {
          "Furnitori": "N.T.P. 1Maji-X",
          "Artikulli": "Coca Cola 0.25l",
          "Kategoria": "Banak",
          "Njesia": "Komplet",
          "Sasia": 24.0,
          "Cmimi_Kaluar": 12.50,
      },
      {
          "Furnitori": "Dinamika Sh.p.k.",
          "Artikulli": "Suxhuk",
          "Kategoria": "Kuzhinë",
          "Njesia": "Kg",
          "Sasia": 1.0,
          "Cmimi_Kaluar": 7.80,
      },
      {
          "Furnitori": "Salespoint G&S",
          "Artikulli": "Palloma katrore",
          "Kategoria": "Sanitative",
          "Njesia": "Copë",
          "Sasia": 10.0,
          "Cmimi_Kaluar": 0.92,
      },
  ])

opsioni = st.sidebar.selectbox(
    "Zgjidh Opsionin",
    [
        "📦 Kontrollo Faturën (Të Gjithë Artikujt)",
        "📸 Skano Faturën e Furnitorit (Kamera)",
        "📋 Tabela e Inventarit",
    ],
)

if opsioni == "📦 Kontrollo Faturën (Të Gjithë Artikujt)":
  st.subheader("🏢 Kontrolli i Faturës sipas Furnitorit")
  furnitoret = sorted(st.session_state.db["Furnitori"].unique())
  zgjidh_furnitor = st.selectbox(
      "Zgjidh furnitorin që ka sjellë faturën:", furnitoret
  )

  df_f = st.session_state.db[
      st.session_state.db["Furnitori"] == zgjidh_furnitor
  ]

  if not df_f.empty:
    st.info(
        f"U gjetën **{len(df_f)} artikuj** për furnitorin **{zgjidh_furnitor}**."
        " Plotëso çmimet e reja totale të faturës për secilin artikull:"
    )

    rezultatet = []
    # Krijojmë fusha inputi për secilin artikull të këtij furnitori
    for idx, row in df_f.iterrows():
      st.markdown(f"---")
      col1, col2, col3 = st.columns([2, 1, 1])

      with col1:
        st.write(
            f"**{row['Artikulli']}**\n\n*Kategoria:* {row['Kategoria']} |"
            f" *Njësia:* {row['Njesia']} (Sasia: {row['Sasia']})"
        )
        st.text(f"Çmimi i kaluar i referencës: {row['Cmimi_Kaluar']} €")

      with col2:
        cmim_fature = st.number_input(
            f"Çmimi i faturës (€) - {row['Artikulli']}",
            min_value=0.0,
            value=float(row["Cmimi_Kaluar"]),
            step=0.05,
            key=f"cf_{idx}",
        )

      with col3:
        cmim_per_njesi = (
            cmim_fature / row["Sasia"] if row["Sasia"] > 0 else cmim_fature
        )
        diferenca = cmim_per_njesi - row["Cmimi_Kaluar"]

        st.metric(
            label="Për Njësi",
            value=f"{cmim_per_njesi:.3f} €",
            delta=f"{diferenca:+.3f} €",
        )

        if diferenca > 0:
          st.error("⚠️ Rritur")
        elif diferenca < 0:
          st.success("🎉 Ulur")
        else:
          st.info("ℹ️ Njëjtë")

  else:
    st.warning("Nuk u gjetën produkte për këtë furnitor.")

elif opsioni == "📸 Skano Faturën e Furnitorit (Kamera)":
  st.subheader("📸 Skano Faturën me Kamerë dhe Llogarit Të Gjithë Artikujt")
  foto_kamera = st.camera_input("Bëj foto të faturës së furnitorit")

  if foto_kamera is not None:
    st.success("Fatura u fotografua me sukses!")
    furn_skan = st.selectbox(
        "Zgjidh Furnitorin e kësaj fature:",
        sorted(st.session_state.db["Furnitori"].unique()),
        key="fs_all",
    )

    df_s = st.session_state.db[st.session_state.db["Furnitori"] == furn_skan]

    st.markdown(
        f"### Llogaritja e faturës për: {furn_skan} (Të gjithë artikujt)"
    )

    for idx, row in df_s.iterrows():
      st.markdown(f"---")
      c1, c2, c3 = st.columns([2, 1, 1])
      with c1:
        st.write(
            f"**{row['Artikulli']}**\n\n*Sasia:* {row['Sasia']} {row['Njesia']}"
            f" | *Referenca:* {row['Cmimi_Kaluar']} €"
        )
      with c2:
        val_fakt = st.number_input(
            f"Totali (€) - {row['Artikulli']}",
            min_value=0.0,
            value=float(row["Cmimi_Kaluar"]),
            step=0.05,
            key=f"scf_{idx}",
        )
      with c3:
        nje_s = val_fakt / row["Sasia"] if row["Sasia"] > 0 else val_fakt
        dif_s = nje_s - row["Cmimi_Kaluar"]
        st.metric(
            label="Çmimi/Njësi",
            value=f"{nje_s:.3f} €",
            delta=f"{dif_s:+.3f} €",
        )
        if dif_s > 0:
          st.error("⚠️ Rritur")
        elif dif_s < 0:
          st.success("🎉 Ulur")
        else:
          st.info("ℹ️ Njëjtë")

elif opsioni == "📋 Tabela e Inventarit":
  st.subheader("📋 Tabela e Produkteve & Çmimeve")
  st.dataframe(st.session_state.db, use_container_width=True)
