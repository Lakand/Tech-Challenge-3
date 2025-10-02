# Previsão de Churn de Clientes Bancários - Tech Challenge Fase 3

Este projeto foi desenvolvido como solução para o Tech Challenge da Fase 3 do curso de Machine Learning Engineering. O objetivo principal é aplicar um ciclo completo de ciência de dados, desde a análise de um problema de negócio até a implementação de um modelo preditivo em uma aplicação funcional.

## 1. Contexto do Problema

A rotatividade de clientes, conhecida como **churn**, é um dos desafios mais críticos para instituições financeiras. Perder um cliente não significa apenas a perda de receita recorrente, mas também implica em custos adicionais para adquirir novos clientes, que são significativamente mais altos do que os custos para reter os existentes.

Neste cenário, o desafio é desenvolver um modelo de Machine Learning capaz de **identificar proativamente os clientes com maior risco de encerrar seu relacionamento com o banco**. Com essa capacidade preditiva, a instituição pode direcionar ações de retenção de forma mais eficaz e personalizada, otimizando recursos e minimizando a perda de receita.

## 2. Fonte dos Dados

O conjunto de dados utilizado neste projeto é o "Bank Customer Churn Prediction" e foi obtido através da plataforma Kaggle. Ele contém informações demográficas e de conta de clientes de um banco, sendo ideal para a modelagem de previsão de rotatividade.

- **Link para o Dataset:** [https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn/data](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn/data)

## 3. Estrutura do Projeto
O projeto foi organizado de forma modular para garantir clareza, manutenibilidade e escalabilidade:
* `/app`: Contém todo o código-fonte da aplicação Streamlit, separado em módulos para a interface (`ui.py`) e para a lógica de predição (`prediction.py`).
* `/data`: Armazena o conjunto de dados brutos utilizado na análise e no treinamento.
* `tech_challenge_3.ipynb`: Notebook Jupyter com toda a análise exploratória, pré-processamento e o processo de modelagem.
* `modelo_churn_xgb.pkl`: Artefato do modelo treinado e pronto para ser consumido pela aplicação.

## 4. Análise Exploratória e Principais Insights de Negócio

Antes da modelagem, foi realizada uma Análise Exploratória de Dados (EDA) para compreender o comportamento dos clientes e identificar os principais fatores que influenciam a decisão de churn. As descobertas mais relevantes foram:

* **O "Ponto Ideal" de Produtos:** A relação entre o número de produtos que um cliente possui e a taxa de churn não é linear. Clientes com **2 produtos** são os mais fiéis (taxa de churn de apenas 7,6%), mas a taxa salta para alarmantes **82,7%** para clientes com **3 produtos**. Isso sugere uma possível falha na oferta ou na jornada do cliente para este segmento específico, tornando-o um alvo prioritário para investigação.

* **A Inatividade como Sinal de Alerta:** Clientes classificados como inativos (`IsActiveMember = 0`) têm quase o **dobro da probabilidade de sair** (churn de 26,4%) em comparação com os clientes ativos (13,7%). A inatividade é, portanto, um forte indicador preditivo e uma oportunidade clara para campanhas de reengajamento.

* **Fator Idade:** O risco de churn tende a aumentar com a idade, concentrando-se na faixa entre **40 e 50 anos**. Em contrapartida, os clientes mais leais estão na faixa dos 30 aos 40 anos, indicando diferentes ciclos de vida e necessidades financeiras.

## 5. Pré-processamento dos Dados

Para preparar os dados para os algoritmos de Machine Learning, foram aplicadas as seguintes técnicas:

1.  **Transformação de Features Categóricas:** Variáveis como `Geography`, `Gender` e `Card Type` foram convertidas para um formato numérico utilizando `OneHotEncoder`.
2.  **Padronização de Features Numéricas:** Todas as variáveis numéricas foram normalizadas com `StandardScaler` para que tivessem a mesma escala, evitando que features com valores maiores dominassem o modelo.
3.  **Tratamento de Desbalanceamento de Classe:** O conjunto de dados original é desbalanceado (cerca de 80% de não-churn e 20% de churn). Para evitar que o modelo se tornasse enviesado para a classe majoritária, a técnica **SMOTE (Synthetic Minority Over-sampling Technique)** foi aplicada *apenas no conjunto de treino* para criar exemplos sintéticos da classe minoritária e balancear os dados.

A aplicação do SMOTE após a divisão treino-teste foi uma decisão metodológica crucial para evitar o vazamento de dados (*data leakage*) e garantir que a avaliação do modelo fosse realista.

## 6. Modelagem e Performance

Foram testados cinco algoritmos de classificação diferentes para identificar a solução mais performática: Regressão Logística, Random Forest, XGBoost, SVM e MLP.

Após uma rodada de otimização de hiperparâmetros com `RandomizedSearchCV`, o modelo **XGBoost** foi selecionado como a solução final por apresentar o melhor equilíbrio entre as métricas de avaliação.

A performance do modelo final foi rigorosamente validada com a técnica de **Validação Cruzada Estratificada com 10 folds**, garantindo a robustez e a estabilidade dos resultados. As métricas médias obtidas foram:

* **ROC AUC de 0.856:** Excelente capacidade de distinguir entre clientes que irão ou não evadir.
* **F1-Score (para a classe Churn) de 0.603:** Ótimo equilíbrio entre precisão e revocação, sendo a principal métrica de otimização para problemas desbalanceados.
* **Precisão (para a classe Churn) de 0.664:** Quando o modelo prevê que um cliente sairá, ele está correto em 2 de cada 3 casos.
* **Revocação (para a classe Churn) de 0.553:** O modelo é capaz de identificar corretamente mais da metade dos clientes que realmente iriam sair.

Em termos de negócio, o F1-Score e a Revocação demonstram que o modelo é uma ferramenta valiosa e acionável para otimizar os esforços de retenção e minimizar a perda de receita.

## 7. Produtização com Streamlit

Para demonstrar a aplicabilidade prática do modelo, foi desenvolvida uma aplicação web simples utilizando a biblioteca **Streamlit**.

A aplicação permite que um usuário:
1.  Insira os dados de um cliente através de um formulário interativo.
2.  Submeta os dados para o modelo treinado (`modelo_churn_xgb.pkl`).
3.  Receba em tempo real a previsão da probabilidade de churn, com uma indicação clara de "ALTO RISCO" ou "BAIXO RISCO".

Esta aplicação serve como um protótipo funcional de como o modelo de Machine Learning pode ser integrado a uma ferramenta de negócios para auxiliar na tomada de decisão.

## 8. Tecnologias Utilizadas

-   **Linguagem:** Python 3
-   **Análise e Modelagem:** Pandas, Scikit-learn, XGBoost, Imbalanced-learn, Joblib
-   **Visualização de Dados:** Matplotlib, Seaborn
-   **Aplicação Web (Dashboard):** Streamlit
-   **Ambiente e Versionamento:** Jupyter Notebook, Git


## 9. Como Executar o Projeto Localmente

Para executar a aplicação Streamlit em sua máquina, siga os passos abaixo.

### Pré-requisitos
* Python 3.8+
* Git

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO_AQUI>
    cd <NOME_DA_PASTA_DO_REPOSITORIO>
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    O projeto utiliza as bibliotecas listadas no arquivo `requirements.txt`. Instale-as com o seguinte comando:
    ```bash
    pip install -r requirements.txt
    ```
   

4.  **Execute a aplicação Streamlit:**
    Após a instalação, execute o comando abaixo no seu terminal (lembre-se de estar na pasta raiz do projeto):
    ```bash
    streamlit run app/app.py
    ```

5.  A aplicação será aberta automaticamente no seu navegador padrão.