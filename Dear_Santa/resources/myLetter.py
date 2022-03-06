from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image('resources/santa.png', 10, 8, 100)
        self.ln(40)
        self.set_font('Courier', 'BU', 40)
        self.cell(0, 20, 'Dear Santa', ln=1, align='C')
        self.ln(20)

"""
    pdf = PDF('P', 'mm', 'Letter')
    pdf.set_auto_page_break(auto=True, margin=35)
    pdf.add_page()
    pdf.set_font('Courier', 'B', 25)

    myLetter = open('myLetter.txt', 'r')

    for line in myLetter:
        pdf.multi_cell(200, 10, txt=line, align='L')
           
    pdf.output('myLetter.pdf', 'F')
"""