import pandas as pd
import streamlit as st
import plotly.express as px

#Sempre que abrir o projeto use #Linux/macOS source .venv/bin/activate #Para Windowsvenv\Scripts\activate
#para executar no streamlit:cd app streamlit run app.py

# Configuração do título
st.title("Suporte WorkSpaceMobile")

# Upload do arquivo XLSX
uploaded_file = st.file_uploader("Carregue um arquivo XLSX", type=["xlsx"])

if uploaded_file:
    # Leitura do arquivo
    df = pd.read_excel(uploaded_file, engine='openpyxl')

    # Exibir quantidade total de linhas
    total_linhas = len(df)
    st.metric("Total de Tickets", total_linhas)

    # Verificar se as colunas existem
    colunas_esperadas = ["Analista Atual", "Cliente Solicitante", "Estado", "Última Fila"]
    colunas_faltando = [col for col in colunas_esperadas if col not in df.columns]

    if colunas_faltando:
        st.error(f"Colunas faltando no arquivo: {', '.join(colunas_faltando)}")
    else:
        # Contagem por Analista
        analista_count = df["Analista Atual"].value_counts().reset_index()
        analista_count.columns = ["Analista Atual", "Quantidade"]
        st.subheader("Quantidade de Tickets em Atendimento")
        fig_analista = px.bar(analista_count, x="Analista Atual", y="Quantidade", text="Quantidade",
                              title="Tickets por Analista Atual")
        st.plotly_chart(fig_analista)

        # Contagem por Cliente
        cliente_count = df["Cliente Solicitante"].value_counts().reset_index()
        cliente_count.columns = ["Cliente Solicitante", "Quantidade"]
        st.subheader("Quantidade de Tickets por Cliente Solicitante")
        fig_cliente = px.bar(cliente_count, x="Cliente Solicitante", y="Quantidade", text="Quantidade", title="Tickets por Cliente")
        fig_cliente.update_layout(
            margin=dict(b=150),  # Further increased bottom margin
            xaxis=dict(
                tickangle=90,  # Rotate labels 90 degrees for better spacing
                tickmode='array',
                ticktext=cliente_count["Cliente Solicitante"],
                tickfont=dict(size=10)  # Reduced font size for better fit
            )
        )
        st.plotly_chart(fig_cliente)

        # Contagem por Estado
        estado_count = df["Estado"].value_counts().reset_index()
        estado_count.columns = ["Estado", "Quantidade"]
        st.subheader("Quantidade de Tickets por Estado")
        fig_estado = px.pie(estado_count, names="Estado", values="Quantidade",
                            title="Distribuição de Tickets por Estado")
        st.plotly_chart(fig_estado)

        # Contagem por Última Fila
        fila_count = df["Última Fila"].value_counts().reset_index()
        fila_count.columns = ["Última Fila", "Quantidade"]
        st.subheader("Quantidade de Tickets por Fila")
        fig_fila = px.bar(fila_count, x="Última Fila", y="Quantidade", text="Quantidade",
                          title="Distribuição de Tickets por Fila")
        fig_fila.update_layout(
            margin=dict(b=150),
            xaxis=dict(
                tickangle=90,
                tickmode='array',
                ticktext=fila_count["Última Fila"],
                tickfont=dict(size=10)
            )
        )
        st.plotly_chart(fig_fila)

        # Exibir amostra dos dados
        st.subheader("Resumo dos Dados")
        st.dataframe(df.get(['Analista Atual', 'Cliente Solicitante', 'Estado', 'Última Fila']))
