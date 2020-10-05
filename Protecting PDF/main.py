from PyPDF2 import PdfFileWriter, PdfFileReader

def secure_pdf(file, password):
    parser = PdfWriter()
    pdf = PdfFileReader(file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)
    with open(f"encrypted_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"encrypted_{file} created...")
    
if __name__=='__main__':
    file = "pdf_file_name.pdf"
    password = "Password@007"
    secure_pdf(file, password)
