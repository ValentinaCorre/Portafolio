import streamlit as st
from PIL import Image
st.title("Aplicaciones de Streamlit.")

with st.sidebar:
  st.subheader("Aplicaciones de streamlit.")
  parrafo = (
    "Los aprendizajes realizados en computacion avanzada "
    "se pueden ver reflejados en las apps que se encuentran en esta pagina "
   
  )
  st.write(parrafo)

url_streamlit="https://share.streamlit.io/"
st.subheader("En el siguiente enlace puedes encontrar las apps hechas en streamlit")
st.write(f"Enlace para apps: [Enlace]({url_streamlit})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("App de frutas")
 image = Image.open('Fruta Matcher.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicaciones creadas en streamlit") 
 url = "https://clasfruta-j3r3mywm6zkywfuynvlsej.streamlit.app/"
 st.write(f"App #1: [Enlace]({url})")

 st.subheader("Gradiente")
 image = Image.open('Gradiente.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://parametros-19-cshgqtp5eacijhvhn5v7n9.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("DETECTOR DE ANOMALIAS")
 image = Image.open('ANOMALIAS.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://colab24a-wdmy2rkm9sndjvfsr9mg6y.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductorw.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Análisis de Datos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://dataagente.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


