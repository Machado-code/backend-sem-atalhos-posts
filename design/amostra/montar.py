"""Monta a amostra grátis do Dev Raiz.

Uso: python3 montar.py <guia.pdf> <pasta> <saida.pdf>
Junta capa.html, as páginas 1 a 9 do guia (a 9 só até o fim da seção 1.6) (com a assinatura da página 1 coberta)
e fim.html num único PDF.
"""
import io
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas

guia, pasta, saida = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])


def html_para_pdf(html: Path, destino: Path) -> None:
    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pagina = nav.new_page()
        pagina.goto(html.resolve().as_uri())
        pagina.pdf(path=str(destino), width="8.5in", height="11in", print_background=True)
        nav.close()


capa_pdf, fim_pdf = pasta / "capa.pdf", pasta / "fim.pdf"
html_para_pdf(pasta / "capa.html", capa_pdf)
html_para_pdf(pasta / "fim.html", fim_pdf)

# Faixa branca sobre a data e a assinatura da página 1, com o selo da amostra no lugar.
buf = io.BytesIO()
c = canvas.Canvas(buf, pagesize=(612, 792))
c.setFillColor(white)
c.rect(44, 654, 230, 28, stroke=0, fill=1)
c.setFillColor(HexColor("#5F6B7A"))
c.setFont("Helvetica", 9)
c.drawString(54, 664, "Amostra grátis  |  sematalhos.dev.br")
c.save()
faixa = PdfReader(io.BytesIO(buf.getvalue())).pages[0]

# Página 9: fica só o fim da seção 1.6; a atividade dos 10 bugs é coberta.
buf2 = io.BytesIO()
c2 = canvas.Canvas(buf2, pagesize=(612, 792))
c2.setFillColor(white)
c2.rect(40, 45, 532, 617, stroke=0, fill=1)
c2.setFillColor(HexColor("#D7263D"))
c2.setFont("Helvetica-Oblique", 12)
c2.drawString(58, 620, "Aqui começa a seção 1.7: a caça a 10 bugs reais, com gabarito comentado.")
c2.drawString(58, 602, "Ela continua no pacote completo, em sematalhos.dev.br.")
c2.save()
corte = PdfReader(io.BytesIO(buf2.getvalue())).pages[0]

origem = PdfReader(str(guia))
saida_pdf = PdfWriter()
saida_pdf.append(str(capa_pdf))
for i in range(9):
    pagina = origem.pages[i]
    if i == 0:
        pagina.merge_page(faixa)
    if i == 8:
        pagina.merge_page(corte)
    saida_pdf.add_page(pagina)
saida_pdf.append(str(fim_pdf))
saida_pdf.add_metadata({"/Title": "Amostra grátis do Dev Raiz", "/Author": "Sem Atalhos"})
with open(saida, "wb") as f:
    saida_pdf.write(f)
print(f"{saida}: {len(saida_pdf.pages)} páginas")

# O texto coberto continua no PDF por baixo da faixa branca. Para que ele não possa ser
# copiado, as duas páginas com cobertura viram imagem.
import subprocess
import tempfile

import img2pdf

with tempfile.TemporaryDirectory() as tmp:
    substitutas = {}
    for indice in (1, 9):  # página 1 e página 9 do guia, dentro da amostra
        prefixo = Path(tmp) / f"p{indice}"
        subprocess.run(["pdftoppm", "-f", str(indice + 1), "-l", str(indice + 1), "-r", "200",
                        "-png", "-singlefile", str(saida), str(prefixo)], check=True)
        layout = img2pdf.get_layout_fun((img2pdf.in_to_pt(8.5), img2pdf.in_to_pt(11)))
        dados = img2pdf.convert(str(prefixo) + ".png", layout_fun=layout)
        substitutas[indice] = PdfReader(io.BytesIO(dados)).pages[0]
    atual = PdfReader(str(saida))
    final = PdfWriter()
    for i, pagina in enumerate(atual.pages):
        final.add_page(substitutas.get(i, pagina))
    final.add_metadata({"/Title": "Amostra grátis do Dev Raiz", "/Author": "Sem Atalhos"})
    with open(saida, "wb") as f:
        final.write(f)
print("páginas com cobertura convertidas em imagem")
