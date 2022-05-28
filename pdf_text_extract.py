import PyPDF2
pdf = open("example.pdf", "rb") #Enter your pdf name in place of example.pdf
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0) #text extract from page 0
print(page.extractText())
