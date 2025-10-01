import streamlit as st
# Alterado de 'build_sidebar' para 'get_user_input'
from ui import get_user_input
from prediction import load_model, predict, display_prediction

def main():
    """
    Função principal que executa a aplicação Streamlit.
    """
    
    # --- Configuração da Página ---
    st.set_page_config(
        page_title="Previsão de Churn",
        page_icon="🏦",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    # --- Título e Introdução ---
    st.title('Sistema de Previsão de Churn de Clientes')
    st.markdown("""
        Esta aplicação utiliza um modelo de Machine Learning (XGBoost) para prever a probabilidade 
        de um cliente deixar o banco (churn). 
        
        Preencha os dados do cliente nos campos abaixo para gerar uma previsão e uma recomendação de ação.
    """)
    st.divider()

    # --- Carregamento do Modelo ---
    pipeline = load_model()

    # --- Interface e Lógica de Predição ---
    if pipeline:
        user_input = get_user_input()
        
        st.divider()

        if st.button('Analisar Cliente', type="primary", use_container_width=True):
            with st.spinner('Realizando a previsão...'):
                probabilidade = predict(pipeline, user_input)
                display_prediction(probabilidade)
    else:
        st.warning("O modelo não pôde ser carregado. A aplicação não pode continuar.")

if __name__ == '__main__':
    main()