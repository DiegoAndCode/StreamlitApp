import streamlit as st
from PIL import Image
from rembg import remove

def remove_bg(image, widget):
    bytes_data = Image.open(image)
    output = remove(bytes_data)
    widget.title('Output Image')
    widget.image(output)


st.title("Remove Background from Image")
image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

col1, col2 = st.columns(2)

if image is not None:
    col1.title('Original Image')
    col1.image(image, width=300)
    col1.button('Remove Background', on_click=remove_bg, args=(image, col2))
    