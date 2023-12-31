import streamlit as st
from PIL import Image
import rarfile
import zipfile
import os

st.title("Comic Book Reader App")

uploaded_file = st.file_uploader("Upload a comic book file", type=["cbr", "cbz"])

if uploaded_file is not None:
    temp_dir = st._get_session().__dict__.setdefault('temp_dir', None)
    if temp_dir is None:
        temp_dir = st._get_session().temp_dir = os.path.join(st._config.session_directory, 'temp')
        os.makedirs(temp_dir, exist_ok=True)

    with open(os.path.join(temp_dir, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.read())

    if uploaded_file.name.lower().endswith('.cbr'):
        with rarfile.RarFile(os.path.join(temp_dir, uploaded_file.name)) as archive:
            archive.extractall(temp_dir)
    elif uploaded_file.name.lower().endswith('.cbz'):
        with zipfile.ZipFile(os.path.join(temp_dir, uploaded_file.name)) as archive:
            archive.extractall(temp_dir)

    extracted_images = [os.path.join(temp_dir, filename) for filename in os.listdir(temp_dir) if filename.lower().endswith(('jpg', 'jpeg', 'png'))]

    if extracted_images:

        images = [Image.open(image) for image in extracted_images]
        total_pages = len(images)


        st.sidebar.title("Navigation")
        page_number = st.sidebar.number_input("Go to page", value=1, min_value=1, max_value=total_pages)

        st.image(images[page_number - 1], caption=f"Page {page_number}/{total_pages}", use_column_width=True)

        col1, col2, col3 = st.beta_columns(3)
        if col2.button("Previous Page", key="prev"):
            page_number = max(1, page_number - 1)
        if col2.button("Next Page", key="next"):
            page_number = min(total_pages, page_number + 1)

        st.image(images[page_number - 1], caption=f"Page {page_number}/{total_pages}", use_column_width=True)
