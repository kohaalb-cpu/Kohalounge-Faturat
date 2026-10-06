import pandas as pd
import streamlit as st

st.set_page_config(
	page_title="Koha Lounge - Kontrolli i Faturave", layout="centered"
)

st.title("🍹 Koha Lounge - Kontrolli i Faturave & Çmimeve")
st.write("Menaxho çmimet e furnitorëve dhe kontrollo luhatjet nga telefoni.")

if "db" not in st.session_state:
	st.session_state.db = pd.DataFrame(
		{
			"Kodi": ["001", "002", "003"],
			"Artikulli": ["Kafe Espresso", "Coca Cola 0.33L", "Djath i Bardhë"],
			"Paketimi": ["Pako", "Arkë", "KG"],
			"Sasia": [10, 24, 1],
			"Cmimi_Kaluar": [1.40, 0.75, 6.80],
			"Cmimi_Konkurrences": [1.35, 0.72, 6.40],
		}
	)

menu = st.sidebar.selectbox(
	"Zgjidh Opsionin",
	["Pranimi i Faturës (Sot)", "Krahasimi i Konkurrencës / Ofertat e Reja"],
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
		f"**Paketimi standard:** {row['Paketimi']} ( {row['Sasia']} copë ) |"
		f" **Çmimi i kaluar për copë:** {row['Cmimi_Kaluar']} €"
	)

	cmimi_fatures_pakete = st.number_input(
		"Fut çmimin total të faturës për këtë paketë (€):",
		min_value=0.0,
		value=15.0,
		step=0.1,
	)

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
			delta=f"{diferenca:+.2f} € ({pind:+.1f}%)",
			delta_inverse=True,
		)

		if diferenca > 0:
			st.error("⚠️ KUJDES: Çmimi është rritur krahasuar me blerjen e fundit!")
		elif diferenca < 0:
			st.success("🎉 KURSIM: Çmimi ka rënë krahasuar me herën e kaluar!")
		else:
			st.info("ℹ️ Çmimi ka mbetur i pandryshuar.")

elif menu == "Krahasimi i Konkurrencës / Ofertat e Reja":
	st.subheader("🔍 Tabela e Çmimeve & Tregut")
	st.dataframe(st.session_state.db, use_container_width=True)

	st.markdown("---")
	st.subheader("➕ Shto Produkt ose Ofertë nga Furnitor i Ri")

	with st.form("formë_oferta"):
		art_ri = st.text_input("Emri i Artikullit të Ri")
		pak_ri = st.text_input("Lloji i Paketimit (p.sh. Pako, Arkë, KG)")
		sasi_ri = st.number_input("Sasia në Paketim", min_value=1, value=1)
		cmim_paketa = st.number_input(
			"Çmimi total i paketës (€)", min_value=0.0, value=10.0
		)
		submit = st.form_submit_button("Ruaj Ofertën")

		if submit and art_ri:
			cmim_cope_ri = cmim_paketa / sasi_ri
			new_row = pd.DataFrame(
				{
					"Kodi": [str(len(st.session_state.db) + 1)],
					"Artikulli": [art_ri],
					"Paketimi": [pak_ri],
					"Sasia": [sasi_ri],
					"Cmimi_Kaluar": [cmim_cope_ri],
					"Cmimi_Konkurrences": [cmim_cope_ri],
				}
			)
			st.session_state.db = pd.concat(
				[st.session_state.db, new_row], ignore_index=True
			)
			st.success(
				f"U shtua me sukses produkti: {art_ri} ({cmim_cope_ri:.2f} €/copë)"
			)
