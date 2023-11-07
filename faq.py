import streamlit as st
from langchain.llms import OpenAI

st.title('Generador de preguntas relacionadas con el tema ingresado')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

if not openai_api_key.startswith('sk-'):
    st.warning('Por favor ingrese su llave secreta de OpenAI', icon='⚠')

if openai_api_key.startswith('sk-'):

    llm = OpenAI(
        temperature=0.5,
        model_name='gpt-3.5-turbo',
        openai_api_key=openai_api_key,
        max_tokens=150
    )
    topic = st.text_input("Escribe tu topic:")
    
    plantilla = """
    Eres un experto en {topic}, ¿que información buscaría alguien que esté interesado en {topic}? como experto en {topic}, teniendo en cuenta la intención de búsqueda muéstrame las 5 mejores preguntas relacionadas al tema ingresado.
    """ 

    respuesta = llm(plantilla.format(topic=topic))
    st.write(respuesta)
