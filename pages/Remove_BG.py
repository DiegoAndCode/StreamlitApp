import streamlit as st
from PIL import Image
from rembg import remove

class BackgroundRemove:
    def __init__(self, image):
        self.image = image
        self.col1, self.col2 = st.columns(2)

    def remove_bg(self, image_to_remove):
        bytes_data = Image.open(image_to_remove)
        output = remove(bytes_data)
        self.col2.title('Output Image')
        self.col2.image(output)

    def upload_image(self):
            self.col1.title('Original Image')
            self.col1.image(self.image, width=300)
            if self.col1.button('Remove Background'):
                self.remove_bg(self.image)

class main():
    def __init__(self):
        st.set_page_config(
            page_title="Remove BG",
            page_icon="🌐",
            layout="wide",
        )
        st.title("Remove BG")
        st.write("---")

        with st.container():            
            st.subheader("Remove Background from Image")
            image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

            if image is not None:
                remover = BackgroundRemove(image)
                remover.upload_image()

            st.write("---")


if __name__ == "__main__":
    main()