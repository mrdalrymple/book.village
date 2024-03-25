from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_LEFT
#from reportlab.lib.units import inch


INPUT_FILENAME = "book.txt"
OUTPUT_FILENAME = "book.pdf"

#def way_one(file)

# Create a PDF document
doc = SimpleDocTemplate(OUTPUT_FILENAME, pagesize=letter)

# Create a list of flowable objects (Paragraphs)
styles = getSampleStyleSheet()
flowables = []

leading_double_space = 24
leading_single_space = 12

# Note: if wanting to double spaced or something... two spacers would be needed (paragraph I think uses spacers for it's line spacing)
blank_line = Spacer(1, 12)  # 1 inch wide, 12 points tall
#blank_line = Spacer(1, leading)

# Open the text file
last_line = None
with open(INPUT_FILENAME, 'r', encoding="utf-8") as file:
    title_style = ParagraphStyle('BodyText', alignment=TA_RIGHT, leading=leading_single_space)
    paragraph_style = ParagraphStyle('BodyText', alignment=TA_JUSTIFY, leading=leading_double_space)

    prev_line = None
    count = 1
    debug = False
    # debug = True
    selected_style = paragraph_style
    paragraph = None


    for line in file.readlines():
        flowable = None
        if debug:
            if count > 3:
                break
            print(f"{count}> ------ ")
            print(f"{count}> LINE: '{line}'")
            print(f"{count}> PARA: '{paragraph}'")




        if paragraph is None:
            paragraph = line + "\n"
        else:
            paragraph = paragraph + line + "\n"

        #paragraph = paragraph + "\n"
        stripped_line = line.strip().lower()
        if stripped_line == "[title]":
            selected_style = title_style
        elif stripped_line == "[paragraph]":
            selected_style = paragraph_style
        elif stripped_line == "{pagebreak}":
            flowable = PageBreak()
            pass
        elif line == "\n":
            flowable = blank_line
            pass
        else:
            flowable = Paragraph(paragraph, selected_style)

        if flowable:
            flowables.append(flowable)

        paragraph = None

        prev_line = line
        count = count + 1

    if paragraph:
        flowable = Paragraph(paragraph, paragraph_style)
        flowables.append(flowable)


# Build the PDF
doc.multiBuild(flowables)
