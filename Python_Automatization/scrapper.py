import requests # python -m pip install requests beautifulsoup4
from bs4 import BeautifulSoup

url = "https://www.seek.co.nz/python-jobs/part-time?salaryrange=100000-&salarytype=annual"

if "__main__" == __name__:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    def has_data_search(tag):
        return tag.has_attr("data-search-sol-meta")

    results = soup.find_all(has_data_search) 

    for job in results:
        try:
            titleElement = job.find("a", attrs={"data-automation": "jobTitle"})
            title = titleElement.get_text()
            company = job.find("a", attrs={"data-automation": "jobCompany"}).get_text()
            joblink = "https://www.seek.co.nz" + titleElement["href"]
            salary = job.find("span", attrs={"data-automation": "jobSalary"})
            salary = salary.get_text() if salary else 'n/a'

            job = "Title: {}\nCompany: {}\nSalary: {}\nLink: {}to\n"

            job = job.format(title, company, salary, joblink)
                  
            print(job)
        except Exception as e:
            print("Exception: {}".format(e))
            pass
#python scrapper.py >> jobs.txt  ||  python3 scrapper.py >> jobs.txt