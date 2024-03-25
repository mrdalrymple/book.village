from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('arial', size=11)
with open("book.txt", "r", encoding="utf-8") as f:
    for l in f.readlines():
        pdf.cell(text=l, new_x="LMARGIN", new_y="NEXT")
#pdf.cell(text="hello world")
pdf.output("hello_world.pdf")
