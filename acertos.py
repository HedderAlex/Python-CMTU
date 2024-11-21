# Imports
import matplotlib.pyplot as plt
import requests

# Rota provisória do Node.js
url = "http://localhost:8079/apiDados/perguntasCertas"

# Dados para teste do python sem o uso de node.js
#top_5_acertadas_json = """
#[
#    {"ID_ALTERNATIVA": 1, "TEXTO": "Alternativa A", "ACERTO": 70},
#    {"ID_ALTERNATIVA": 2, "TEXTO": "Alternativa B", "ACERTO": 65},
#    {"ID_ALTERNATIVA": 3, "TEXTO": "Alternativa C", "ACERTO": 60},
#    {"ID_ALTERNATIVA": 4, "TEXTO": "Alternativa D", "ACERTO": 55},
#    {"ID_ALTERNATIVA": 5, "TEXTO": "Alternativa E", "ACERTO": 50}
#]
#"""

try:
    # Fazendo a requisição
    response = requests.get(url)
    response.raise_for_status()

    # Obtendo os dados do JSON
    top_5_acertadas = response.json()  #Converte em um objeto python

    # Extraindo os dados para o gráfico
    textos = [item['TEXTO'] for item in top_5_acertadas]
    acertos = [item['ACERTO'] for item in top_5_acertadas]

    # Criando o gráfico
    plt.figure(figsize=(8, 5))
    color = (0.2, 0.4, 0.2, 0.6)  # vermelho, verde, azul, transparência
    plt.bar(textos, acertos, color=color)

    # Configurando o gráfico
    plt.title('Top 5 Perguntas Mais Acertadas', fontsize=16)
    plt.xlabel('Perguntas', fontsize=14)
    plt.ylabel('Quantidade de Acertos', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()

    # Exibindo o gráfico
    plt.show()

except requests.exceptions.RequestException as e:
    print(f"Erro ao se conectar à API: {e}")
except KeyError as e:
    print(f"Erro ao acessar dados do JSON: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
