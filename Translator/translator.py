# Import required libraries
from openai import OpenAI

client = OpenAI()
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv


# Define the translation function
def translate_text(text, source_language, target_language):
    prompt = f"Translate the following '{source_language}' text to '{target_language}': {text}"

    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that translates text."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=150,
    n=1,
    stop=None,
    temperature=0.5)

    translation = response.choices[0].message.content.strip()
    return translation

def on_translate_click(text_input, source_lang_input, target_lang_input, result_label):
    text = text_input.get()
    source_language = source_lang_input.get()
    target_language = target_lang_input.get()

    translated_text = translate_text(text, source_language, target_language)
    result_label.config(text=translated_text)

def create_app():
    app = tk.Tk()
    app.title("Multilingual Translation Tool")

    text_label = ttk.Label(app, text="Text:")
    text_label.grid(column=0, row=0)
    text_input = ttk.Entry(app)
    text_input.grid(column=1, row=0)

    source_lang_label = ttk.Label(app, text="Source Language:")
    source_lang_label.grid(column=0, row=1)
    source_lang_input = ttk.Entry(app)
    source_lang_input.grid(column=1, row=1)

    target_lang_label = ttk.Label(app, text="Target Language:")
    target_lang_label.grid(column=0, row=2)
    target_lang_input = ttk.Entry(app)
    target_lang_input.grid(column=1, row=2)

    translate_button = ttk.Button(app, text="Translate", command=lambda: on_translate_click(text_input, source_lang_input, target_lang_input, result_label))
    translate_button.grid(column=1, row=3)

    result_label = ttk.Label(app, text="")
    result_label.grid(column=0, row=4, columnspan=2)
    app.mainloop()


def main():
    load_dotenv()
    create_app()

if __name__ == '__main__':
    main()
