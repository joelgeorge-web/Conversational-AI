import streamlit as st
import os
import fitz  # PyMuPDF library

current_dir = os.getcwd()
save_file_name = None  # Initialize the global variable

def streamlit_file_loader():
    global save_file_name  # Declare the global variable
    st.title("PDF Reader")
    st.write("Upload a PDF file to read its content.")
    uploaded_file = st.file_uploader("Choose a file to upload", type=['txt', 'pdf', 'docx'])
    
    if uploaded_file is not None:
        filename = uploaded_file.name
        safe_filename = os.path.splitext(filename)[0] + "_" + os.path.splitext(filename)[1]
        save_file_name = os.path.join(current_dir, safe_filename)

        try:
            with open(save_file_name, "wb") as buffer:
                buffer.write(uploaded_file.getbuffer())
            st.success(f"Successfully uploaded and saved {filename}")
        except Exception as e:
            st.error(f"Error saving file: {e}")

def read_pdf():
    if save_file_name and save_file_name.lower().endswith('.pdf') or save_file_name and save_file_name.lower().endswith('.txt'):
        try:
            pdf_document = fitz.open(save_file_name)
            num_pages = len(pdf_document)
            for page_num in range(num_pages):
                page = pdf_document[page_num]
                text = page.get_text()
                st.write(f"Page {page_num + 1}:\n{text}")
            pdf_document.close()
        except Exception as e:
            st.error(f"Error reading PDF: {e}")
    else:
        st.warning("No file uploaded or incorrect file format.")

def main():
    streamlit_file_loader()
    read_pdf()

if __name__ == "__main__":
    main()
