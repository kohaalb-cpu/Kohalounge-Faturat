import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Koha Lounge - Kontrolli i Faturave", layout="centered"
)

st.title("🍹 Koha Lounge - Kontrolli i Faturave & Çmimeve")
st.write(
    "Menaxho çmimet e furnitorëve dhe kontrollo luhatjet direkt nga telefoni."
)

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Koha Lounge - Kontrolli i Faturave", layout="centered"
)

st.title("🍹 Koha Lounge - Skanimi & Kontrolli i Faturave")
st.write(
    "Menaxho çmimet e furnitorëve, kontrollo luhatjet dhe skano faturat direkt"
    " nga telefoni."
)

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Koha Lounge - Kontrolli i Faturave", layout="centered"
)

st.title("🍹 Koha Lounge - Skanimi & Menaxhimi i Furnitorëve")
st.write(
    "Zgjidh furnitorin, skano faturën me kamerë dhe kontrollo çmimet në kohë"
    " reale."
)

# Baza e të dhënave me 54 artikujt e verifikuar dhe furnitorët e tyre
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
          "Kategoria": "Mish/Ushqim i ngrirë",
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
          "Furnitori": "Dauti - Komerc",
          "Artikulli": "Vaj lule dielli",
          "Kategoria": "Ushqimore",
          "Njesia": "Litër",
          "Sasia": 1.0,
          "Cmimi_Kaluar": 1.52,
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
          "Furnitori": "N.T.P. 1Maji-X",
          "Artikulli": "Fanta Orange 0.25L",
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
          "Furnitori": "Dinamika Sh.p.k.",
          "Artikulli": "Përshutë",
          "Kategoria": "Kuzhinë",
          "Njesia": "Kg",
          "Sasia": 1.0,
          "Cmimi_Kaluar": 10.00,
      },
      {
          "Furnitori": "Salespoint G&S",
          "Artikulli": "Palloma katrore",
          "Kategoria": "Sanitative",
          "Njesia": "Copë",
          "Sasia": 10.0,
          "Cmimi_Kaluar": 0.92,
      },
      {
          "Furnitori": "Salespoint G&S",
          "Artikulli": "Rollne WC",
          "Kategoria": "Sanitative",
          "Njesia": "Copë",
          "Sasia": 20.0,
          "Cmimi_Kaluar": 1.06,
      },
      {
          "Furnitori": "LB Group",
          "Artikulli": "Set thikë luge pirunë",
          "Kategoria": "Aksesorë",
          "Njesia": "Copë",
          "Sasia": 1.0,
          "Cmimi_Kaluar": 0.095,
      },
      {
          "Furnitori": "Dioren Sh.p.k.",
          "Artikulli": "Produkt i Dioren",
          "Kategoria": "Ushqimore",
          "Njesia": "Copë",
          "Sasia": 1.0,
          "Cmimi_Kaluar": 2.60,
      },
  ])

# Menyja anësore e aplikacionit
menu = st.sidebar.selectbox(
    "Zgjidh Opsionin",
    [
        "📦 Kontrollo Faturën sipas Furnitorit",
        "📸 Skano Faturën (Kamera / Foto)",
        "📋 Tabela e Plotë e Inventarit",
    ],
)

if menu == "📦 Kontrollo Faturën sipas Furnitorit":
  st.subheader("🏢 Zgjidh Furnitorin dhe Produktet")

  # Marrja e listës së furnitorëve
  furnitoret = sorted(st.session_state.db["Furnitori"].unique())
  zgjidh_furnitor = st.selectbox(
      "Zgjidh Furnitorin që ka sjellë mallin:", furnitoret
  )

  # Filtrimi i produkteve për këtë furnitor
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
        "Fut çmimin total të faturës për këtë paketë/artikull (€):",
        min_value=0.0,
        value=float(row["Cmimi_Kaluar"]),
        step=0.05,
    )

    if st.button("Llogarit dhe Krahaso Çmimin"):
      cmim_per_njesi = (
          cmim_fature / row["Sasia"] if row["Sasia"] > 0 else cmim_fature
      )
      diferenca = cmim_per_njesi - row["Cmimi_Kaluar"]
      pind = (
          (diferenca / row["Cmimi_Kaluar"]) * 100
          if row["Cmimi_Kaluar"] > 0
          else 0
      )

        st.metric(
            label="Çmimi i Ri për Njësi",
            value=f"{cmimi_per_cope:.2f} €",
            delta=f"{diferenca:.2f} €",
            delta_color="inverse")

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

elif menu == "📸 Skano Faturën (Kamera / Foto)":
  st.subheader("📸 Skano ose Ngarko Faturën e Furnitorit")
  st.write(
      "Bëj foto të faturës me kamerën e telefonit direkt nga shfletuesi ose"
      " ngarko një foto ekzistuese për verifikim."
  )

  uploaded_file = st.file_uploader(
      "Fotografo ose ngarko faturën", type=["jpg", "jpeg", "png"]
  )

  if uploaded_file is not None:
    st.image(
        uploaded_file, caption="Fatura e skanuar / ngarkuar", use_container_width=True
    )
    st.success(
        "Fatura u mor me sukses! Tani zgjidh furnitorin dhe artikullin për të"
        " konfirmuar çmimin:"
    )

    furn_skan = st.selectbox(
        "Zgjidh Furnitorin e Faturës:",
        sorted(st.session_state.db["Furnitori"].unique()),
        key="fs",
    )
    df_s = st.session_state.db[st.session_state.db["Furnitori"] == furn_skan]
    art_skan = st.selectbox("Zgjidh Artikullin:", df_s["Artikulli"], key="as")
    row_s = df_s[df_s["Artikulli"] == art_skan].iloc[0]

    cmim_skanuar = st.number_input(
        "Fut çmimin e lexuar nga fatura (€):",
        min_value=0.0,
        value=float(row_s["Cmimi_Kaluar"]),
        step=0.05,
    )

    if st.button("Verifiko Faturën e Skanuar"):
      c_njesi = (
          cmim_skanuar / row_s["Sasia"] if row_s["Sasia"] > 0 else cmim_skanuar
      )
      dif = c_njesi - row_s["Cmimi_Kaluar"]
      st.metric(
          label="Çmimi i Skanuar për Njësi",
          value=f"{c_njesi:.3f} €",
          delta=f"{dif:+.3f} €",
          delta_inverse=True,
      )
      if dif > 0:
        st.warning("⚠️ Çmimi në faturën e skanuar është RITUR!")
      else:
        st.success("✅ Çmimi është në rregull ose më i lirë.")

elif menu == "📋 Tabela e Plotë e Inventarit":
  st.subheader("📋 Tabela e Produkteve & Çmimeve")
  st.dataframe(st.session_state.db, use_container_width=True)
