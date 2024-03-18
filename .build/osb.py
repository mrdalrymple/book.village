from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


#def way_one(file)

# Create a PDF document
doc = SimpleDocTemplate('output.pdf', pagesize=letter)

# Create a list of flowable objects (Paragraphs)
styles = getSampleStyleSheet()
flowables = []

# Open the text file
last_line = None
with open('book.txt', 'r', encoding="utf-8") as file:
    #text = file.read()
    text = []
    current_paragraph = None
    for line in file.readlines():
        if last_line is None:
            text = []
        elif last_line == "\n":
            flowables.append(Paragraph("\n".join(text), styles['BodyText']))
            text = []

        text.append(line)
        last_line = line

if text:
    flowables.append(Paragraph("\n".join(text), styles['BodyText']))

#flowables.append(Paragraph(text, styles['BodyText']))

# Build the PDF
doc.multiBuild(flowables)
