Este projeto teve como objetivo desenvolver um modelo de Machine Learning para prever a rotatividade (churn) de clientes de um banco, a partir de um conjunto de dados com informações demográficas e de conta. A finalidade do modelo é identificar proativamente os clientes com maior risco de encerrar seu relacionamento com a instituição, permitindo que ações de retenção sejam direcionadas de forma mais eficaz.

Após um ciclo completo de análise exploratória, pré-processamento de dados e otimização de hiperparâmetros, o modelo **XGBoost** foi selecionado como a solução mais performática. A performance foi validada rigorosamente com a técnica de Validação Cruzada, garantindo a robustez dos resultados.

### Principais Descobertas e Insights Acionáveis

A análise exploratória dos dados revelou padrões de comportamento cruciais para a estratégia de negócio:

* **O "Ponto Ideal" de Produtos:** A relação entre o número de produtos e o churn não é linear. Clientes com **2 produtos** são os mais fiéis (taxa de churn de apenas 7,6%), mas a taxa salta para alarmantes **82,7%** para clientes com **3 produtos**, indicando uma grave falha na jornada ou oferta para este segmento.

* **A Inatividade como Sinal de Alerta:** Clientes classificados como inativos (`IsActiveMember = 0`) têm quase o **dobro da probabilidade de sair** (churn de 26,9%) em comparação com os clientes ativos (14,3%). Isso posiciona a inatividade como um forte indicador preditivo e uma oportunidade para campanhas de reengajamento.

* **Fator Idade:** O risco de churn aumenta com a idade, sendo mais concentrado na faixa entre **40 e 50 anos**, em contraste com os clientes mais leais, que se concentram na faixa dos 30 aos 40 anos.

### Performance e Valor de Negócio do Modelo Final

O modelo XGBoost final demonstrou uma performance sólida e estável, com as seguintes métricas médias obtidas na validação cruzada:

* **ROC AUC de 0.85:** Excelente capacidade de distinguir entre clientes que irão ou não evadir.
* **F1-Score (Churn) de 0.60:** Bom equilíbrio entre precisão e revocação para a classe de interesse.

Em termos de negócio, isso significa que o modelo é capaz de **identificar corretamente mais da metade (54%)** dos clientes que realmente iriam sair e, quando sinaliza um cliente como risco, ele está **correto em 2 de cada 3 casos (67%)**. Este nível de performance torna o modelo uma ferramenta valiosa e acionável para otimizar os esforços de retenção e minimizar a perda de receita.