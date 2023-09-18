from docx import Document
from docx.shared import Pt

arquivoWord = Document("D:\\Usuários\\Natalia\\Desktop\\RPA\\Word\\Certificado1.docx")

estilo = arquivoWord.styles["Normal"]


for paragrafo in arquivoWord.paragraphs:
    if "@nome" in paragrafo.text:
        paragrafo.text = "Berenice Rosa Santos"
        fonte = estilo.font
        fonte.name = "Calibri (Corpo)"
        fonte.size = Pt(24)

arquivoWord.save('Berenice Rosa Santos.docx')


