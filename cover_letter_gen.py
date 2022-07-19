import json
from string_interpolate import interpolate
from fpdf import FPDF

with open('cover_letter_gen.json', 'r') as f:
    variables = json.load(f)
    text = interpolate(variables)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(0, 20, txt="Cover Letter", ln=1, align="C")
    pdf.set_auto_page_break(auto=True, margin = 0.0)

    for line in text.splitlines():
      print(line)
      line
      pdf.set_font("Arial", size=8)
      pdf.multi_cell(0,5, txt=line, border=0, align="J", fill=False)
    pdf.output("./cover_letters/cover_letter.pdf")

    # pdf.output("./cover_letters/cover_letter.pdf")