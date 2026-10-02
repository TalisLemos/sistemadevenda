
#Titulo: Sistema de vendas
#Sessao para cadastrar vendas
    #campo: data
    #Campo: vendedor
    #Campo: produto
    #Campo: quantidade
    #Campo: valor
    #Botao "cadastrar venda"
#Sesao de vendas cadastradas
    #Tabela com as vendas
#Sessao dashboard
    #Card com uam metrica (faturamento total)
    #Grafico de barra (venda por vendedor)
    #Grafico de pizza (venda por produto)

#streamlit | pandas | plotly
# streamlit run codigo.py

import streamlit as st
import pandas as pd
import plotly.express as px


#Carregar base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

#Sesao de vendas cadastradas
st.sidebar.write("## Cadastra vendas")
data = st.sidebar.date_input("data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carlos"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade",step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar venda")

if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    st.success("Venda cadastrada!")
    tabela_vendas.to_csv("vendas.csv", index=False)



#Sesao de vendas cadastradas /Visualizar vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)


#Sessao dashboard
st.write("## Dashoboard")

    #Card com uma metrica (faturamento total)
faturamento = tabela_vendas["valor"].sum()
faturamento_formatado = f"R$ {faturamento:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
st.metric("Faturamento total", faturamento_formatado)

    #Grafico de barra (venda por vendedor)
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

    #Grafico de pizza (venda por produto)
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)
