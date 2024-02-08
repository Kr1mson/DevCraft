import pdfplumber
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Extract text to string
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text_content = ""
        for page in pdf.pages:
            text_content += page.extract_text()
    return text_content

# Remove Punctuation
def remove_punctuation(text_content):
    pattern = r'[^a-zA-Z0-9\s]'  
    result = re.sub(pattern, '', text_content)
    return result

# Get Keywords
def get_keywords(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words]
    return filtered_tokens

if __name__ == "__main__":
    pdf_path = r"C:\Users\parth\OneDrive\Desktop\DevCraft\Non-Disclosure-Agreement-Template-Signaturely.pdf"
    text_content = extract_text_from_pdf(pdf_path)
    print("Data extracted to string.")
    text_content = remove_punctuation(text_content)
    keywords = get_keywords(text_content)
    print("Keywords:")
    for word in keywords:
        print(word)

