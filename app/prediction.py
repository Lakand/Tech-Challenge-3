import streamlit as st
import joblib
import pandas as pd

@st.cache_resource
def load_model():
    """Carrega o pipeline de machine learning do arquivo .pkl em cache."""
    try:
        pipeline = joblib.load('modelo_churn_xgb.pkl')
        return pipeline
    except FileNotFoundError:
        st.error("Arquivo do modelo 'modelo_churn_xgb.pkl' não encontrado. Certifique-se de que ele está na pasta correta.")
        return None

def predict(pipeline, input_data):
    """
    Realiza a predição de churn usando o pipeline carregado e os dados de entrada.
    Retorna a probabilidade de churn.
    """
    input_df = pd.DataFrame([input_data])
    probabilidade_churn = pipeline.predict_proba(input_df)[:, 1][0]
    return probabilidade_churn

def display_prediction(probabilidade):
    """
    Exibe o resultado da predição e a recomendação de ação na interface.
    """
    st.subheader('Resultado da Previsão:')
    
    if probabilidade > 0.5:
        st.error(f'ALTO RISCO DE CHURN: {probabilidade:.2%} de probabilidade')
        st.warning('**Recomendação de Ação:** Este cliente possui um perfil com alta propensão a deixar o banco. Recomenda-se que a equipe de retenção entre em contato para oferecer benefícios, entender suas necessidades ou resolver possíveis problemas.')
    else:
        st.success(f'BAIXO RISCO DE CHURN: {probabilidade:.2%} de probabilidade')
        st.info('**Recomendação de Ação:** Este cliente apresenta baixa probabilidade de churn. Monitore o comportamento, mas nenhuma ação de retenção imediata é necessária.')