import streamlit as st
import time

# Configurações iniciais
st.title('Tamagoji - Seu Gato Virtual')
st.write('Cuide do seu gato virtual e veja como ele cresce!')

# Estado do Tamagoji
if 'hunger' not in st.session_state:
    st.session_state.hunger = 100
if 'happiness' not in st.session_state:
    st.session_state.happiness = 100
if 'age' not in st.session_state:
    st.session_state.age = 0

# Função para atualizar o estado do Tamagoji
def feed_cat():
    st.session_state.hunger = min(st.session_state.hunger + 20, 100)
    st.session_state.happiness = min(st.session_state.happiness + 10, 100)

def play_with_cat():
    st.session_state.happiness = min(st.session_state.happiness + 20, 100)
    st.session_state.hunger = max(st.session_state.hunger - 10, 0)

def age_cat():
    st.session_state.age += 1
    st.session_state.hunger = max(st.session_state.hunger - 10, 0)
    st.session_state.happiness = max(st.session_state.happiness - 5, 0)

# Layout
st.sidebar.title("Ações")
if st.sidebar.button('Alimentar'):
    feed_cat()

if st.sidebar.button('Brincar'):
    play_with_cat()

if st.sidebar.button('Passar Tempo'):
    age_cat()

# Mostrar informações do Tamagoji
st.write(f"Idade: {st.session_state.age} anos")
st.write(f"Fome: {st.session_state.hunger}%")
st.write(f"Felicidade: {st.session_state.happiness}%")

# Feedback visual
if st.session_state.hunger == 0:
    st.write("Seu Tamagoji está com muita fome!")
if st.session_state.happiness == 0:
    st.write("Seu Tamagoji está triste!")

time.sleep(1)  # Aguarda 1 segundo para evitar a atualização rápida
