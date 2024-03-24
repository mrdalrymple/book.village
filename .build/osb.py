from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
#from reportlab.lib.units import inch


INPUT_FILENAME = "book.txt"
OUTPUT_FILENAME = "book.pdf"

#def way_one(file)

# Create a PDF document
doc = SimpleDocTemplate(OUTPUT_FILENAME, pagesize=letter)

# Create a list of flowable objects (Paragraphs)
styles = getSampleStyleSheet()
flowables = []

leading = 24

# Note: if wanting to double spaced or something... two spacers would be needed (paragraph I think uses spacers for it's line spacing)
blank_line = Spacer(1, 12)  # 1 inch wide, 12 points tall
#blank_line = Spacer(1, leading)

# Open the text file
last_line = None
with open('book.txt', 'r', encoding="utf-8") as file:
    #text = file.read()
    text = []
    current_paragraph = None
    # for line in file.readlines():
    #     if last_line is None:
    #         text = []
    #     elif last_line == "\n":
    #         flowables.append(Paragraph("\n".join(text), styles['BodyText']))
    #         text = []

    #     text.append(line)
    #     last_line = line

    #paragraph_style = styles['BodyText']
    paragraph_style = ParagraphStyle('BodyText', alignment=TA_JUSTIFY, leading=leading)

    prev_line = None

    count = 1

    debug = False
    # debug = True



    paragraph = None
    for line in file.readlines():
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

        if line == "\n":
            if prev_line == "\n":
                #print(f"({count}) SPACER 2")
                pass
            else:
                #print(f"({count}) SPACER")
                pass
            flowable = blank_line
        else:
            flowable = Paragraph(paragraph, paragraph_style)

        flowables.append(flowable)
        paragraph = None

        prev_line = line
        count = count + 1

    if paragraph:
        flowable = Paragraph(paragraph, paragraph_style)
        flowables.append(flowable)


#if text:
#    flowables.append(Paragraph("\n".join(text), styles['BodyText']))

#flowables.append(Paragraph(text, styles['BodyText']))

# Build the PDF
doc.multiBuild(flowables)
