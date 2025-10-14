import ipywidgets as widgets;
from langchain_groq import ChatGroq
import os
import getpass
from IPython.display import display

topic = widgets.Text(
    description = 'Tema:',
    placeholder = 'Ex: saúde mental, alimentação saudável, prevenção, etc.'
)

w_dropdown = '250px'

platform = widgets.Dropdown(
    options = ['Instagram', 'Facebook', 'LinkedIn', 'Blog', 'E-mail'],
    description = 'Plataforma',
    layout = widgets.Layout(width = w_dropdown)
)

tone = widgets.Dropdown(
    options=['Normal', 'Informativo', 'Inspirador', 'Urgente', 'Informal'],
    description='Tom:',
    layout=widgets.Layout(width=w_dropdown)
)

length = widgets.Dropdown(
    options=['Curto', 'Médio', 'Longo'],
    description='Tamanho:',
    layout=widgets.Layout(width=w_dropdown)
)

audience = widgets.Dropdown(
    options=['Geral', 'Jovens adultos', 'Famílias', 'Idosos', 'Adolescentes'],
    description='Público-alvo:',
    layout=widgets.Layout(width=w_dropdown)
)

cta = widgets.Checkbox(
    value = False,
    description = 'Incluir CTA'
)

hashtags = widgets.Checkbox(
    value=False,
    description='Retornar Hashtags',
)

keywords = widgets.Textarea(
  description = 'Palavra-chave (SEO)',
  placeholder = 'Ex: bem-estar, medicina preventiva...',
  layout = widgets.Layout(width='500px', height='50px')
)

display(topic, platform, tone, length, audience, cta, hashtags, keywords)

generate_button = widgets.Button(
  description = 'Gerar conteúdo'
)

display(generate_button)

output = widgets.Output()

def generate_result(b):
  with output:
    output.clear_output()
    print("OK!")

generate_button.on_click(generate_result)