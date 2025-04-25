import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

BASE_URL = "https://resumegenius.com/resume-samples"
DOWNLOAD_FOLDER = "downloaded_resumes"

# Ensure the directory exists
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Set up the driver with download preferences
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": os.path.abspath(DOWNLOAD_FOLDER),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}
chrome_options.add_experimental_option("prefs", prefs)

def get_resume_links():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extracting links for each job title
    job_links = [a['href'] for a in soup.find_all('a', href=True) if "resume" in a['href']]
    return job_links

def download_resumes_with_selenium(links):
    driver = webdriver.Chrome(options=chrome_options)
    
    for link in links:
        try:
            driver.get(link)
            
            # Adjusted to find the download button with class 'banner-download'
            download_button = driver.find_element(By.XPATH, "//a[contains(@class, 'banner-download')]")
            download_button.click()
            
            # Wait for the download to complete (you might need to adjust the sleep time)
            time.sleep(5)
        except Exception as e:
            print(f"Error downloading from {link}: {e}")

    driver.quit()

if __name__ == "__main__":
    resume_links = get_resume_links()
    download_resumes_with_selenium(resume_links)
