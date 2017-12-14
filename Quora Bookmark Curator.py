from selenium import webdriver
import time
import pyperclip
import pdfkit
from bs4 import BeautifulSoup
import requests

browser = webdriver.Chrome()
browser.get("https://www.quora.com/bookmarked_answers")
wait_input = input("\n\nPress Enter once page loaded\n\n")

question = browser.find_element_by_class_name("question_link").text
browser.get("https://www.quora.com/bookmarked_answers?order=desc")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    current = browser.find_element_by_class_name("question_link")
    current = current[len(current)-1].text
    if(question == current):
        break

share = browser.find_element_by_link_text("Share")

options = {'page-size' : 'Letter', 'dip':'450','javascript-delay':10000}

l = len(share)
j = 0

for i in range(l):
    try:
        share[i].click()
        time.sleep(5)
        copy = browser.find_element_by_link_text("Copy Link")
        copy.click()
        answer = pyperclip.paste()
        conn = requests.get(url=answer)
        soup = BeautifulSoup(conn.read(),"html.parser")
        title = soup.find('a',class_="question_link").text
        pdfkit.from_url(answer,title+'.pdf',options=options)
    except:
        j+=1
        print("Fail",j)

print("Job Done!!")
