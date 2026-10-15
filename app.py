import streamlit as st
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Portal do Universo: Curiosidades & Atualidades", 
    page_icon="🌌", 
    layout="centered"
)

# Estilização visual e cabeçalho
st.title("✨ Portal do Universo: Curiosidades & Atualidades")
st.markdown("Um espaço dedicado a explorar os mistérios do cosmos, astrofísica e acompanhar as principais novidades astronômicas.")

# Base inicial de postagens (Curiosidades e Atualidades de exemplo)
if "atualidades" not in st.session_state:
    st.session_state.atualidades = [
        {
            "titulo": "🔭 Novas observações do Telescópio James Webb (JWST)",
            "data": "14/10/2026",
            "texto": "Dados recentes obtidos pelo JWST continuam a mapear galáxias distantes no infravermelho, revelando detalhes fascinantes sobre a evolução do universo primordial e estruturas estelares antigas."
        },
        {
            "titulo": "🌀 A Física dos Buracos Negros em Rotação",
            "data": "10/10/2026",
            "texto": "Diferente dos buracos negros estáticos de Schwarzschild, os buracos negros em rotação (geometria de Kerr) arrastam o próprio tecido do espaço-tempo ao seu redor através de um fenômeno conhecido como 'frame-dragging'."
        },
        {
            "titulo": "🌟 A Escala do Cosmos",
            "data": "05/10/2026",
            "texto": "A luz que sai da estrela mais próxima do nosso sistema solar (Alpha Centauri) leva pouco mais de 4 anos para chegar até nós. Olhar para o espaço profundo é, literalmente, olhar para o passado!"
        }
    ]

# --- PAINEL LATERAL: ADICIONAR NOVAS ATUALIDADES ---
st.sidebar.header("📝 Adicionar Nova Postagem")
st.sidebar.markdown("Use este painel para publicar novas curiosidades ou notas diretamente no seu site.")

with st.sidebar.form("form_postagem", clear_on_submit=True):
    titulo_input = st.text_input("Título da Atualidade")
    texto_input = st.text_area("Texto / Descrição")
    botao_enviar = st.form_submit_button("Publicar no Site")
    
    if botao_enviar:
        if titulo_input and texto_input:
            data_hoje = datetime.now().strftime("%d/%m/%Y")
            # Adiciona a nova postagem no topo da lista
            st.session_state.atualidades.insert(0, {
                "titulo": titulo_input,
                "data": data_hoje,
                "texto": texto_input
            })
            st.sidebar.success("Postagem publicada com sucesso!")
        else:
            st.sidebar.error("Por favor, preencha o título e o texto.")

st.markdown("---")
st.header("🚀 Mural de Fatos e Atualidades Cósmicas")

# Exibição iterativa de todas as atualidades cadastradas
for post in st.session_state.atualidades:
    with st.container():
        st.subheader(post["titulo"])
        st.caption(f"📅 Publicado em: {post['data']}")
        st.write(post["texto"])
        st.markdown("---")

# Rodapé simples
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 14px;'>Atualizado regularmente com novas descobertas e curiosidades astronômicas 🌌</p>", 
    unsafe_allow_html=True
)
