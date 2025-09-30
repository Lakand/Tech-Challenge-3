import streamlit as st
import pandas as pd
import joblib


@st.cache_resource
def load_model():
    pipeline = joblib.load('modelo_churn_xgb.pkl')
    return pipeline

pipeline_churn = load_model()


st.title('Sistema de Previsão de Churn de Clientes')
st.markdown('Insira os dados do cliente para prever a probabilidade de churn.')

col1, col2, col3 = st.columns(3)

with col1:
    credit_score = st.number_input('Score de Crédito (CreditScore)', min_value=0, max_value=1000, value=650)
    geography = st.selectbox('País (Geography)', ('France', 'Germany', 'Spain'))
    gender = st.selectbox('Gênero (Gender)', ('Male', 'Female'))
    age = st.slider('Idade (Age)', 18, 100, 38)
    tenure = st.slider('Tempo como Cliente (Tenure)', 0, 10, 5)

with col2:
    balance = st.number_input('Saldo em Conta (Balance)', value=50000.0, format="%.2f")
    num_of_products = st.slider('Número de Produtos (NumOfProducts)', 1, 4, 1)
    has_cr_card = st.selectbox('Possui Cartão de Crédito? (HasCrCard)', (1, 0), format_func=lambda x: 'Sim' if x == 1 else 'Não')
    is_active_member = st.selectbox('É Membro Ativo? (IsActiveMember)', (1, 0), format_func=lambda x: 'Sim' if x == 1 else 'Não')
    
with col3:
    estimated_salary = st.number_input('Salário Estimado (EstimatedSalary)', value=100000.0, format="%.2f")
    satisfaction_score = st.slider('Pontuação de Satisfação (Satisfaction Score)', 1, 5, 3)
    card_type = st.selectbox('Tipo de Cartão (Card Type)', ('DIAMOND', 'GOLD', 'SILVER', 'PLATINUM'))
    point_earned = st.number_input('Pontos Ganhos (Point Earned)', min_value=0, value=500)
    
if st.button('Prever Churn'):
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
    
    st.subheader('Resultado da Previsão:')
    if probabilidade_churn > 0.5:
        st.error(f'ALTO RISCO DE CHURN: {probabilidade_churn:.2%} de probabilidade')
    else:
        st.success(f'BAIXO RISCO DE CHURN: {probabilidade_churn:.2%} de probabilidade')