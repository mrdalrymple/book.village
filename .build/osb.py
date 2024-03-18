from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Open the text file
with open('book.txt', 'r', encoding="utf-8") as file:
    text = file.read()

# Create a PDF document
doc = SimpleDocTemplate('output.pdf', pagesize=letter)

# Create a list of flowable objects (Paragraphs)
styles = getSampleStyleSheet()
flowables = []
flowables.append(Paragraph(text, styles['BodyText']))

# Build the PDF
doc.multiBuild(flowables)
