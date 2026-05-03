import streamlit as st
from groq import Groq

# 1. Configuração de Estética, Animações e Centralização
st.set_page_config(page_title="Oráculo Já Perdes", page_icon="🔮", layout="centered")

st.markdown("""
    <style>
    /* Fundo e Texto Geral */
    .main { background-color: #000000; color: #ffffff; }
    
    /* Centralização do Logo e Slogan */
    .header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding-bottom: 30px;
    }
    
    .slogan {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 14px;
        color: #888;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-top: -10px;
        font-weight: 300;
    }

    /* Botões Personalizados e Animados */
    div.stButton > button {
        background: linear-gradient(145deg, #1a1a1a, #000000);
        color: #ffffff;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 20px;
        font-weight: bold;
        font-size: 16px;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.4s ease-in-out;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        width: 100%;
        margin-bottom: 10px;
    }

    div.stButton > button:hover {
        border-color: #ff4b4b;
        color: #ff4b4b;
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(255, 75, 75, 0.2);
    }

    /* Caixa de Resposta */
    .resposta-card {
        background: #0a0a0a;
        border-left: 4px solid #ff4b4b;
        padding: 25px;
        border-radius: 0 10px 10px 0;
        margin-top: 30px;
        font-size: 18px;
        line-height: 1.6;
        animation: fadeIn 1s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Lógica da IA (Secrets)
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Erro: Verifique a GROQ_API_KEY nos Secrets do Streamlit.")

def responder(tema, pergunta):
    with st.spinner("O Cavalheiro está a redigir a sua análise..."):
        try:
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "Tu és o Mentor Cavalheiro do Já Perdes. Educado, refinado e implacável. Responda com clareza cirúrgica. Começa com '⚖️ Análise de Lucidez'. Assina com o padrão da página."},
                    {"role": "user", "content": f"Tema: {tema}. Situação: {pergunta}"}
                ]
            )
            st.markdown(f"<div class='resposta-card'>{completion.choices[0].message.content}</div>", unsafe_allow_html=True)
        except:
            st.error("O Oráculo solicitou um momento de reflexão. Tente novamente.")

# 3. Cabeçalho Centralizado
st.markdown('<div class="header-container">', unsafe_allow_html=True)
# Centralizar a imagem usando colunas para garantir o alinhamento
col_img1, col_img2, col_img3 = st.columns([1, 1, 1])
with col_img2:
    st.image("LOGO JP-2025.png", use_container_width=True)
st.markdown('<p class="slogan">ontem juntos, hoje separados</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; font-weight: 300; letter-spacing: 1px;'>Painel de Diagnóstico</h2>", unsafe_allow_html=True)

# 4. Interface de Botões
col1, col2 = st.columns(2)
with col1:
    if st.button("💍 RELACIONAMENTOS"): st.session_state.modulo = "rel"
with col2:
    if st.button("💼 NEGÓCIOS"): st.session_state.modulo = "neg"

col3, col4 = st.columns(2)
with col3:
    if st.button("🔥 DISCIPLINA"): st.session_state.modulo = "dis"
with col4:
    if st.button("🎭 EGO/VITIMISMO"): st.session_state.modulo = "ego"

st.markdown("---")

# 5. Programação dos Sub-Menus
if 'modulo' in st.session_state:
    m = st.session_state.modulo
    
    if m == "rel":
        st.subheader("Pilar: Relacionamentos")
        if st.button("Porque é que ela se afastou?"): responder("Relacionamento", "Afastamento inesperado")
        if st.button("Como reagir ao fim?"): responder("Relacionamento", "Lidar com o término com dignidade")

    elif m == "neg":
        st.subheader("Pilar: Negócios")
        if st.button("O medo de falhar parou-me."): responder("Negócios", "Medo e paralisia")
        if st.button("Não sou respeitado no trabalho."): responder("Negócios", "Falta de autoridade e postura")

    elif m == "dis":
        st.subheader("Pilar: Disciplina")
        if st.button("Sei o que fazer, mas não faço."): responder("Disciplina", "Falta de execução")
        if st.button("O cansaço venceu-me."): responder("Disciplina", "Cansaço mental vs foco")

    elif m == "ego":
        st.subheader("Pilar: Ego & Ilusão")
        if st.button("Sinto-me injustiçado."): responder("Ego", "Mentalidade de vítima")
        if st.button("Preciso que me validem."): responder("Ego", "Dependência de aprovação")

# Lateral / VIP
st.sidebar.markdown("### 👑 MENTORIA")
st.sidebar.link_button("ACESSO ILIMITADO", "https://www.instagram.com/japerdes/")
