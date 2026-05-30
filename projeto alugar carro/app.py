import streamlit as st
from datetime import datetime

st.sidebar.image("logo.png")

st.sidebar.title("🚨Rent car🏎️ ")

moto_carro = st.sidebar.selectbox("escolha a moto ou carro da sua preferencia ao qual voce vai querer alugar:", ["audii","ferrari","kawasaki","yamaha YZF-R3"])
valor_diaria = {"audii":1750, "ferrari":10000, "kawasaki":2754, "yamaha YZF-R3":2700}

st.image(f"{moto_carro}.png")
st.subheader(f"{moto_carro}| DIaria: R$ {valor_diaria[moto_carro]}")

data_retirada = st.date_input("selecione o dia da retirada: ", datetime.now(), datetime.now())
data_devolução = st.date_input("selecione o dia de devolução: ", data_retirada, data_retirada)

if st.button("alugar"):
    dias = (data_devolução - data_retirada).days 
    valor_total = valor_diaria[moto_carro] * dias 
    st.subheader(f"alugando o {moto_carro} por {dias} dias, o total é: R$ {valor_total}")
    st.metric("o total do aluguel foi de", f"R${valor_total:.2f}")


st.feedback("stars")
st.markdown("<br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

st.text_area("Deixe um comentário: ")
if st.button("Comentar"):
    st.snow()