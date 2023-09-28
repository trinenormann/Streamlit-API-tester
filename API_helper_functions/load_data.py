
import streamlit as st
import csv
import pandas as pd
import requests

# Laster inn orgnummer
@st.cache_data(max_entries=100)
def get_orgnummer():
    file = open('data/organisasjonsnumre.csv')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    orgnummer = [val for sublist in rows for val in sublist]
    orgnummer = orgnummer[1:]
    return orgnummer

# Laster inn fylkesnummere
@st.cache_data(max_entries=100)
def get_fylker():
    url = "https://api.statistikkbanken.udir.no/api/rest/v2/Eksport/155/data?filter=EierformID(-10)_EnhetNivaa(2)_TidID(202212)_TrinnID(10)&format=0&sideNummer=1"
    response = requests.get(url)
    fylker = []
    for fylke in response.json():
        fylker.append(fylke['Fylkekode'])
    return fylker