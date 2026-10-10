import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Koha Lounge - Kontrolli i Faturave", layout="centered"
)

st.title("🍹 Koha Lounge - Menaxhimi & Skanimi i Faturave")
st.write(
    "Zgjidh furnitorin, bëj foto faturës me kamerë dhe kontrollo çmimet në kohë"
    " reale."
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
        "📦 Kontrollo Faturën sipas Furnitorit",
        "📸 Skano me Kamerë të Telefonit",
        "📋 Tabela e Inventarit",
    ],
)

if opsioni == "📦 Kontrollo Faturën sipas Furnitorit":
  st.subheader("🏢 Zgjidh Furnitorin dhe Produktet")
  furnitoret = sorted(st.session_state.db["Furnitori"].unique())
  zgjidh_furnitor = st.selectbox(
      "Zgjidh furnitorin që ka sjellë mallin:", furnitoret
  )

  df_f = st.session_state.db[
      st.session_state.db["Furnitori"] == zgjidh_furnitor
  ]

  if not df_f.empty:
    artikulli_z = st.selectbox("Zgjidh Artikullin:", df_f["Artikulli"])
    row = df_f[df_f["Artikulli"] == artikulli_z].iloc[0]

    st.info(
        f"**Kategoria:** {row['Kategoria']} | **Njësia:** {row['Njesia']} (Sasia:"
        f" {row['Sasia']})\n\n**Çmimi i kaluar i referencës:**"
        f" {row['Cmimi_Kaluar']} €"
    )

    cmim_fature = st.number_input(
        "Fut çmimin total të faturës për këtë produkt (€):",
        min_value=0.0,
        value=float(row["Cmimi_Kaluar"]),
        step=0.05,
    )

    if st.button("Llogarit dhe Krahaso Çmimin"):
      cmim_per_njesi = (
          cmim_fature / row["Sasia"] if row["Sasia"] > 0 else cmim_fature
      )
      diferenca = cmim_per_njesi - row["Cmimi_Kaluar"]

      st.metric(
          label="Çmimi i Ri për Njësi",
          value=f"{cmim_per_njesi:.3f} €",
          delta=f"{diferenca:+.3f} €",
      )

      if diferenca > 0:
        st.error(
            "⚠️ KUJDES: Çmimi është rritur krahasuar me blerjen e fundit!"
        )
      elif diferenca < 0:
        st.success(
            "🎉 KURSIM: Çmimi ka rënë krahasuar me herën e kaluar!"
        )
      else:
        st.info("ℹ️ Çmimi ka mbetur i pandryshuar.")
  else:
    st.warning("Nuk u gjetën produkte për këtë furnitor.")

elif opsioni == "📸 Skano me Kamerë të Telefonit":
  st.subheader("📸 Skano Faturën direkt me Kamerë")
  st.write(
      "Kliko butonin më poshtë për të hapur kamerën e telefonit dhe për të"
      " fotografuar faturën:"
  )

  # Kjo hap direkt kamerën e pajisjes celulare
  foto_kamera = st.camera_input("Bëj foto të faturës")

  if foto_kamera is not None:
    st.success("Fotografia u mor me sukses!")

    f_skan = st.selectbox(
        "Zgjidh Furnitorin e kësaj fature:",
        sorted(st.session_state.db["Furnitori"].unique()),
        key="fs",
    )
    df_s = st.session_state.db[st.session_state.db["Furnitori"] == f_skan]
    a_skan = st.selectbox("Zgjidh Artikullin:", df_s["Artikulli"], key="as")
    r_s = df_s[df_s["Artikulli"] == a_skan].iloc[0]

    c_fakt = st.number_input(
        "Fut çmimin total në faturë (€):",
        min_value=0.0,
        value=float(r_s["Cmimi_Kaluar"]),
        step=0.05,
    )

    if st.button("Verifiko Çmimin e Skanuar"):
      c_nje = c_fakt / r_s["Sasia"] if r_s["Sasia"] > 0 else c_fakt
      dif = c_nje - r_s["Cmimi_Kaluar"]
      st.metric(
          label="Çmimi i Skanuar për Njësi",
          value=f"{c_nje:.3f} €",
          delta=f"{dif:+.3f} €",
      )
      if dif > 0:
        st.warning("⚠️ Çmimi në faturën e skanuar është RITUR!")
      else:
        st.success("✅ Çmimi është në rregull ose më i lirë.")

elif opsioni == "📋 Tabela e Inventarit":
  st.subheader("📋 Tabela e Produkteve & Çmimeve")
  st.dataframe(st.session_state.db, use_container_width=True)
