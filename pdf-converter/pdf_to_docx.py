import PyPDF2
import docx


file_name = 'Riaz Pages SIGNED.pdf'
# Open the PDF file in read-binary mode
with open(file_name, 'rb') as pdf_file:

    # Read the PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Create a new Word document
    doc = docx.Document()

    # Loop through each page in the PDF file
    for page_num in range(len(pdf_reader.pages)):

        # Get the page from the PDF file
        pdf_page = pdf_reader.pages[page_num]

        # Extract the text from the page
        text = pdf_page.extract_text()

        # Add the text to the Word document
        doc.add_paragraph(text)

    # Save the Word document
    doc.save('example.docx')