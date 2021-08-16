from bs4 import BeautifulSoup
import requests
from datetime import datetime

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/58.0.3029.110 Safari/537.3'}
url = "https://www.linkedin.com/jobs/software-test-engineer-jobs?position=1&pageNum=0"
html_text = requests.get(url, headers=header).text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
selection = soup.find('ul', class_='jobs-search__results-list')
jobs = selection.find_all("li")
current_time = datetime.now()
file_name = current_time.strftime("%m_%d_%y_%H_%M")

with open(f"/home/manish/Documents/Programming/Python/pythonProject/Python_Mini_Projects/Job_Posts/{file_name}.txt",
          'w') as f:
    for job in jobs:
        company = job.find('h4', class_='base-search-card__subtitle').text.strip()
        job_title = job.find('h3', class_='base-search-card__title').text.strip()
        location = job.find('span', class_='job-search-card__location').text.strip()
        # urgency = job.find('span', class_='result-benefits__text').text.strip()
        # posted_on = job.find('time', class_='job-search-card__listdate').text.strip()
        link = job.find('a', class_='base-card__full-link')
        url = link['href']
        f.write(f"{company} : {job_title} : {location}\nurl: {url} \n\n")
print(f"file saved: {file_name}")
