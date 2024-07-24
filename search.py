import streamlit as st
import pandas as pd

# Função para carregar o banco de dados .xlsx
@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path)

# Função para filtrar os dados
def filter_data(df, search_term):
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term).any(), axis=1)]
    return filtered_df

# Função para exibir a tabela no estilo desejado
def display_table(df):
    # Transpor os dados para exibição no estilo desejado
    transposed_df = df.transpose()
    transposed_df.columns = [f'Column_{i}' for i in range(1, len(transposed_df.columns) + 1)]
    st.table(transposed_df)
    return transposed_df

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Consulta ao Banco de Dados")

option = st.selectbox(
    "Qual banco de dados deseja selecionar?",
    ("Termos de Embargo", "SICAR")
)

if option == "SICAR":
# Carregar o arquivo .xlsx
    file_path = "SR.xlsx"
    data = load_data(file_path)
else:
    file_path = "TER.xlsx"
    data = load_data(file_path)
      # Coloque o caminho do seu arquivo limpo aqui


# Título do aplicativo

# Campo de entrada para o conjunto de caracteres
search_term = st.text_input("Digite o termo de pesquisa:")

# Variável para armazenar a tabela exibida
displayed_table = None

if search_term:
    filtered_data = filter_data(data, search_term)
    if not filtered_data.empty:
        st.write(f"Resultados encontrados para '{search_term}':")
        displayed_table = display_table(filtered_data)
    else:
        st.write(f"Nenhum resultado encontrado para '{search_term}'.")
else:
    st.write("Digite um termo para iniciar a pesquisa.")

if st.button('Mostrar todos os dados'):
    displayed_table = display_table(data)

# Botão para baixar a imagem da tabela