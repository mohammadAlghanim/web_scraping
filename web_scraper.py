import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
def  get_citations_needed_count(url):
    """
    Retrieves the count of citations needed on a webpage.

    Args:
        url (str): The URL of the webpage to analyze.

    Returns:
        int: The count of citations needed on the webpage.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_posts = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    count=0
    for i in all_posts:
      if i:
       count+=1
    return count
print(get_citations_needed_count(URL))



def  get_citations_needed_report(url):
   """
    Generates a report of citations needed on a webpage.

    Args:
        url (str): The URL of the webpage to analyze.

    Returns:
        str: The report of citations needed on the webpage.
    """
   page = requests.get(url)
   soup = BeautifulSoup(page.content, 'html.parser')
   tiile = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
   report=''
   list_of_p=[]
   for i in tiile:
      p_tag = i.find_previous('p')
      
      if p_tag:
        citation_text = p_tag.text
        report += citation_text + "\n\n"
        list_of_p.append(report)
        # print(citation_text)
#    h =set(list_of_p)
   return report




print(get_citations_needed_report(URL))

