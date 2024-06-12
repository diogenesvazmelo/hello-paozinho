import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
"""
# Meu Coração para a Dona Pão!
"""
# Função para desenhar um coração
def plot_heart(ax, scale=1, color='red'):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    ax.plot(scale * x, scale * y, color=color)
    ax.fill(scale * x, scale * y, color=color, alpha=0.3)

# Título do aplicativo
st.title(" ")

# Texto romântico
text_placeholder = st.empty()

# Parâmetros variáveis
# scale = st.slider("Tamanho do Coração", 0.5, 2.0, 1.0, 0.1)
scale = 1
# color = st.color_picker("Cor do Coração", "#FF0000")
color = "#FF0000"
# animate = st.checkbox("Animar Texto")
animate = True

# Desenho do coração
fig, ax = plt.subplots(figsize=(5, 5))
plot_heart(ax, scale=scale, color=color)
ax.axis('equal')
ax.axis('off')
st.pyplot(fig)

# Configura a animação do texto
if animate:
    messages = [" ", "", " ", " ", " ", " "
                "Eu", "te", "amo", "muito", "meu", "Pãozinho"
                , " ", "🍞❤️🥖", "🍞❤️🥖", "🍞❤️🥖", "🍞❤️🥖", "🍞❤️🥖"
                , "🍞❤️🥖", "🍞❤️🥖", "🍞❤️🥖", "🍞❤️🥖", "🍞❤️🥖", "🍞❤️🥖"
                , " ", "", " ", " ", " ", " "
                
                
                ]
    while True:
        for message in messages:
            text_placeholder.write(f"<h1 style='text-align: center; color: {color};'>{message}</h1>", unsafe_allow_html=True)
            time.sleep(0.685)
else:
    text_placeholder.write("<h1 style='text-align: center;'>Este coração é para você, meu amor! ❤️</h1>", unsafe_allow_html=True)