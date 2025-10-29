import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3, col4 = st.columns(4)

with col1:
 
 st.subheader("Mi Primera App")
 image = Image.open('Mi_primera_app.png')
 st.image(image, width=190)
 st.write("") 
 url = "https://wt9udcox4gbjdexwnk7xek.streamlit.app/"
 st.write(f"Mi primera App: [Enlace]({url})")

 st.subheader("Uso de textblob")
 image = Image.open('reconocimento_emociones.png')
 st.image(image, width=200)
 st.write(".") 
 url = "https://8mcuwxfcrzqdgw54y7usty.streamlit.app/"
 st.write(f"Uso de textblob: [Enlace]({url})")

 st.subheader("Identifica la función de la flor")
 image = Image.open('Identifica_la_función_de_la_flor.png')
 st.image(image, width=200)
 st.write("") 
 url = "https://visionapp-gdrsrcspkrgqh674jpjxtw.streamlit.app/"
 st.write(f"Identifica la función de la flor: [Enlace]({url})")

with col2: 
 st.subheader("Detección de Objetos en Imágenes")
 image = Image.open('Detección_de_Objetos_en_Imágenes.png')
 st.image(image, width=200)
 st.write("") 
 url = "https://yolov5-ijocake9ej9sfaaz8kpzn9.streamlit.app/"
 st.write(f"Detección de Objetos en Imágenes: [Enlace]({url})")

 st.subheader("INTERFACES MULTIMODALES")
 image = Image.open('Control_Voz.png')
 st.image(image, width=190)
 st.write("") 
 url = "https://ctrlvoice-dzmug9tlghbiwrekshhxje.streamlit.app/"
 st.write(f"INTERFACES MULTIMODALES: [Enlace]({url})")

 st.subheader("Tablero para dibujo")
 image = Image.open('Tablero_para_dibujo.png')
 st.image(image, width=200)
 st.write(".") 
 url = "https://tablero-herwgpfoxptbhpurfgt2yd.streamlit.app/"
 st.write(f"Tablero para dibujo: [Enlace]({url})")


with col3: 
 st.subheader("Generación Aumentada por Recuperación")
 image = Image.open('Generación_Aumentada_por_Recuperación.png')
 st.image(image, width=190)
 st.write("") 
 url = "https://chatpdf-3uaru8k8a3zdfobuxtzz4k.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Reconocimiento óptico de Caracteres")
 image = Image.open('Reconocimiento_Óptico_de_Caracteres.png')
 st.image(image, width=200)
 st.write("") 
 url = "https://zxvbun6rirsxo3hdpxhfyh.streamlit.app/"
 st.write(f"Reconocimiento óptico de Caracteres: [Enlace]({url})")
 
 st.subheader("Demo TF-IDF en Español")
 image = Image.open('Demo_TF-IDF _en_Español.png')
 st.image(image, width=190)
 st.write("") 
 url = "https://tdfesp-p3ukwbfgwwaniwdcne67ua.streamlit.app/"
 st.write(f"Demo TF-IDF en Español: [Enlace]({url})")


with col4: 
 st.subheader("Traductor")
 image = Image.open('Traductor.png')
 st.image(image, width=190)
 st.write("") 
 url = "https://traductor-jjpi7chz6zwqn6hfuzvnht.streamlit.app/"
 st.write(f"Traductor: [Enlace]({url})")

 st.subheader("Conversión de Texto a Audio")
 image = Image.open('Conversión_de_Texto_a_Audio.png')
 st.image(image, width=200)
 st.write("") 
 url = "https://uz4btakkmemzfv38dfgm3g.streamlit.app/"
 st.write(f"Conversión de Texto a Audio: [Enlace]({url})")
 
 st.subheader("Tablero Inteligente")
 image = Image.open('Tablero_Inteligente.png')
 st.image(image, width=190)
 st.write("") 
 url = "https://drawrecog-vyroxqycvvuay4ha28xp5t.streamlit.app/"
 st.write(f"Tablero Inteligente: [Enlace]({url})")


