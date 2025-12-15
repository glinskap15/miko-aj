import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def draw_santa_matplotlib():
    """
    Rysuje prosty, stylizowany obraz Mikołaja za pomocą Matplotlib.
    Zwraca obiekt figure (fig) z Matplotlib.
    """
    
    # 1. Konfiguracja płótna
    fig, ax = plt.subplots(figsize=(4, 5)) 
    
    # Usuwanie osi i tła
    ax.set_facecolor('#B0E0E6') # Jasnoniebieskie tło
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')
    
    # --- Kolory ---
    RED = '#D93025'
    WHITE = '#FFFFFF'
    SKIN = '#F2C8AD'
    BLACK = '#000000'
    
    # --- Rysowanie Elementów ---

    # 2. Twarz (Koło)
    face = plt.Circle((0, 0.4), 0.35, color=SKIN)
    ax.add_artist(face)
    
    # 3. Brody (Duży owal/eliptyczny kształt)
    # Przybliżony owal brody
    beard_body = plt.Rectangle((-0.45, -1.0), 0.9, 1.0, color=WHITE)
    ax.add_artist(beard_body)
    
    # Dolna krawędź brody (półkole)
    beard_bottom = plt.Arc((0, -1.0), 0.9, 0.9, angle=0, theta1=0, theta2=180, color=WHITE, linewidth=50)
    ax.add_artist(beard_bottom)
    
    # 4. Kapelusz (Trójkąt i białe elementy)
    # Czerwony Kapelusz (Trójkąt)
    hat_x = [-0.6, 0.6, 0]
    hat_y = [0.8, 0.8, 1.4]
    ax.fill(hat_x, hat_y, color=RED)
    
    # Biały Brzeg Kapelusza (Prostokąt)
    brim = plt.Rectangle((-0.65, 0.75), 1.3, 0.2, color=WHITE)
    ax.add_artist(brim)
    
    # Pompon (Małe koło)
    pom_pom = plt.Circle((0, 1.4), 0.1, color=WHITE, edgecolor=BLACK, linewidth=0.5)
    ax.add_artist(pom_pom)
    
    # 5. Oczy (Małe czarne koła)
    eye1 = plt.Circle((-0.15, 0.45), 0.05, color=BLACK)
    eye2 = plt.Circle((0.15, 0.45), 0.05, color=BLACK)
    ax.add_artist(eye1)
    ax.add_artist(eye2)
    
    # 6. Wąsy (Proste łuki)
    mustache_left = plt.Arc((-0.1, 0.25), 0.3, 0.2, angle=0, theta1=0, theta2=180, color=WHITE, linewidth=3, solid_capstyle='round')
    mustache_right = plt.Arc((0.1, 0.25), 0.3, 0.2, angle=0, theta1=0, theta2=180, color=WHITE, linewidth=3, solid_capstyle='round')
    ax.add_artist(mustache_left)
    ax.add_artist(mustache_right)

    return fig

# --- Interfejs Użytkownika Streamlit ---

st.title("🎅 Generator Mikołaja (Streamlit + Matplotlib)")
st.caption("Obraz Mikołaja generowany dynamicznie za pomocą wykresów Matplotlib.")

# Przycisk do generowania obrazu
if st.button("Wygeneruj Mikołaja"):
    
    # Generowanie obiektu Matplotlib Figure
    santa_figure = draw_santa_matplotlib()
    
    # Wyświetlanie obrazu w Streamlit
    # st.pyplot() automatycznie obsługuje obiekty Figure Matplotlib
    st.pyplot(santa_figure)
    
    # Opcja pobrania obrazu jest bardziej skomplikowana z Matplotlib w Streamlit,
    # ale można ją zaimplementować, zapisując figurę do bufora.
    
    buffer = io.BytesIO()
    santa_figure.savefig(buffer, format="png")
    
    st.download_button(
        label="Pobierz obraz jako PNG",
        data=buffer.getvalue(),
        file_name="mikolaj_matplotlib.png",
        mime="image/png"
    )
