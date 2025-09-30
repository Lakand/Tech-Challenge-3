import streamlit as st
import pandas as pd
import joblib

# --- CARREGAMENTO DO MODELO ---
# Usar cache para carregar o modelo apenas uma vez e otimizar a performance
@st.cache_resource
def load_model():
    """Carrega o pipeline de machine learning do arquivo .pkl"""
    pipeline = joblib.load('modelo_churn_xgb.pkl')
    return pipeline

pipeline_churn = load_model()


# --- INTERFACE DO USUÁRIO ---
st.title('Sistema de Previsão de Churn de Clientes')
st.markdown("""
    Esta aplicação utiliza um modelo de Machine Learning (XGBoost) para prever a probabilidade 
    de um cliente deixar o banco (churn). 
    
    Preencha os dados do cliente nos campos abaixo para gerar uma previsão e uma recomendação de ação.
""")
st.divider()


# --- COLETA DOS DADOS DE ENTRADA ---
col1, col2 = st.columns(2)

with col1:
    with st.expander("Informações Pessoais e de Crédito", expanded=True):
        credit_score = st.number_input('Score de Crédito (CreditScore)', min_value=0, max_value=1000, value=650, help="Pontuação de crédito do cliente, geralmente entre 300 e 850.")
        geography = st.selectbox('País (Geography)', ('France', 'Germany', 'Spain'))
        gender = st.selectbox('Gênero (Gender)', ('Male', 'Female'))
        age = st.slider('Idade (Age)', 18, 100, 38)
        tenure = st.slider('Tempo como Cliente (Anos)', 0, 10, 5, help="Há quantos anos a pessoa é cliente do banco.")

with col2:
    with st.expander("Informações da Conta e Produtos", expanded=True):
        balance = st.number_input('Saldo em Conta (Balance)', value=50000.0, format="%.2f")
        num_of_products = st.slider('Número de Produtos', 1, 4, 1, help="Número de produtos que o cliente possui no banco (ex: conta, cartão, investimento).")
        has_cr_card = st.selectbox('Possui Cartão de Crédito?', (1, 0), format_func=lambda x: 'Sim' if x == 1 else 'Não')
        is_active_member = st.selectbox('É Membro Ativo?', (1, 0), format_func=lambda x: 'Sim' if x == 1 else 'Não', help="Indica se o cliente teve movimentação recente na conta.")
        estimated_salary = st.number_input('Salário Estimado por ano (EstimatedSalary)', value=100000.0, format="%.2f")

with st.expander("Informações Adicionais de Engajamento"):
    col3, col4, col5, col6 = st.columns(4)
    with col3:
        satisfaction_score = st.slider('Pontuação de Satisfação', 1, 5, 3)
    with col4:
        card_type = st.selectbox('Tipo de Cartão', ('DIAMOND', 'GOLD', 'SILVER', 'PLATINUM'))
    with col5:
        point_earned = st.number_input('Pontos Ganhos (Programa de Fidelidade)', min_value=0, value=500)


# --- EXECUÇÃO E EXIBIÇÃO DA PREVISÃO ---
if st.button('Prever Churn', type="primary"):
    # Criar DataFrame com os dados de entrada
    input_data = pd.DataFrame({
        'CreditScore': [credit_score],
        'Geography': [geography],
        'Gender': [gender],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'NumOfProducts': [num_of_products],
        'HasCrCard': [has_cr_card],
        'IsActiveMember': [is_active_member],
        'EstimatedSalary': [estimated_salary],
        'Satisfaction Score': [satisfaction_score],
        'Card Type': [card_type],
        'Point Earned': [point_earned]
    })

  
    probabilidade_churn = pipeline_churn.predict_proba(input_data)[:, 1][0]
    
    st.divider()
    st.subheader('Resultado da Previsão:')
    

    if probabilidade_churn > 0.5:
        st.error(f'ALTO RISCO DE CHURN: {probabilidade_churn:.2%} de probabilidade')
        st.warning('**Recomendação de Ação:** Este cliente possui um perfil com alta propensão a deixar o banco. Recomenda-se que a equipe de retenção entre em contato para oferecer benefícios, entender suas necessidades ou resolver possíveis problemas.')
    else:
        st.success(f'BAIXO RISCO DE CHURN: {probabilidade_churn:.2%} de probabilidade')
        st.info('**Recomendação de Ação:** Este cliente apresenta baixa probabilidade de churn. Monitore o comportamento, mas nenhuma ação de retenção imediata é necessária.')