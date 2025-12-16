import streamlit as st
import pandas as pd

# Título
st.title("📊 Dashboard de Desempenho Escolar")

# Carregar dados
dados = pd.read_csv("notas.csv")

# Mostrar tabela
st.subheader("Notas dos alunos")
st.dataframe(dados)

# Cálculos
media = dados["Nota"].mean()
maior = dados["Nota"].max()
menor = dados["Nota"].min()

# Métricas
st.subheader("Resumo")
st.write(f"📌 Média da turma: {media:.2f}")
st.write(f"🏆 Maior nota: {maior}")
st.write(f"⚠️ Menor nota: {menor}")

# Gráfico
st.subheader("Gráfico de notas")
st.bar_chart(dados.set_index("Aluno"))
