from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text

def load_image(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")



def main():
    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    st.set_page_config(page_title="Gemini Image Extractor")

    st.header("Generative AI Image Extractor")

    with st.sidebar:
        st.subheader("Add documents")
        uploaded_images = st.file_uploader("Upload your images here", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

        if uploaded_images is not None:
            st.session_state['uploaded_image'] = uploaded_images

        if 'uploaded_image' in st.session_state and st.session_state['uploaded_image'] is not None:
            image = Image.open(st.session_state['uploaded_image'])
            st.sidebar.image(image, caption="Uploaded Image.", use_column_width=True)
            st.session_state['image_data'] = load_image(st.session_state['uploaded_image'])

    input_text = st.text_input("Ask a question: ", key="input")

    if input_text and 'image_data' in st.session_state and st.session_state['image_data']:
        input_prompt = """
            You are an expert in image extraction.
            You will receive input images  &
            you will have to answer questions based on the input image
            """
        response = get_gemini_response(input_prompt, st.session_state['image_data'], input_text)
        st.subheader("Response:")
        st.write(response)


if __name__ == '__main__':
    main()