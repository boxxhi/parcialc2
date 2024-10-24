from pypdf import PdfReader, PdfWriter

reader = PdfReader('./Recetario.pdf')

# Conocer el total de paginas del pdf
page_n = len(reader.pages)

print(page_n)

# Extrear texto
page = reader.pages[4]
page_text = page.extract_text()

print(page_text)

# Enciptacion

writer = PdfWriter(clone_from=reader)
writer.encrypt('messi')

with open("encrypted-pdf.pdf", "wb") as f:
    writer.write(f)