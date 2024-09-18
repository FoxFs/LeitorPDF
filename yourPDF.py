import fitz #função da biblioteca PyMuPDF

documento = "YourPDFhere" #coloque apenas o nome do arquivo com PDF no final.
doc = fitz.open(documento)

texto = ""
for pagina in range(doc.paginas_count):
    paginas = doc.load_page(pagina)
    texto += paginas.get_text()

print(f"Seu texto aqui: ")
print()
print(texto)