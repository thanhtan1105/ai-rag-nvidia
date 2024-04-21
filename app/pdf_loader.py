import os
from pdfminer.high_level import extract_text


class PDFLoader:
    @staticmethod
    def extract_text_from_pdf(path):
        return extract_text(path)
