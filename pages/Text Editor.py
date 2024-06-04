import streamlit as st
import streamlit.components.v1 as components

def ckeditor_editor():
    ckeditor_code = """
    <script src="https://cdn.ckeditor.com/4.16.2/standard/ckeditor.js"></script>
    <textarea id="editor1">Your text here...</textarea>
    <script>
        CKEDITOR.replace('editor1');
        CKEDITOR.instances.editor1.on('change', function() {
            var content = CKEDITOR.instances.editor1.getData();
            var editor_content = document.getElementById('editor_content');
            editor_content.value = content;
        });
    </script>
    <textarea id="editor_content" style="display:none"></textarea>
    """
    return ckeditor_code

def main():
    st.title("Dinamic Text Editor")

    # Exibir o CKEditor
    components.html(ckeditor_editor(), height=315)


if __name__ == "__main__":
    main()
