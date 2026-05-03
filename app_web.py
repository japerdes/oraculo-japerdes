import streamlit as st
from groq import Groq
import os

# Configuração da Página
st.set_page_config(page_title="O Oráculo - Já Perdes", page_icon="🔮", layout="centered")

# Estilo Customizado
st.markdown("""
    <style>
    .main { background-color: #000000; color: white; }
    .stButton>button { background-color: #d9534f; color: white; width: 100%; border-radius: 10px; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #0a0a0a; color: white; border: 1px solid #333; }
    .stInfo { background-color: #111; border: 1px solid #333; color: #ddd; }
    </style>
    """, unsafe_allow_html=True)

# Interface
st.image("LOGO JP-2025.png", width=180)
st.title("O Oráculo")
st.write("A elegância da verdade nua e crua.")

# Inicializar Groq (Usando Secrets para segurança)
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Erro: Configure a GROQ_API_KEY nos Secrets do Streamlit.")

# Sistema de Consultas
if 'consultas' not in st.session_state:
    st.session_state.consultas = 3

if st.session_state.consultas > 0:
    user_input = st.text_input("Expunha a sua situação, meu caro...", placeholder="O que o inquieta?")
    
    if st.button("OUVIR A VERDADE"):
        if user_input:
            with st.spinner("O Oráculo analisa a sua lucidez..."):
                try:
                    completion = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[
                            {
                                "role": "system", 
                                "content": """
                                Tu és o Mentor da página Já Perdes. O teu estilo é de um Cavalheiro de Elite: 
                                educado, polido e refinado, mas extremamente direto. 
                                Nunca és rude, mas és implacável na verdade.

                                Estrutura obrigatória da resposta:
                                1. Começa com: '⚖️ Análise de Lucidez: [Nível de Ilusão: X% | Foco Necessário: Alto/Médio]'.
                                2. Responde com elegância (ex: 'Meu caro', 'Estimado').
                                3. Sê cirúrgico ao apontar a falha.
                                
                                Assinatura: Se o coração acelerou é porque é verdade. É o Já Perdes, onde a verdade não usa roupas de grife.
                                """
                            },
                            {"role": "user", "content": user_input}
                        ],
                        temperature=0.6
                    )
                    resposta = completion.choices[0].message.content
                    st.info(resposta)
                    st.session_state.consultas -= 1
                    st.write(f"Sessões de cortesia restantes: {st.session_state.consultas}")
                except Exception as e:
                    st.error(f"Ocorreu um erro na ligação: {e}")
else:
    st.warning("Estimado, as suas consultas de cortesia terminaram.")
    st.link_button("🔥 DESBLOQUEAR ACESSO ILIMITADO", "https://www.instagram.com/japerdes/")
