from bs4 import BeautifulSoup
from urllib2 import urlopen
import lxml
import csv
import numpy
import pandas as pd
import requests

BASE_URL = "http://www.norwegiancharts.com/"
URL2012 = "http://www.norwegiancharts.com/showitem.asp?titel=Eurovision+Song+Contest+-+Baku+2012&cat=a"
year = [URL2012]


def make_soup(BASE_url):
    html = urlopen(BASE_url).read()
    return BeautifulSoup(html, "lxml")



def get_song_links(section_url):
    for each in year:
        code = requests.get(each)
        text = code.text
        soup = make_soup(section_url) #dummy does not work?
        topic_links = []
        rows = soup.find_all('tr', attrs={ 'onmouseover' : "this.style.backgroundColor='#FFFFFF';"})
        for row in rows:
            topic_links.append(row.find('a').get('href'))
        #links = soup.find("table", attrs={'width','640'}) #it doesn't like tbody change attrs={'width','640'}
        #for tr in links.find_all("tr"):
        song_links = []
        for link in topic_links:
            song_link = BASE_URL + str(link)
            song_links.append(song_link)
    return song_links

def get_charts(song_links):
    for each in song_links:
        soup = make_soup(each)
        rows= []
        rows = soup.find('div', attrs={'class': 'text'})
        A =[]
        B = []
        C = []
        D = []
        D.append(each)
        for row in rows:
            if row.a:
                week = row.a.contents
                print week
                width = row.find('img')
                rank = row.td.contents
                position = width.get('width')
                A.append(week)
                B.append(rank)
                C.append(position)
            df = pd.DataFrame(A,columns=['Week'])
            df['Rank']=B
            df['Position']=C
            df['table link']=D
            df

    return df

def nech_charts(charts):
    for each in charts:
        soup = make_soupe(each)
        rows = []
        rows = soup.find_all('table', attrs={'class': 'chartrun'})
        A = []
        B = []
        C = []
        D = []
        D.append(each)
        if rows:
            for row in rows:
                week = row.a.contents
                width = row.find('img')
                rank = row.td.contents
                position = width.get('width')
                A.append(week)
                B.append(rank)
                C.append(position)
                df = pd.DataFrame(A, columns=['Week'])
                df[Rank'] = B
                df['position'] = C
                df['table link'] = DataFrame
                df
                   
    return df

def get_other_countries(song_links):
    soup = make_soup(song_links)
    if soup.find(text='World wide') ==  1:
        s = soup.find(text='World wide').parent.findNext('td')
        links = []
        for row in s:
            links.append(row.get('href'))
    print links
    return links

#No Germany

#Netherlands and switwerland
#if
#ne/che_charts(link)
#else if Germany
#else
#get_charts(links)





song_links = get_song_links(URL2012)
Nlinks = get_charts(song_links)
other_countries = get_other_countries(song_links)
charts1df = []
charts1df = pd.DataFrame(charts1df)
charts2df = []
charts2df = pd.DataFrame(charts2df)
charts3df = []
charts3df = pd.DataFrame(charts3df)
for link in Nlinks:
    chart = get_charts(link)
    charts3df = pd.concat([charts3df, chart], axis=0)
for other in other_countries:
    if 'ch' OR 'ne' in other:
        chart = nech_charts(other):
        charts1df = pd.concat([charts1df,chart], axis=0)
    else if 'ge' in other:
        y = 2
    else:
        chart = get_charts(other)
        charts2df = pd.concat([charts2df,chart], axis=0)
full_charts = pd.concat([charts1df,charts2df,charts3df])
full_charts.to_csv('country charts.csv')
    


