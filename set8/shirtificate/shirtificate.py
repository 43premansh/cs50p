from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", format="A4")
pdf.add_page()

# Title at the top
pdf.set_font("Helvetica", style="B", size=40)
pdf.cell(w=0, h=20, text="CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

# Shirt image
pdf.image("shirtificate.png", x=10, y=60, w=190)

# Name in white, on top of shirt
pdf.set_text_color(255, 255, 255)
pdf.set_font("Helvetica", style="B", size=30)
pdf.set_xy(x=0, y=110)  # adjust y until name sits where shirt text would
pdf.cell(w=210, h=10, text=f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")