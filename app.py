import streamlit as st
import numpy as np
# from scrapping_diesel import consultar_preco
import locale
import pandas as pd
# import seaborn as sns

# locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

with st.sidebar:

    distancia_atual = 464
    volume_por_veiculo_atual = 50
    tarifa_tonelada_atual = 29.68
    pedagio_por_eixo = 13.2
    media_consumo_atual = 2.1
    pedagio_total_por_tonelada = 0
    
    distancia_cenario = 2 * st.number_input("Distância ida e retorno em km:", value=244)
    volume_por_veiculo_cenario = st.number_input("Volume por veículo em ton:", value=50)
    tarifa_tonelada_atual = st.number_input("Tarifa R$:", value=29.68)
    qtd_eixos_ida = st.slider("Eixos ida:", min_value=5, max_value=9, value=7, step=1)
    qtd_eixos_retorno = st.slider("Eixos retorno:", min_value=5, max_value=9, value=7, step=1)
    media_consumo_cenario = st.number_input("Consumo médio por litro:", value=2.1)
    custo_diesel = st.number_input("Custo do diesel por litro:", value=6.3)
    lista_pontos_pedagio = {'Pedro Canário' : 3.7, 'São Mateus' : 4.9, 'Aracruz' : 4.6}
    lista_pontos_pedagio_cenario = st.multiselect('Pontos de pedágio na rota:', 
                                                  options=lista_pontos_pedagio.keys(), 
                                                  default=lista_pontos_pedagio.keys(), )
    
    for ponto in lista_pontos_pedagio_cenario:
            pedagio_total_por_tonelada += lista_pontos_pedagio[ponto]
            
st.markdown('''
            # Simualdor de Cenários de Transporte
            Um app para calcular cenários de transporte e auxiliar na tomada de decisões estratégicas diante de situações adversas.
            
            ---
            ''')

st.markdown('''
        ### Resultados
        ''')

with st.container():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
                tarifa_diesel_atual = (distancia_atual / media_consumo_atual) * custo_diesel / volume_por_veiculo_atual
                tarifa_diesel_cenario = (distancia_cenario / media_consumo_cenario) * custo_diesel / volume_por_veiculo_cenario
                
                # st.metric(label='Diesel Atual', 
                #         value="% .2f" % (tarifa_diesel_atual))
                
                st.metric(label='Diesel / Ton', 
                        value="% .2f" % (tarifa_diesel_cenario), 
                        delta="% .2f" % (tarifa_diesel_cenario - tarifa_diesel_atual),
                        delta_color='inverse')
                
                
        with col2:
                # tarifa_tonelada_atual = frete_cenario / volume_por_veiculo_cenario 
                
                # st.metric(label='Frete ', 
                #         value="% .2f" % (tarifa_tonelada_atual))
                
                st.metric(label='Tarifa / Ton', 
                        value="% .2f" % (tarifa_tonelada_atual),
                        delta="% .2f" % (tarifa_tonelada_atual - tarifa_tonelada_atual),
                        delta_color='inverse')
                
                
        with col3:
                pedagio_atual = (pedagio_por_eixo * (9 + 7)) / volume_por_veiculo_atual
                pedagio_cenario = (pedagio_total_por_tonelada * (qtd_eixos_ida + qtd_eixos_retorno)) / volume_por_veiculo_cenario
                # st.metric(label='Pedágio', 
                #         value="% .2f" % (pedagio_atual))
                
                st.metric(label='Pedágio / Ton', 
                        value="% .2f" % (pedagio_cenario),
                        delta="% .2f" % (pedagio_cenario - pedagio_atual),
                        delta_color='inverse')


        with col4:
                total_atual = tarifa_diesel_atual + tarifa_tonelada_atual + pedagio_atual
                total_cenario = tarifa_diesel_cenario + tarifa_tonelada_atual + pedagio_cenario
                # st.metric(label='Total', 
                #         value="% .2f" % (total_atual))
        
                st.metric(label='Total / Ton', 
                        value="% .2f" % (total_cenario),
                        delta="% .2f" % (total_cenario - total_atual),
                        delta_color='inverse')

with st.container():
        st.markdown('''
        ### Projeções de Volume
        ''')
        
        col1, col2 = st.columns(2)
        
        with col1:
                dias_simulacao = st.number_input("Dias de operação:", value=1)
                
        with col2:
                qtd_veiculos_dia = st.number_input("Quantidade de veiculos:", value=1)

        timeline = np.arange(1, dias_simulacao+1)
        acumulado = timeline * volume_por_veiculo_cenario * qtd_veiculos_dia 
        df = pd.DataFrame(acumulado, timeline, columns=["Dias"])
        st.bar_chart(df)
        
        timeline = np.arange(1, dias_simulacao+1)
        diesel_total = acumulado * tarifa_diesel_cenario
        tarifa_total = acumulado * tarifa_tonelada_atual
        pedagio_total = acumulado * pedagio_cenario
        df = pd.DataFrame({'Diesel':diesel_total, 'Tarifa':tarifa_total, 'Pedágio':pedagio_total}, timeline)
        st.bar_chart(df)