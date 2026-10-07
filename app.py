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

# Lista e inventarit (109 produkte)
if "db" not in st.session_state:
  st.session_state.db = pd.DataFrame([
      {
          "Kodi": "1",
          "Artikulli": "Qumësht",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 12.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 8.0,
          "Cmimi_Konkurrences": 7.8,
      },
      {
          "Kodi": "2",
          "Artikulli": "Coca Cola 0.25l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 12.5,
          "Cmimi_Konkurrences": 12.2,
      },
      {
          "Kodi": "3",
          "Artikulli": "Fanta Orange 0.25L",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 12.5,
          "Cmimi_Konkurrences": 12.2,
      },
      {
          "Kodi": "4",
          "Artikulli": "Sprite 0.25l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 12.5,
          "Cmimi_Konkurrences": 12.2,
      },
      {
          "Kodi": "5",
          "Artikulli": "Schweps 0.25 l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 13.5,
          "Cmimi_Konkurrences": 13.0,
      },
      {
          "Kodi": "6",
          "Artikulli": "Coca Cola Zero 0.25 l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 12.5,
          "Cmimi_Konkurrences": 12.2,
      },
      {
          "Kodi": "7",
          "Artikulli": "Coca Cola 0.33l Kanaqe",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI-X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 11.5,
          "Cmimi_Konkurrences": 11.2,
      },
      {
          "Kodi": "8",
          "Artikulli": "Bravo Orange 0.20 l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 16.5,
          "Cmimi_Konkurrences": 16.0,
      },
      {
          "Kodi": "9",
          "Artikulli": "Bravo Vishnje 0.20 l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 16.5,
          "Cmimi_Konkurrences": 16.0,
      },
      {
          "Kodi": "10",
          "Artikulli": "Bravo Dredhez 0.20 l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 16.5,
          "Cmimi_Konkurrences": 16.0,
      },
      {
          "Kodi": "11",
          "Artikulli": "Bravo Pjeshkë 0.20 l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 16.5,
          "Cmimi_Konkurrences": 16.0,
      },
      {
          "Kodi": "12",
          "Artikulli": "Bravo Mollë 0.20 l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI-X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 16.5,
          "Cmimi_Konkurrences": 16.0,
      },
      {
          "Kodi": "13",
          "Artikulli": "Ujë Natyral Dea 0.50 l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 12.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 2.05,
          "Cmimi_Konkurrences": 2.0,
      },
      {
          "Kodi": "14",
          "Artikulli": "Ujë Mineral Dea 0.50 l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 12.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 2.15,
          "Cmimi_Konkurrences": 2.1,
      },
      {
          "Kodi": "15",
          "Artikulli": "Llashko 0.25 l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 17.5,
          "Cmimi_Konkurrences": 17.0,
      },
      {
          "Kodi": "16",
          "Artikulli": "Birra Peja 0.33",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 15.0,
          "Cmimi_Konkurrences": 14.5,
      },
      {
          "Kodi": "17",
          "Artikulli": "Heineken 0.25 l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 22.8,
          "Cmimi_Konkurrences": 22.0,
      },
      {
          "Kodi": "18",
          "Artikulli": "Smirnoff Ice 0.25 l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI -X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 29.0,
          "Cmimi_Konkurrences": 28.0,
      },
      {
          "Kodi": "19",
          "Artikulli": "FroseTea",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI-X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 9.6,
          "Cmimi_Konkurrences": 9.3,
      },
      {
          "Kodi": "20",
          "Artikulli": "Redbull 0.25 l",
          "Kategoria": "BANAK",
          "Furnitori": "1 MAJI-X",
          "Sasia": 24.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 25.0,
          "Cmimi_Konkurrences": 24.5,
      },
      {
          "Kodi": "21",
          "Artikulli": "Lemonade 10 L",
          "Kategoria": "BANAK",
          "Furnitori": "FER GROUP",
          "Sasia": 10.0,
          "Njesia": "LITER",
          "Cmimi_Kaluar": 6.0,
          "Cmimi_Konkurrences": 5.8,
      },
      {
          "Kodi": "22",
          "Artikulli": "Boronice 10 L",
          "Kategoria": "BANAK",
          "Furnitori": "FER GROUP",
          "Sasia": 10.0,
          "Njesia": "LITER",
          "Cmimi_Kaluar": 6.0,
          "Cmimi_Konkurrences": 5.8,
      },
      {
          "Kodi": "23",
          "Artikulli": "Pavin Caffe",
          "Kategoria": "BANAK",
          "Furnitori": "PAVIN CAFFE",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 22.0,
          "Cmimi_Konkurrences": 21.5,
      },
      {
          "Kodi": "24",
          "Artikulli": "Nes Caffe",
          "Kategoria": "BANAK",
          "Furnitori": "DOLCEZZA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 12.0,
          "Cmimi_Konkurrences": 11.5,
      },
      {
          "Kodi": "25",
          "Artikulli": "Nes Quick",
          "Kategoria": "BANAK",
          "Furnitori": "DOLCEZZA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 12.0,
          "Cmimi_Konkurrences": 11.5,
      },
      {
          "Kodi": "26",
          "Artikulli": "Akullore",
          "Kategoria": "BANAK",
          "Furnitori": "MAGICE ICE",
          "Sasia": 1.0,
          "Njesia": "KASETE",
          "Cmimi_Kaluar": 12.1,
          "Cmimi_Konkurrences": 11.8,
      },
      {
          "Kodi": "27",
          "Artikulli": "Hot Chocolate",
          "Kategoria": "BANAK",
          "Furnitori": "DOLCEZZA",
          "Sasia": 1.0,
          "Njesia": "COPA",
          "Cmimi_Kaluar": 0.37,
          "Cmimi_Konkurrences": 0.35,
      },
      {
          "Kodi": "28",
          "Artikulli": "Kafe Turke",
          "Kategoria": "BANAK",
          "Furnitori": "VIVA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 0.0,
          "Cmimi_Konkurrences": 0.0,
      },
      {
          "Kodi": "29",
          "Artikulli": "Sheqer Kafe",
          "Kategoria": "BANAK",
          "Furnitori": "DUGI",
          "Sasia": 1.0,
          "Njesia": "PAKO",
          "Cmimi_Kaluar": 11.0,
          "Cmimi_Konkurrences": 10.5,
      },
      {
          "Kodi": "30",
          "Artikulli": "Lugë për Makiato",
          "Kategoria": "BANAK",
          "Furnitori": "DUGI",
          "Sasia": 1.0,
          "Njesia": "PAKO",
          "Cmimi_Kaluar": 8.0,
          "Cmimi_Konkurrences": 7.8,
      },
      {
          "Kodi": "31",
          "Artikulli": "Qaj Frutash",
          "Kategoria": "BANAK",
          "Furnitori": "KOSMONTE",
          "Sasia": 20.0,
          "Njesia": "PAKO",
          "Cmimi_Kaluar": 1.12,
          "Cmimi_Konkurrences": 1.1,
      },
      {
          "Kodi": "32",
          "Artikulli": "Qaj Mentë",
          "Kategoria": "BANAK",
          "Furnitori": "KOSMONTE",
          "Sasia": 20.0,
          "Njesia": "PAKO",
          "Cmimi_Kaluar": 1.12,
          "Cmimi_Konkurrences": 1.1,
      },
      {
          "Kodi": "33",
          "Artikulli": "Qaj Kamomil",
          "Kategoria": "BANAK",
          "Furnitori": "KOSMONTE",
          "Sasia": 20.0,
          "Njesia": "PAKO",
          "Cmimi_Kaluar": 1.12,
          "Cmimi_Konkurrences": 1.1,
      },
      {
          "Kodi": "34",
          "Artikulli": "Qaj Gjelbërt",
          "Kategoria": "BANAK",
          "Furnitori": "KOSMONTE",
          "Sasia": 20.0,
          "Njesia": "PAKO",
          "Cmimi_Kaluar": 1.12,
          "Cmimi_Konkurrences": 1.1,
      },
      {
          "Kodi": "35",
          "Artikulli": "Qaj Brusnicë",
          "Kategoria": "BANAK",
          "Furnitori": "KOSMONTE",
          "Sasia": 20.0,
          "Njesia": "PAKO",
          "Cmimi_Kaluar": 1.17,
          "Cmimi_Konkurrences": 1.15,
      },
      {
          "Kodi": "36",
          "Artikulli": "Qaj I zi",
          "Kategoria": "BANAK",
          "Furnitori": "KOSMONTE",
          "Sasia": 20.0,
          "Njesia": "PAKO",
          "Cmimi_Kaluar": 1.12,
          "Cmimi_Konkurrences": 1.1,
      },
      {
          "Kodi": "37",
          "Artikulli": "Bukë Hamburgeri",
          "Kategoria": "KUZHINE",
          "Furnitori": "FURRA PASHTRIKU",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.15,
          "Cmimi_Konkurrences": 0.14,
      },
      {
          "Kodi": "38",
          "Artikulli": "Bukë Tosti",
          "Kategoria": "KUZHINE",
          "Furnitori": "FURRA PASHTRIKU",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.15,
          "Cmimi_Konkurrences": 0.14,
      },
      {
          "Kodi": "39",
          "Artikulli": "Bukë Rriska",
          "Kategoria": "KUZHINE",
          "Furnitori": "FURRA PASHTRIKU",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.55,
          "Cmimi_Konkurrences": 0.53,
      },
      {
          "Kodi": "40",
          "Artikulli": "KOS 10 KG",
          "Kategoria": "KUZHINE",
          "Furnitori": "MAGICE ICE",
          "Sasia": 10.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 12.569,
          "Cmimi_Konkurrences": 12.0,
      },
      {
          "Kodi": "41",
          "Artikulli": "DJATH",
          "Kategoria": "KUZHINE",
          "Furnitori": "MAGICE ICE",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 6.254,
          "Cmimi_Konkurrences": 6.0,
      },
      {
          "Kodi": "42",
          "Artikulli": "Gjizë",
          "Kategoria": "KUZHINE",
          "Furnitori": "MAGICE ICE",
          "Sasia": 700.0,
          "Njesia": "GR",
          "Cmimi_Kaluar": 1.754,
          "Cmimi_Konkurrences": 1.7,
      },
      {
          "Kodi": "43",
          "Artikulli": "MUSKUJ",
          "Kategoria": "KUZHINE",
          "Furnitori": "GAZI - COM",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 11.0,
          "Cmimi_Konkurrences": 10.5,
      },
      {
          "Kodi": "44",
          "Artikulli": "MISH TUL ( PLEQKE)",
          "Kategoria": "KUZHINE",
          "Furnitori": "GAZI - COM",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 11.0,
          "Cmimi_Konkurrences": 10.5,
      },
      {
          "Kodi": "45",
          "Artikulli": "MISH I BLUAR",
          "Kategoria": "KUZHINE",
          "Furnitori": "GAZI - COM",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 9.5,
          "Cmimi_Konkurrences": 9.2,
      },
      {
          "Kodi": "46",
          "Artikulli": "MEDALION",
          "Kategoria": "KUZHINE",
          "Furnitori": "GAZI - COM",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 11.0,
          "Cmimi_Konkurrences": 10.5,
      },
      {
          "Kodi": "47",
          "Artikulli": "PLESKAVICE BIO",
          "Kategoria": "KUZHINE",
          "Furnitori": "GAZI - COM",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 8.0,
          "Cmimi_Konkurrences": 7.8,
      },
      {
          "Kodi": "48",
          "Artikulli": "QOFTE",
          "Kategoria": "KUZHINE",
          "Furnitori": "GAZI - COM",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 6.0,
          "Cmimi_Konkurrences": 5.8,
      },
      {
          "Kodi": "49",
          "Artikulli": "VIRSHLLE",
          "Kategoria": "KUZHINE",
          "Furnitori": "GAZI - COM",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 7.0,
          "Cmimi_Konkurrences": 6.8,
      },
      {
          "Kodi": "50",
          "Artikulli": "BRUM I PLESKAVICES",
          "Kategoria": "KUZHINE",
          "Furnitori": "GAZI - COM",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 6.0,
          "Cmimi_Konkurrences": 5.8,
      },
      {
          "Kodi": "51",
          "Artikulli": "DOMATE",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 1.7,
          "Cmimi_Konkurrences": 1.6,
      },
      {
          "Kodi": "52",
          "Artikulli": "TRANGUJ",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 1.7,
          "Cmimi_Konkurrences": 1.6,
      },
      {
          "Kodi": "53",
          "Artikulli": "QEP",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 0.0,
          "Cmimi_Konkurrences": 0.0,
      },
      {
          "Kodi": "54",
          "Artikulli": "KARROTA",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 0.0,
          "Cmimi_Konkurrences": 0.0,
      },
      {
          "Kodi": "55",
          "Artikulli": "SPEC DJEGES",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 2.0,
          "Cmimi_Konkurrences": 1.9,
      },
      {
          "Kodi": "56",
          "Artikulli": "SPEC PA DJEGES",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 1.4,
          "Cmimi_Konkurrences": 1.35,
      },
      {
          "Kodi": "57",
          "Artikulli": "SPEC I KUQ",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 2.2,
          "Cmimi_Konkurrences": 2.1,
      },
      {
          "Kodi": "58",
          "Artikulli": "LAKER E BARDH",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 0.3,
          "Cmimi_Konkurrences": 0.28,
      },
      {
          "Kodi": "59",
          "Artikulli": "LAKER E KUQE",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 0.74,
          "Cmimi_Konkurrences": 0.7,
      },
      {
          "Kodi": "60",
          "Artikulli": "DOMATINA",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 2.5,
          "Cmimi_Konkurrences": 2.4,
      },
      {
          "Kodi": "61",
          "Artikulli": "PATATE",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 0.0,
          "Cmimi_Konkurrences": 0.0,
      },
      {
          "Kodi": "62",
          "Artikulli": "QEP E KUQE",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 0.0,
          "Cmimi_Konkurrences": 0.0,
      },
      {
          "Kodi": "63",
          "Artikulli": "MAGDANOZ",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "TUBE",
          "Cmimi_Kaluar": 2.5,
          "Cmimi_Konkurrences": 2.4,
      },
      {
          "Kodi": "64",
          "Artikulli": "MARULL",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 15.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.53,
          "Cmimi_Konkurrences": 0.5,
      },
      {
          "Kodi": "65",
          "Artikulli": "LIMON",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 1.8,
          "Cmimi_Konkurrences": 1.7,
      },
      {
          "Kodi": "66",
          "Artikulli": "RUKOLLA",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 1.5,
          "Cmimi_Konkurrences": 1.4,
      },
      {
          "Kodi": "67",
          "Artikulli": "PURRI",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "TUBE",
          "Cmimi_Kaluar": 1.0,
          "Cmimi_Konkurrences": 0.95,
      },
      {
          "Kodi": "68",
          "Artikulli": "DOMATE E ZEZE",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 2.6,
          "Cmimi_Konkurrences": 2.5,
      },
      {
          "Kodi": "69",
          "Artikulli": "KUNGULLESHE",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 0.0,
          "Cmimi_Konkurrences": 0.0,
      },
      {
          "Kodi": "70",
          "Artikulli": "MIELL MISRI",
          "Kategoria": "KUZHINE",
          "Furnitori": "BEKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 0.0,
          "Cmimi_Konkurrences": 0.0,
      },
      {
          "Kodi": "71",
          "Artikulli": "KEPURDHA",
          "Kategoria": "KUZHINE",
          "Furnitori": "GREEN GROUP",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 3.0,
          "Cmimi_Konkurrences": 2.9,
      },
      {
          "Kodi": "72",
          "Artikulli": "KAQKAVALL EDAMER",
          "Kategoria": "KUZHINE",
          "Furnitori": "KOSMONTE",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 4.9,
          "Cmimi_Konkurrences": 4.7,
      },
      {
          "Kodi": "73",
          "Artikulli": "CHEESE BURGER",
          "Kategoria": "KUZHINE",
          "Furnitori": "KOSMONTE",
          "Sasia": 10.0,
          "Njesia": "KOMPLET",
          "Cmimi_Kaluar": 1.1,
          "Cmimi_Konkurrences": 1.05,
      },
      {
          "Kodi": "74",
          "Artikulli": "AJVAR",
          "Kategoria": "KUZHINE",
          "Furnitori": "KOSMONTE",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 2.9,
          "Cmimi_Konkurrences": 2.8,
      },
      {
          "Kodi": "75",
          "Artikulli": "ORIZ SCOTTI",
          "Kategoria": "KUZHINE",
          "Furnitori": "VIVA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 1.79,
          "Cmimi_Konkurrences": 1.7,
      },
      {
          "Kodi": "76",
          "Artikulli": "POMFRIT",
          "Kategoria": "KUZHINE",
          "Furnitori": "KOSMONTE",
          "Sasia": 2.5,
          "Njesia": "KG",
          "Cmimi_Kaluar": 3.72,
          "Cmimi_Konkurrences": 3.6,
      },
      {
          "Kodi": "77",
          "Artikulli": "ROLLNE FISKALI",
          "Kategoria": "BANAK",
          "Furnitori": "ITECH STORE",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.45,
          "Cmimi_Konkurrences": 0.43,
      },
      {
          "Kodi": "78",
          "Artikulli": "DOREZA PER KUZHINE",
          "Kategoria": "KUZHINE",
          "Furnitori": "KOSLABOR",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 3.2,
          "Cmimi_Konkurrences": 3.0,
      },
      {
          "Kodi": "79",
          "Artikulli": "SUXHUK",
          "Kategoria": "KUZHINE",
          "Furnitori": "DINAMIKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 7.8,
          "Cmimi_Konkurrences": 7.5,
      },
      {
          "Kodi": "80",
          "Artikulli": "PERSHUTE",
          "Kategoria": "KUZHINE",
          "Furnitori": "DINAMIKA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 10.0,
          "Cmimi_Konkurrences": 9.5,
      },
      {
          "Kodi": "81",
          "Artikulli": "KRIP",
          "Kategoria": "KUZHINE",
          "Furnitori": "DAUTI KOMERC",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 0.456,
          "Cmimi_Konkurrences": 0.44,
      },
      {
          "Kodi": "82",
          "Artikulli": "UTHULL E BARDH",
          "Kategoria": "KUZHINE",
          "Furnitori": "DAUTI KOMERC",
          "Sasia": 1.0,
          "Njesia": "LITER",
          "Cmimi_Kaluar": 0.59,
          "Cmimi_Konkurrences": 0.55,
      },
      {
          "Kodi": "83",
          "Artikulli": "VAJ LULE DIELLI",
          "Kategoria": "KUZHINE",
          "Furnitori": "DAUTI KOMERC",
          "Sasia": 1.0,
          "Njesia": "LITER",
          "Cmimi_Kaluar": 1.52,
          "Cmimi_Konkurrences": 1.45,
      },
      {
          "Kodi": "84",
          "Artikulli": "LAZANJE",
          "Kategoria": "KUZHINE",
          "Furnitori": "DAUTI KOMERC",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 1.75,
          "Cmimi_Konkurrences": 1.7,
      },
      {
          "Kodi": "85",
          "Artikulli": "TRANGUJ TURSHI",
          "Kategoria": "KUZHINE",
          "Furnitori": "DAUTI KOMERC",
          "Sasia": 2.5,
          "Njesia": "KG",
          "Cmimi_Kaluar": 3.3,
          "Cmimi_Konkurrences": 3.2,
      },
      {
          "Kodi": "86",
          "Artikulli": "DIGO FARE BUKE",
          "Kategoria": "KUZHINE",
          "Furnitori": "DAUTI KOMERC",
          "Sasia": 500.0,
          "Njesia": "GR",
          "Cmimi_Kaluar": 3.95,
          "Cmimi_Konkurrences": 3.8,
      },
      {
          "Kodi": "87",
          "Artikulli": "GJYVEQ",
          "Kategoria": "KUZHINE",
          "Furnitori": "DAUTI KOMERC",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 1.53,
          "Cmimi_Konkurrences": 1.48,
      },
      {
          "Kodi": "88",
          "Artikulli": "MIELL PER BUKE",
          "Kategoria": "KUZHINE",
          "Furnitori": "DAUTI KOMERC",
          "Sasia": 25.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 15.5,
          "Cmimi_Konkurrences": 15.0,
      },
      {
          "Kodi": "89",
          "Artikulli": "MIELL PER PIZZA",
          "Kategoria": "KUZHINE",
          "Furnitori": "DAUTI KOMERC",
          "Sasia": 24.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 19.5,
          "Cmimi_Konkurrences": 19.0,
      },
      {
          "Kodi": "90",
          "Artikulli": "MISER",
          "Kategoria": "KUZHINE",
          "Furnitori": "1 MAJI SH.P.K",
          "Sasia": 400.0,
          "Njesia": "GR",
          "Cmimi_Kaluar": 1.4,
          "Cmimi_Konkurrences": 1.35,
      },
      {
          "Kodi": "91",
          "Artikulli": "VEGET",
          "Kategoria": "KUZHINE",
          "Furnitori": "1 MAJI SH.P.K",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 2.5,
          "Cmimi_Konkurrences": 2.4,
      },
      {
          "Kodi": "92",
          "Artikulli": "HOPLA PER KUZHINE",
          "Kategoria": "KUZHINE",
          "Furnitori": "1 MAJI SH.P.K",
          "Sasia": 1.0,
          "Njesia": "LITER",
          "Cmimi_Kaluar": 2.0,
          "Cmimi_Konkurrences": 1.9,
      },
      {
          "Kodi": "93",
          "Artikulli": "LINGUINI",
          "Kategoria": "KUZHINE",
          "Furnitori": "1 MAJI SH.P.K",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 2.5,
          "Cmimi_Konkurrences": 2.4,
      },
      {
          "Kodi": "94",
          "Artikulli": "KETCJHUP STICK",
          "Kategoria": "KUZHINE",
          "Furnitori": "1 MAJI SH.P.K",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.05,
          "Cmimi_Konkurrences": 0.04,
      },
      {
          "Kodi": "95",
          "Artikulli": "MAJONEZ STICK",
          "Kategoria": "KUZHINE",
          "Furnitori": "1 MAJI SH.P.K",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.05,
          "Cmimi_Konkurrences": 0.04,
      },
      {
          "Kodi": "96",
          "Artikulli": "PALLOMA KATRORE",
          "Kategoria": "KUZHINE",
          "Furnitori": "SALESPOINT",
          "Sasia": 10.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.92,
          "Cmimi_Konkurrences": 0.9,
      },
      {
          "Kodi": "97",
          "Artikulli": "ROLLNE WC",
          "Kategoria": "KUZHINE",
          "Furnitori": "SALESPOINT",
          "Sasia": 20.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 1.06,
          "Cmimi_Konkurrences": 1.0,
      },
      {
          "Kodi": "98",
          "Artikulli": "ULLINJE",
          "Kategoria": "KUZHINE",
          "Furnitori": "DOLCEZZA",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 2.712,
          "Cmimi_Konkurrences": 2.6,
      },
      {
          "Kodi": "99",
          "Artikulli": "SET THIKE LUGE PIRUNE",
          "Kategoria": "KUZHINE",
          "Furnitori": "LB GROUP",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.095,
          "Cmimi_Konkurrences": 0.09,
      },
      {
          "Kodi": "100",
          "Artikulli": "GOTA PER AKULLORE",
          "Kategoria": "BANAK",
          "Furnitori": "LB GROUP",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.06,
          "Cmimi_Konkurrences": 0.055,
      },
      {
          "Kodi": "101",
          "Artikulli": "TASA TRANSPARENT",
          "Kategoria": "BANAK",
          "Furnitori": "LB GROUP",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.058,
          "Cmimi_Konkurrences": 0.055,
      },
      {
          "Kodi": "102",
          "Artikulli": "LUGE PER AKULLORE",
          "Kategoria": "BANAK",
          "Furnitori": "LB GROUP",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.024,
          "Cmimi_Konkurrences": 0.022,
      },
      {
          "Kodi": "103",
          "Artikulli": "FOLI ALUMINI",
          "Kategoria": "KUZHINE",
          "Furnitori": "LB GROUP",
          "Sasia": 1.0,
          "Njesia": "METER",
          "Cmimi_Kaluar": 0.49,
          "Cmimi_Konkurrences": 0.45,
      },
      {
          "Kodi": "104",
          "Artikulli": "PAKETIME PA NDARJE",
          "Kategoria": "KUZHINE",
          "Furnitori": "LB GROUP",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.1,
          "Cmimi_Konkurrences": 0.095,
      },
      {
          "Kodi": "105",
          "Artikulli": "DEMIGLACE",
          "Kategoria": "KUZHINE",
          "Furnitori": "EUROPA PRODUCT",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 1.472,
          "Cmimi_Konkurrences": 1.4,
      },
      {
          "Kodi": "106",
          "Artikulli": "HUDER E BLUAR",
          "Kategoria": "KUZHINE",
          "Furnitori": "EUROPA PRODUCT",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 33.8,
          "Cmimi_Konkurrences": 32.5,
      },
      {
          "Kodi": "107",
          "Artikulli": "BIBER I ZI I BLUAR",
          "Kategoria": "KUZHINE",
          "Furnitori": "EUROPA PRODUCT",
          "Sasia": 1.0,
          "Njesia": "KG",
          "Cmimi_Kaluar": 33.8,
          "Cmimi_Konkurrences": 32.5,
      },
      {
          "Kodi": "108",
          "Artikulli": "SHLLAG",
          "Kategoria": "BANAK",
          "Furnitori": "VIVA",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 1.76,
          "Cmimi_Konkurrences": 1.7,
      },
      {
          "Kodi": "109",
          "Artikulli": "MARGARINE",
          "Kategoria": "KUZHINE",
          "Furnitori": "VIVA",
          "Sasia": 1.0,
          "Njesia": "COPE",
          "Cmimi_Kaluar": 0.98,
          "Cmimi_Konkurrences": 0.94,
      },
  ])

menu = st.sidebar.selectbox(
    "Zgjidh Opsionin",
    [
        "Pranimi i Faturës (Sot)",
        "📸 Skano Faturën (Kamera)",
        "Krahasimi i Konkurrencës / Ofertat e Reja",
    ],
)

if menu == "Pranimi i Faturës (Sot)":
  st.subheader("📦 Regjistrimi i Faturës së Re")

  artikulli_zgjedhur = st.selectbox(
      "Zgjidh Artikullin:", st.session_state.db["Artikulli"]
  )
  row = st.session_state.db[
      st.session_state.db["Artikulli"] == artikulli_zgjedhur
  ].iloc[0]

  st.info(
      f"**Kategoria:** {row['Kategoria']} | **Furnitori:** {row['Furnitori']}\n\n"
      f"**Paketimi standard:** {row['Njesia']} (Sasia: {row['Sasia']}) |"
      f" **Çmimi i fundit:** {row['Cmimi_Kaluar']} €"
  )

  cmimi_fatures_pakete = st.number_input(
      "Fut çmimin total të faturës për këtë produkt (€):",
      min_value=0.0,
      value=float(row["Cmimi_Kaluar"]),
      step=0.1,
  )

  if st.button("Llogarit dhe Kontrollo Çmimin"):
    if row["Sasia"] > 0:
      cmimi_per_cope = cmimi_fatures_pakete / row["Sasia"]
    else:
      cmimi_per_cope = cmimi_fatures_pakete

    diferenca = cmimi_per_cope - row["Cmimi_Kaluar"]
    pind = (
        (diferenca / row["Cmimi_Kaluar"]) * 100
        if row["Cmimi_Kaluar"] > 0
        else 0
    )

    st.metric(
        label="Çmimi i Ri për Njësi/Copë",
        value=f"{cmimi_per_cope:.3f} €",
        delta=f"{diferenca:+.3f} € ({pind:+.1f}%)",
        delta_inverse=True,
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

elif menu == "📸 Skano Faturën (Kamera)":
  st.subheader("📸 Skano Faturën e Furnitorit")
  st.write(
      "Bëj një foto të faturës me kamerën e telefonit ose ngarko foton e"
      " faturës për verifikim të shpejtë."
  )

  uploaded_file = st.file_uploader(
      "Zgjidh ose bëj foto të faturës", type=["jpg", "jpeg", "png"]
  )

  if uploaded_file is not None:
    st.image(
        uploaded_file, caption="Fatura e ngarkuar", use_container_width=True
    )
    st.success(
        "Fatura u ngarkua me sukses! Zgjidhni artikullin më poshtë për të"
        " konfirmuar çmimin e skanuar:"
    )

    artikulli_skanim = st.selectbox(
        "Zgjidh artikullin përkatës nga fatura:",
        st.session_state.db["Artikulli"],
        key="skan_art",
    )
    row_skan = st.session_state.db[
        st.session_state.db["Artikulli"] == artikulli_skanim
    ].iloc[0]

    cmim_skanuar = st.number_input(
        "Fut çmimin e lexuar nga fatura (€):", min_value=0.0, value=10.0
    )

    if st.button("Verifiko Çmimin e Skanuar"):
      cm_cope_skan = (
          cmim_skanuar / row_skan["Sasia"] if row_skan["Sasia"] > 0 else cmim_skanuar
      )
      dif_skan = cm_cope_skan - row_skan["Cmimi_Kaluar"]
      st.metric(
          label="Çmimi i Skanuar për Njësi",
          value=f"{cm_cope_skan:.3f} €",
          delta=f"{dif_skan:+.3f} €",
          delta_inverse=True,
      )
      if dif_skan > 0:
        st.warning(
            "⚠️ Furnitori ka rritur çmimin për këtë artikull në faturën e"
            " sotme!"
        )
      else:
        st.success("✅ Çmimi është në rregull ose më i ulët se hera e kaluar.")

elif menu == "Krahasimi i Konkurrencës / Ofertat e Reja":
  st.subheader("🔍 Tabela e Inventarit & Çmimeve të Tregut")
  st.dataframe(st.session_state.db, use_container_width=True)

  st.markdown("---")
  st.subheader("➕ Shto Produkt ose Ofertë nga Furnitor i Ri")

  with st.form("formë_oferta"):
    art_ri = st.text_input("Emri i Artikullit të Ri")
    kat_ri = st.selectbox("Kategoria", ["BANAK", "KUZHINE"])
    furn_ri = st.text_input("Emri i Furnitorit")
    pak_ri = st.text_input("Lloji i Njësisë (p.sh. KOMPLET, KG, COPE)")
    sasi_ri = st.number_input("Sasia në Paketim", min_value=0.1, value=1.0)
    cmim_paketa = st.number_input(
        "Çmimi total (€)", min_value=0.0, value=10.0
    )
    submit = st.form_submit_button("Ruaj Ofertën")

    if submit and art_ri:
      new_row = pd.DataFrame({
          "Kodi": [str(len(st.session_state.db) + 1)],
          "Artikulli": [art_ri],
          "Kategoria": [kat_ri],
          "Furnitori": [furn_ri],
          "Sasia": [sasi_ri],
          "Njesia": [pak_ri],
          "Cmimi_Kaluar": [cmim_paketa],
          "Cmimi_Konkurrences": [cmim_paketa * 0.98],
      })
      st.session_state.db = pd.concat(
          [st.session_state.db, new_row], ignore_index=True
      )
      st.success(f"U shtua me sukses produkti: {art_ri}!")