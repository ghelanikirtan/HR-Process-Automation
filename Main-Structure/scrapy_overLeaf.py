import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.overleaf.com/gallery/tagged/cv"
OUTPUT_FILE = "pdf_links.txt"

def get_resume_links():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extracting links for each resume template
    resume_links = [a['href'] for a in soup.find_all('a', href=True) if "/latex/templates/" in a['href']]
    return resume_links

def save_pdf_links_to_file(links):
    with open(OUTPUT_FILE, 'w') as file:
        for link in links:
            # Append .pdf to the link
            pdf_link = link + ".pdf"
            file.write(pdf_link + "\n")

if __name__ == "__main__":
    resume_links = get_resume_links()
    save_pdf_links_to_file(resume_links)
    print(f"All PDF links saved to {OUTPUT_FILE}")
