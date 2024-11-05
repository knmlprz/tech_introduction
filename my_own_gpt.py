import os
import gradio as gr
from transformers import pipeline

if not os.path.exists('./output'):
    os.makedirs('./output')

generator = pipeline('text-generation', model='distilgpt2')

def generate_text(prompt):
    result = generator(prompt, max_length=50, num_return_sequences=1)
    text = result[0]['generated_text']
    with open('./output/daniel_k.md', 'w', encoding='utf-8') as f:
        f.write(text)

    return text
iface = gr.Interface(fn=generate_text, inputs="text", outputs="text", title="Mały Model Językowy")
iface.launch()
