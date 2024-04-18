import streamlit as st
from PIL import Image
from rembg import remove

class BackgroundRemover:
    def __init__(self):
        self.image = None
        self.col1, self.col2 = st.columns(2)

    def remove_bg(self, image):
        bytes_data = Image.open(image)
        output = remove(bytes_data)
        self.col2.title('Output Image')
        self.col2.image(output)

    def upload_image(self):
        st.title("Remove Background from Image")
        image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

        if image is not None:
            self.col1.title('Original Image')
            self.col1.image(image, width=300)
            if self.col1.button('Remove Background'):
                self.remove_bg(image)

def main():
    remover = BackgroundRemover()
    remover.upload_image()

if __name__ == "__main__":
    main()