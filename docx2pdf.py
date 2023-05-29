import os
from docxtpl import DocxTemplate
import subprocess
from docx import Document

def convert_docx_to_pdf(docx_file, pdf_file):
    # Load the DOCX document
    doc = Document(docx_file)

    # Create a temporary file for the intermediate ODT format
    odt_file = os.path.splitext(docx_file)[0] + '.odt'
    doc.save(odt_file)

    # Use unoconv to convert ODT to PDF
    subprocess.run(['unoconv', '-f', 'pdf', '-o', os.path.dirname(pdf_file), odt_file])

    # Remove the intermediate ODT file
    os.remove(odt_file)

# Usage example
docx_file = 'template.docx'  # Replace with the path to your DOCX file
pdf_file = 'output.pdf'   # Replace with the desired output PDF path

convert_docx_to_pdf(docx_file, pdf_file)
print('Conversion complete. PDF file:', pdf_file)