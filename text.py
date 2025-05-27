import PyPDF2 # Library used to read PDF files and extract text
import random # Used to randomly select batches of text from the PDF content
# This function reads a PDF, extracts all readable text from each page, and filters it to 
# keep only meaningful lines that begin with a letter — preparing the content for further
# use like generating MCQs.
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            # Extract text and split into lines
            page_text = page.extract_text().splitlines()
            # Iterate through lines, keeping only those starting with a letter
            text += "\n".join([line for line in page_text if line[0].isalpha()])
    return text
# This function randomly selects and returns smaller chunks of text from a large PDF by
# slicing fixed-size segments from random positions, helping avoid overloading the model
# with too much input.
def select_text_from_pdf(pdf_path, batch_size=10000, num_batches=2):
    # Extract text from PDF

    pdf_text = extract_text_from_pdf(pdf_path)

    # Calculate the total number of words in the preprocessed text
    total_words = len(pdf_text)

    # Randomly select starting indices for the batches
    selected_start_indices = random.sample(range(total_words - (batch_size * num_batches)), num_batches)

    # Initialize the selected text
    selected_text = ""

    # Extract text for each selected batch and concatenate
    for start_index in selected_start_indices:
        end_index = start_index + batch_size
        selected_text += pdf_text[start_index:end_index]

    return selected_text
