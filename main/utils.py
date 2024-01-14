import pdfplumber


def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        pages = [page.extract_text() for page in pdf.pages]
    text = "\n".join(filter(None, pages))
    return text
