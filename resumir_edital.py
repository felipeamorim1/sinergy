# -*- coding: utf-8 -*-
import os

os.system("pip install -U -q google-generativeai")

!pip install -q streamlit

# Importe o módulo google.generativeai
import google.generativeai as genai
import streamlit as st

# Defina a chave da API do Google
from google.colab import userdata
api_key = userdata.get('google_api_key')

# Configure o módulo genai com a chave da API
genai.configure(api_key=api_key)

# Configuração da página
st.set_page_config(layout="wide")
st.title("Análise de Editais com IA")

# Upload do PDF
uploaded_file = st.file_uploader("Selecione o edital em PDF:")

# Verificação do upload
if uploaded_file is not None:
    # Leitura do conteúdo do PDF
    with open(uploaded_file.name, "rb") as pdf_file:
        pdf_content = pdf_file.read()

    # Análise do conteúdo do PDF
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
    system_instruction = "Quem é você?\nVocê é um especialista em análise de editais para captação de recursos públicos. \nVocê também é convincente e persuasivo\n\nQual seu objetivo?\nVocê precisa analisar editais e retornar as informações de forma estruturada para apresentar a um cliente um resumo do edital.\n\nComo você irá fazer?\n 1 - Você irá analisar o edital;\n 2 - Você retornará os dados que serão apresentados a seguir;\n 3 - Você irá estruturar de forma simples e objetiva os campos como se fosse para apresentar a um cliente; \n\na seguir será colocado os campos que serão retornados.\n\nTítulo: (Insira o título do edital); \nInstituição: (Insira a instituição promotora do edital);\nSeguimento: (Insira o segmento de atuação do edital); \nData final de Inscrição;\nObjetivo do edital: (Descreva o objetivo principal do edital de forma sucinta e objetiva);\nCritérios de elegibilidade: (Liste os critérios de elegibilidade para participar do edital, como requisitos de experiência, formação e documentação); \nValor por projeto: (Insira o valor máximo por projeto, discriminando por fonte de financiamento);\nItens financiáveis: (Liste os itens que podem ser financiados pelo edital, como diárias, materiais de consumo, serviços de terceiros, equipamentos e bolsas); \nContrapartida: (Descreva a contrapartida exigida do beneficiário do edital, como percentual do valor total ou contrapartida específica); \nPalavras-chave: (Liste as palavras-chave do edital, que podem ser utilizadas para pesquisa e categorização); \nAbrangência de Regiões: (Indique a abrangência regional do edital, como estado, região ou nacional) \nÁreas temáticas: (Liste as áreas temáticas do edital, que podem ser utilizadas para pesquisa e categorização); \nPúblico-Alvo: (Descreva o público-alvo do edital, como tipo de organização, porte, área de atuação ou perfil profissional); \nGrau de maturidade desejada do projeto:  (Descreva o grau de maturidade desejado para os projetos que se candidatem ao edital, como ideia inovadora, protótipo funcional ou empresa em estágio inicial);\n\nno final apresente vantagens simples e objetivas para participar desse edital.\n"

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    convo = model.start_chat(history=[
    ])

    convo.send_message(pdf_content.decode("utf-8"))

    # Exibição do resultado da análise
    st.write("**Resultado da Análise:**")
    st.write(convo.last.text)
