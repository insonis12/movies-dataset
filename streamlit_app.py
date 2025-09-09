import streamlit as st
import pandas as pd

# Dane budynków
budynki = [
    {"Nazwa": "Ratusz", "MaxPoziom": 30, "MinPoziom": 1, "Drewno": 90, "Glina": 80, "Zelazo": 70, "Populacja": 5, "CzynnikDrewna": 1.26, "CzynnikGliny": 1.275, "CzynnikZelaza": 1.26, "CzynnikPopulacji": 1.17},
    {"Nazwa": "Koszary", "MaxPoziom": 25, "MinPoziom": 0, "Drewno": 200, "Glina": 170, "Zelazo": 90, "Populacja": 7, "CzynnikDrewna": 1.26, "CzynnikGliny": 1.28, "CzynnikZelaza": 1.26, "CzynnikPopulacji": 1.17},
    {"Nazwa": "Stajnia", "MaxPoziom": 20, "MinPoziom": 0, "Drewno": 270, "Glina": 240, "Zelazo": 260, "Populacja": 8, "CzynnikDrewna": 1.26, "CzynnikGliny": 1.28, "CzynnikZelaza": 1.26, "CzynnikPopulacji": 1.17},
    {"Nazwa": "Warsztat", "MaxPoziom": 15, "MinPoziom": 0, "Drewno": 300, "Glina": 240, "Zelazo": 260, "Populacja": 8, "CzynnikDrewna": 1.26, "CzynnikGliny": 1.28, "CzynnikZelaza": 1.26, "CzynnikPopulacji": 1.17},
    {"Nazwa": "Pałac", "MaxPoziom": 1, "MinPoziom": 0, "Drewno": 15000, "Glina": 25000, "Zelazo": 10000, "Populacja": 80, "CzynnikDrewna": 2, "CzynnikGliny": 2, "CzynnikZelaza": 2, "CzynnikPopulacji": 1.17},
    {"Nazwa": "Kuźnia", "MaxPoziom": 20, "MinPoziom": 0, "Drewno": 220, "Glina": 180, "Zelazo": 240, "Populacja": 20, "CzynnikDrewna": 1.26, "CzynnikGliny": 1.275, "CzynnikZelaza": 1.26, "CzynnikPopulacji": 1.17},
    {"Nazwa": "Plac", "MaxPoziom": 1, "MinPoziom": 0, "Drewno": 10, "Glina": 40, "Zelazo": 30, "Populacja": 0, "CzynnikDrewna": 1.26, "CzynnikGliny": 1.275, "CzynnikZelaza": 1.26, "CzynnikPopulacji": 1.17},
    {"Nazwa": "Piedestał", "MaxPoziom": 1, "MinPoziom": 0, "Drewno": 220, "Glina": 220, "Zelazo": 220, "Populacja": 10, "CzynnikDrewna": 1.26, "CzynnikGliny": 1.275, "CzynnikZelaza": 1.26, "CzynnikPopulacji": 1.17},
    {"Nazwa": "Rynek", "MaxPoziom": 25, "MinPoziom": 0, "Drewno": 100, "Glina": 100, "Zelazo": 100, "Populacja": 20, "CzynnikDrewna": 1.26, "CzynnikGliny": 1.275, "CzynnikZelaza": 1.26, "CzynnikPopulacji": 1.17},
    {"Nazwa": "Tartak", "MaxPoziom": 30, "MinPoziom": 0, "Drewno": 50, "Glina": 60, "Zelazo": 40, "Populacja": 5, "CzynnikDrewna": 1.25, "CzynnikGliny": 1.275, "CzynnikZelaza": 1.245, "CzynnikPopulacji": 1.155},
    {"Nazwa": "Cegielnia", "MaxPoziom": 30, "MinPoziom": 0, "Drewno": 65, "Glina": 50, "Zelazo": 40, "Populacja": 10, "CzynnikDrewna": 1.27, "CzynnikGliny": 1.265, "CzynnikZelaza": 1.24, "CzynnikPopulacji": 1.14},
    {"Nazwa": "Huta Żelaza", "MaxPoziom": 30, "MinPoziom": 0, "Drewno": 75, "Glina": 65, "Zelazo": 70, "Populacja": 10, "CzynnikDrewna": 1.252, "CzynnikGliny": 1.275, "CzynnikZelaza": 1.24, "CzynnikPopulacji": 1.17},
    {"Nazwa": "Zagroda", "MaxPoziom": 30, "MinPoziom": 1, "Drewno": 45, "Glina": 40, "Zelazo": 30, "Populacja": 0, "CzynnikDrewna": 1.3, "CzynnikGliny": 1.32, "CzynnikZelaza": 1.29, "CzynnikPopulacji": 1},
    {"Nazwa": "Spichlerz", "MaxPoziom": 30, "MinPoziom": 1, "Drewno": 60, "Glina": 50, "Zelazo": 40, "Populacja": 0, "CzynnikDrewna": 1.265, "CzynnikGliny": 1.27, "CzynnikZelaza": 1.245, "CzynnikPopulacji": 1.15},
    {"Nazwa": "Mur", "MaxPoziom": 20, "MinPoziom": 0, "Drewno": 50, "Glina": 100, "Zelazo": 20, "Populacja": 5, "CzynnikDrewna": 1.26, "CzynnikGliny": 1.275, "CzynnikZelaza": 1.26, "CzynnikPopulacji": 1.17}
]

# Funkcja do obliczania zapotrzebowania na materiały
def oblicz_zapotrzebowanie(budynek, poziom):
    zapotrzebowanie = {}
    zapotrzebowanie["Drewno"] = budynek["Drewno"] * (budynek["CzynnikDrewna"] ** poziom)
    zapotrzebowanie["Glina"] = budynek["Glina"] * (budynek["CzynnikGliny"] ** poziom)
    zapotrzebowanie["Zelazo"] = budynek["Zelazo"] * (budynek["CzynnikZelaza"] ** poziom)
    zapotrzebowanie["Populacja"] = budynek["Populacja"] * (budynek["CzynnikPopulacji"] ** poziom)
    return zapotrzebowanie

# Interfejs Streamlit
st.title("Symulator zapotrzebowania na materiały budowlane")

# Wybór budynku
budynek_wybrany = st.selectbox("Wybierz budynek:", [b["Nazwa"] for b in budynki])

# Wyszukiwanie wybranego budynku
budynek = next(b for b in budynki if b["Nazwa"] == budynek_wybrany)

# Wybór poziomu budynku
poziom = st.slider(f"Wybierz poziom dla {budynek_wybrany}", budynek["MinPoziom"], budynek["MaxPoziom"], 1)

# Obliczanie zapotrzebowania na materiały
zapotrzebowanie = oblicz_zapotrzebowanie(budynek, poziom)

# Wyświetlanie wyników
st.subheader(f"Zapotrzebowanie na materiały dla {budynek_wybrany} na poziomie {poziom}")
st.write(f"Drewno: {zapotrzebowanie['Drewno']:.2f}")
st.write(f"Glina: {zapotrzebowanie['Glina']:.2f}")
st.write(f"Żelazo: {zapotrzebowanie['Zelazo']:.2f}")
st.write(f"Populacja: {zapotrzebowanie['Populacja']:.2f}")

# Dodanie tabeli dla zapotrzebowania na materiały dla różnych poziomów
tabela_wynikow = []
for p in range(budynek["MinPoziom"], budynek["MaxPoziom"] + 1):
    zapotrzebowanie = oblicz_zapotrzebowanie(budynek, p)
    tabela_wynikow.append({
        "Poziom": p,
        "Drewno": zapotrzebowanie["Drewno"],
        "Glina": zapotrzebowanie["Glina"],
        "Zelazo": zapotrzebowanie["Zelazo"],
        "Populacja": zapotrzebowanie["Populacja"]
    })

df = pd.DataFrame(tabela_wynikow)

# Wyświetlanie tabeli
st.subheader(f"Tabela zapotrzebowania dla {budynek_wybrany}")
st.dataframe(df)
