import PyPDF2

# Crea un archivo PDF en blanco
pdf_file = PyPDF2.PdfWriter()

# Agrega una página en blanco al archivo PDF
pdf_file.add_blank_page(width=612, height=792)

# Guarda el archivo PDF
with open('archivo_en_blanco.pdf', 'wb') as f:
    pdf_file.write(f)