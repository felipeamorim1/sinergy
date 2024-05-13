{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMIAE6XC43/cm45VxPFin17",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/felipeamorim1/sinergy/blob/main/Resumir_edital.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -U -q google-generativeai\n",
        "!pip install -q streamlit"
      ],
      "metadata": {
        "collapsed": true,
        "id": "rY1H1-fmGw0O"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Importe o módulo google.generativeai\n",
        "import google.generativeai as genai\n",
        "import streamlit as st\n",
        "\n",
        "# Defina a chave da API do Google\n",
        "from google.colab import userdata\n",
        "api_key = userdata.get('google_api_key')\n",
        "\n",
        "# Configure o módulo genai com a chave da API\n",
        "genai.configure(api_key=api_key)"
      ],
      "metadata": {
        "id": "ya_JGO3gHCsX"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "witxqABeGmRL",
        "outputId": "c5346671-a5d6-4f0a-a06b-e1e3dd7c03c0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-05-13 22:54:53.022 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n"
          ]
        }
      ],
      "source": [
        "# Configuração da página\n",
        "st.set_page_config(layout=\"wide\")\n",
        "st.title(\"Análise de Editais com IA\")\n",
        "\n",
        "# Upload do PDF\n",
        "uploaded_file = st.file_uploader(\"Selecione o edital em PDF:\")\n",
        "\n",
        "# Verificação do upload\n",
        "if uploaded_file is not None:\n",
        "    # Leitura do conteúdo do PDF\n",
        "    with open(uploaded_file.name, \"rb\") as pdf_file:\n",
        "        pdf_content = pdf_file.read()\n",
        "\n",
        "    # Análise do conteúdo do PDF\n",
        "    model = genai.GenerativeModel(model_name=\"gemini-1.5-pro-latest\")\n",
        "    system_instruction = \"Quem é você?\\nVocê é um especialista em análise de editais para captação de recursos públicos. \\nVocê também é convincente e persuasivo\\n\\nQual seu objetivo?\\nVocê precisa analisar editais e retornar as informações de forma estruturada para apresentar a um cliente um resumo do edital.\\n\\nComo você irá fazer?\\n 1 - Você irá analisar o edital;\\n 2 - Você retornará os dados que serão apresentados a seguir;\\n 3 - Você irá estruturar de forma simples e objetiva os campos como se fosse para apresentar a um cliente; \\n\\na seguir será colocado os campos que serão retornados.\\n\\nTítulo: (Insira o título do edital); \\nInstituição: (Insira a instituição promotora do edital);\\nSeguimento: (Insira o segmento de atuação do edital); \\nData final de Inscrição;\\nObjetivo do edital: (Descreva o objetivo principal do edital de forma sucinta e objetiva);\\nCritérios de elegibilidade: (Liste os critérios de elegibilidade para participar do edital, como requisitos de experiência, formação e documentação); \\nValor por projeto: (Insira o valor máximo por projeto, discriminando por fonte de financiamento);\\nItens financiáveis: (Liste os itens que podem ser financiados pelo edital, como diárias, materiais de consumo, serviços de terceiros, equipamentos e bolsas); \\nContrapartida: (Descreva a contrapartida exigida do beneficiário do edital, como percentual do valor total ou contrapartida específica); \\nPalavras-chave: (Liste as palavras-chave do edital, que podem ser utilizadas para pesquisa e categorização); \\nAbrangência de Regiões: (Indique a abrangência regional do edital, como estado, região ou nacional) \\nÁreas temáticas: (Liste as áreas temáticas do edital, que podem ser utilizadas para pesquisa e categorização); \\nPúblico-Alvo: (Descreva o público-alvo do edital, como tipo de organização, porte, área de atuação ou perfil profissional); \\nGrau de maturidade desejada do projeto:  (Descreva o grau de maturidade desejado para os projetos que se candidatem ao edital, como ideia inovadora, protótipo funcional ou empresa em estágio inicial);\\n\\nno final apresente vantagens simples e objetivas para participar desse edital.\\n\"\n",
        "\n",
        "    safety_settings = [\n",
        "        {\n",
        "            \"category\": \"HARM_CATEGORY_HARASSMENT\",\n",
        "            \"threshold\": \"BLOCK_MEDIUM_AND_ABOVE\"\n",
        "        },\n",
        "        {\n",
        "            \"category\": \"HARM_CATEGORY_HATE_SPEECH\",\n",
        "            \"threshold\": \"BLOCK_MEDIUM_AND_ABOVE\"\n",
        "        },\n",
        "        {\n",
        "            \"category\": \"HARM_CATEGORY_SEXUALLY_EXPLICIT\",\n",
        "            \"threshold\": \"BLOCK_MEDIUM_AND_ABOVE\"\n",
        "        },\n",
        "        {\n",
        "            \"category\": \"HARM_CATEGORY_DANGEROUS_CONTENT\",\n",
        "            \"threshold\": \"BLOCK_MEDIUM_AND_ABOVE\"\n",
        "        },\n",
        "    ]\n",
        "\n",
        "    convo = model.start_chat(history=[\n",
        "    ])\n",
        "\n",
        "    convo.send_message(pdf_content.decode(\"utf-8\"))\n",
        "\n",
        "    # Exibição do resultado da análise\n",
        "    st.write(\"**Resultado da Análise:**\")\n",
        "    st.write(convo.last.text)"
      ]
    }
  ]
}