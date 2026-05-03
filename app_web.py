import streamlit as st
from groq import Groq
import os

# Configuração da Página
st.set_page_config(page_title="O Oráculo - Já Perdes", page_icon="🔮", layout="centered")

# Estilo Customizado (Preto e Minimalista)
st.markdown("""
    <style>
    .main { background-color: #000000; color: white; }
    .stButton>button { background-color: #d9534f; color: white; width: 100%; border-radius: 10px; }
    .stTextInput>div>div>input { background-color: #0a0a0a; color: white; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

# Interface
st.image("LOGO JP-2025.png", width=200)
st.title("O diário de um otário")
st.write("A verdade não usa roupas de grife.")

# Inicializar Groq
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

# Sistema de Limite Simples (Sessão do Navegador)
if 'consultas' not in st.session_state:
    st.session_state.consultas = 3

if st.session_state.consultas > 0:
    user_input = st.text_input("Desabafa aqui...", placeholder="O que tens para dizer?")
    
    if st.button("OUVIR A VERDADE"):
        if user_input:
            with st.spinner("O Oráculo está a pensar..."):
                try:
                    completion = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        # Procura esta parte no teu código e substitui:
messages=[
    {
        "role": "system", 
        "content": """
        Tu és o Mentor da página Já Perdes. O teu estilo é de um Cavalheiro de Elite: 
        educado, polido, usa um vocabulário rico, mas é extremamente focado e direto. 
        Nunca és rude, mas nunca passas a mão na cabeça. 

        Estrutura da resposta:
        1. Começa sempre com uma breve análise: 'Nível de Ilusão: X%' e 'Foco: [Baixo/Médio/Alto]'.
        2. Responde com elegância, tratando o utilizador de forma respeitosa (ex: 'Meu caro', 'Estimado').
        3. Sê cirúrgico ao apontar onde ele está a falhar.
        
        Assinatura obrigatória: 
        Se o coração acelerou é porque é verdade. É o Já Perdes, onde a verdade não usa roupas de grife.
        """
    },
    {"role": "user", "content": user_input}
]
                    resposta = completion.choices[0].message.content
                    st.info(resposta)
                    st.session_state.consultas -= 1
                except:
                    st.error("Erro de conexão.")
else:
    st.warning("Acabou a borla.")
    st.link_button("🔥 DESBLOQUEAR CONSULTAS ILIMITADAS", "https://www.instagram.com/japerdes/")
