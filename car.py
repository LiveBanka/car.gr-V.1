import requests
import urllib2
from bs4 import BeautifulSoup
import os


def get_pages():
    for i in range(1,1000):
        site = requests.get("https://www.car.gr/classifieds/bikes/?condition=%CE%9A%CE%B1%CE%B9%CE%BD%CE%BF%CF%8D%CF%81%CE%B9%CE%BF&condition=%CE%9C%CE%B5%CF%84%CE%B1%CF%87%CE%B5%CE%B9%CF%81%CE%B9%CF%83%CE%BC%CE%AD%CE%BD%CE%BF&offer_type=sale&pg="+ str(i) +"&sort=pra")
        txt = open('main/' + str(i) + '.html' , 'w+')
        txt.write(site.text.encode("utf-8"))
        print '[DONE] ' , i
        txt.close
    print "get_page DONE"

def get_user():
    txt = open('userlinks.txt' , 'w+')
    for file in os.listdir(os.path.join('main')):
        page = urllib2.urlopen ( 'file:///'+ os.path.abspath('main/') + '/' + file)
        html_page = BeautifulSoup(page , 'html.parser')
        main_container = html_page.find_all("a", { "class" : "vehicle list-group-item clsfd_list_row" })
        for user in main_container:
            txt.write(user.get('href') + '\n')
    print "get_user DONE"
    txt.close()
def get_numbers():
    txt = open('userlinks.txt' , 'r')
    txt_number = open('txt_numbers.txt','w+')
    for line in txt:
        url =  "http://www.car.gr"+line
        site = requests.get(url)
        txt_user=open('user.html','w+')
        txt_user.write(site.text.encode("utf-8"))
        page = urllib2.urlopen('file:///'+ os.path.abspath('user.html'))
        html_page = BeautifulSoup(page , 'html.parser')
        container = html_page.find('h3',{'class': 'details-header'})
        numbers = container.getText()[:50]
        not_yet = numbers.replace(numbers[:37], "")
        get = not_yet.strip()
        txt_number.write(get + '\n')
        print get
    txt_number.close()
    print "get_numbers DONE"
def Remove():
    txt_number = open('txt_numbers.txt','r')
    txt_nice = open('txt_number.good.txt','w+')
    lst=[]
    for line in txt_number:
        lst=lst+[line]
    final_list = []
    for num in lst:
        if num not in final_list:
            final_list.append(num)
    for line in final_list:
        txt_nice.write(line)
    txt_number.close()
    txt_nice.close()
    os.remove('txt_numbers.txt')
get_pages()
get_user()
get_numbers()
Remove()
