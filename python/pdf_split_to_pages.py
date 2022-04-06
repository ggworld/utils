from PyPDF2 import PdfFileWriter, PdfFileReader

original_pdf = "/Users/geva/Downloads/טופס ירוק - מנחם גבע.pdf"
dest_pdf = ""/Users/geva/Downloads/"
inputpdf = PdfFileReader(open(original_pdf, "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open(f"{dest_pdf}document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)
