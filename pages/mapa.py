import streamlit as st


html = '<iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d966105.425427681!2d-40.63658880180354!3d-18.938062642931758!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0xca9f6f582f152d%3A0x2b4e17a912a0c48e!2sSuzano%20-%20Unidade%20Mucuri%2C%20Rod.%20BR%20101%2C%20Km%20945%2C5%2C%20s%2Fn%20Zona%20Industrial%2C%20Mucuri%20-%20BA%2C%2045930-000!3m2!1d-18.042383!2d-39.919638!4m5!1s0xb7de81d7c5c3cb%3A0x51d7131646cd1e98!2sPortocel%20-%20Barra%20do%20Riacho%2C%20Aracruz%20-%20ES!3m2!1d-19.8333892!2d-40.0632557!5e0!3m2!1spt-BR!2sbr!4v1673543950352!5m2!1spt-BR!2sbr" width="800" height="450" style="border:0; align-itens:center" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'


html2 = '<iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d966105.425427681!2d-40.63658880180354!3d-18.938062642931758!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0xca9f6f582f152d%3A0x2b4e17a912a0c48e!2sSuzano%20-%20Unidade%20Mucuri%2C%20Rod.%20BR%20101%2C%20Km%20945%2C5%2C%20s%2Fn%20Zona%20Industrial%2C%20Mucuri%20-%20BA%2C%2045930-000!3m2!1d-18.042383!2d-39.919638!4m5!1s0xb7de81d7c5c3cb%3A0x51d7131646cd1e98!2sPortocel%20-%20Barra%20do%20Riacho%2C%20Aracruz%20-%20ES!3m2!1d-19.8333892!2d-40.0632557!5e0!3m2!1spt-BR!2sbr!4v1673543950352!5m2!1spt-BR!2sbr" width="800" height="450" style="border:0; align-itens:center" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'   
html3 = '<iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d1932225.310849235!2d-40.063266031928116!3d-19.833284192519773!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0xca9f6f582f152d%3A0x2b4e17a912a0c48e!2sSuzano%20-%20Unidade%20Mucuri%2C%20Rod.%20BR%20101%2C%20Km%20945%2C5%2C%20s%2Fn%20Zona%20Industrial%2C%20Mucuri%20-%20BA%2C%2045930-000!3m2!1d-18.042383!2d-39.919638!4m5!1s0xb7ea9b6cb3af0d%3A0xf77c4d3ca214b280!2sSuzano%20Aracruz%20-%20ES%20-%20Barra%20do%20Riacho%2C%20Aracruz%20-%20ES!3m2!1d-19.839581!2d-40.0824332!5e0!3m2!1spt-BR!2sbr!4v1673545465274!5m2!1spt-BR!2sbr" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'  


st.markdown(html3, unsafe_allow_html=True)