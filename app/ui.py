import streamlit as st

def get_user_input():
    """
    Cria a interface do usuário com seções expansíveis (expanders) e colunas
    para coletar os dados do cliente.
    Retorna um dicionário com todos os valores de entrada.
    """
    input_data = {}

    # --- Criação das duas colunas principais ---
    col1, col2 = st.columns(2)

    with col1:
        with st.expander("Informações Pessoais e de Crédito", expanded=True):
            input_data['CreditScore'] = st.number_input('Score de Crédito (CreditScore)', min_value=0, max_value=1000, value=650, help="Pontuação de crédito do cliente, geralmente entre 300 e 850.")
            input_data['Geography'] = st.selectbox('País (Geography)', ('France', 'Germany', 'Spain'))
            input_data['Gender'] = st.selectbox('Gênero (Gender)', ('Male', 'Female'))
            input_data['Age'] = st.slider('Idade (Age)', 18, 100, 38)
            input_data['Tenure'] = st.slider('Tempo como Cliente (Anos)', 0, 10, 5, help="Há quantos anos a pessoa é cliente do banco.")

    with col2:
        with st.expander("Informações da Conta e Produtos", expanded=True):
            input_data['Balance'] = st.number_input('Saldo em Conta (Balance)', value=50000.0, format="%.2f")
            input_data['NumOfProducts'] = st.slider('Número de Produtos', 1, 3, 1, help="Número de produtos que o cliente possui no banco (ex: conta, cartão, investimento).")
            input_data['HasCrCard'] = st.selectbox('Possui Cartão de Crédito?', (1, 0), format_func=lambda x: 'Sim' if x == 1 else 'Não')
            input_data['IsActiveMember'] = st.selectbox('É Membro Ativo?', (1, 0), format_func=lambda x: 'Sim' if x == 1 else 'Não', help="Indica se o cliente teve movimentação recente na conta.")
            input_data['EstimatedSalary'] = st.number_input('Salário Estimado por ano (EstimatedSalary)', value=100000.0, format="%.2f")

    # --- Expander para informações adicionais abaixo das colunas ---
    with st.expander("Informações Adicionais de Engajamento"):
        sub_col1, sub_col2, sub_col3 = st.columns(3)
        with sub_col1:
            input_data['Satisfaction Score'] = st.slider('Pontuação de Satisfação', 1, 5, 3)
        with sub_col2:
            input_data['Card Type'] = st.selectbox('Tipo de Cartão', ('DIAMOND', 'GOLD', 'SILVER', 'PLATINUM'))
        with sub_col3:
            input_data['Point Earned'] = st.number_input('Pontos Ganhos (Programa de Fidelidade)', min_value=0, value=500)

    return input_data