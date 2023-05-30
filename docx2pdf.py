import subprocess

def convert_docx_to_pdf(docx_file_path, pdf_file_path):
    subprocess.run(['unoconv', '-f', 'pdf', '-o', pdf_file_path, docx_file_path])
    print("Conversion successful!")

# Specifing the input DOCX file path
docx_path = "docx/template.docx"

# Specifing the output PDF file path and name
pdf_path = "pdfs/template.pdf"

# Convert DOCX to PDF
convert_docx_to_pdf(docx_path, pdf_path)
