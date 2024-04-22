import streamlit as st
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter, PdfMerger


class PDFConverter:
    def __init__(self, files):
        self.buffer = BytesIO()
        self.input_files = files


    def merge_pdfs(self):
        try:
            progressbar = st.progress(0, "Merging PDFs...")

            merger = PdfMerger()
            
            for file in self.input_files:
                merger.append(file)
                
            merger.write(self.buffer)
            merger.close()
            progressbar.progress(100, "Merged successfully!")

            st.success("Merged successfully!", icon="✅")

            st.download_button(
                    label="Download PDF",
                    data=self.buffer.getvalue(),
                    file_name="merged.pdf",
                    mime="application/pdf",
                    type="primary"
                )
        except Exception as e:
            st.error(f"An error occurred: {e}", icon="❌")


    def resize_pdf(self):
        # Tamanho A4 em pontos (1 polegada = 72 pontos)
        A4_WIDTH = 595.276
        A4_HEIGHT = 841.89
        
        with open(self.input_files, 'rb') as file:
            reader = PdfReader(file)
            writer = PdfWriter()
            
            for page in reader.pages:
                # Redimensionar a página para tamanho A4
                page.scale_to(A4_WIDTH, A4_HEIGHT)
                writer.add_page(page)
                
            writer.write(self.buffer)


class main():
    def __init__(self):
        st.set_page_config(
            page_title="Convert PDFs",
            page_icon="🌐",
            layout="wide",            
        )
        st.title("PDF Converter")
        st.write("---")

        with st.container():
            st.subheader("Merge PDFs")
            files = st.file_uploader("Upload Files", type=["pdf"], accept_multiple_files=True)

            if files:
                button = st.button("Merge PDFs")

                if button:
                    convert = PDFConverter(files)
                    convert.merge_pdfs()
            st.write("---")


if __name__ == "__main__":
    main()