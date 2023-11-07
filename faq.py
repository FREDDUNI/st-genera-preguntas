#get a token: https://platform.openai.com/account/api-keys

from langchain.llms import OpenAI
from getpass import getpass
from langchain.prompts import PromptTemplate
import streamlit as st

st.title('Generador de preguntas relacionadas con el tema ingresado')
st.caption('Introduzca en la consola la clave API como password antes y luego de ingresar el tema')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

llm = OpenAI(
    temperature=0.5,
    model_name='gpt-3.5-turbo',
    openai_api_key=openai_api_key,
    max_tokens=150
)

plantilla = """
Eres un experto en {topic}, ¿que información buscaría alguien que esté interesado en {topic}? como experto en {topic}, teniendo en cuenta la intención de búsqueda muéstrame las 5 mejores preguntas relacionadas al tema ingresado.
""" 

pregunta =st.text_input("Escribe tu topic:")
topic = pregunta

respuesta = llm(plantilla.format(topic=topic))
st.write(respuesta)
