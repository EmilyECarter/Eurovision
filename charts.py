from bs4 import BeautifulSoup
from urllib2 import urlopen
import lxml
import csv
import numpy
import pandas as pd
import requests

BASE_URL = "http://top40-charts.com/"


def make_soup(BASE_url):
    html = urlopen(BASE_url).read()
    return BeautifulSoup(html, "lxml")



def get_country_links(section_url):
    code = requests.get("http://top40-charts.com/charts.php")
    text = code.text
    soup=BeautifulSoup(text, "lxml")
    soupa= make_soup(section_url) #dummy does not work?
    topic_links=[]
    for topic_link in soup.select('td [href^=chart.php]'):
        topic_links.append(topic_link.get('href'))
    #links = soup.find("table", attrs={'width','640'}) #it doesn't like tbody change attrs={'width','640'}
    #for tr in links.find_all("tr"):
    country_links = []
    for link in topic_links:
        country_link = BASE_URL + str(link)
        country_links.append(country_link)
    #addd in australia later
    
    return country_links

#make another function to add dates I want to each url
#make this a function in future versions, when changing the dates and stuff, for now whatever
dates16 = pd.date_range(pd.datetime(2016, 03, 01), pd.datetime(2016,05,30), freq='W').tolist()
dates15 = pd.date_range(pd.datetime(2015,03, 01), pd.datetime(2015,05,30), freq='W').tolist()
dates14 = pd.date_range(pd.datetime(2014,03,01), pd.datetime(2014,05,30), freq='W').tolist()
dates13 = pd.date_range(pd.datetime(2013,03,01), pd.datetime(2013,05,30), freq='W').tolist()
dates12 = pd.date_range(pd.datetime(2012, 03,01), pd.datetime(2012,05,30), freq='W').tolist()
dates11 = pd.date_range(pd.datetime(2011,03,01), pd.datetime(2011, 05,30), freq='W').tolist()
dates10 = pd.date_range(pd.datetime(2010,03,01), pd.datetime(2010,05,30), freq='W').tolist()
start = pd.datetime(2009,03,01)
end = pd.datetime(2009,01,30)
dates09 = pd.date_range(start, end, freq='W').tolist()

import itertools
date_list =[]
date_list = list(itertools.chain(dates16, dates15, dates14, dates13, dates12, dates11, dates10, dates09))
date_strings = [dt.strftime('%Y %m %d.') for dt in date_list]
date_list = date_strings


def make_links(country):
    date_links = []
    for date in date_list:
        for link in country:
            date_link = link + str("&date=") + str(date)
            date_links.append(date_link)

    return date_links

def get_charts(week):
    soup = make_soup(week)
    song = soup.find_all('tr', attrs={'class':'latc_song'})
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    G=[]
    G.append(week)
    print song
    for s in song:
        
        This_Week = s.find('b').contents
        x=[]
        x=s.find_all('a')
        string = x[0].contents
        string = str(string)
        print string
        if string.find("Watch the video")== -1:
            title = x[1].contents
            Name = x[2].contents
            print title
            print Name
        else:
            title = x[2].contents
            Name = x[3].contents
            print "l"
        y=[]
        y=s.find_all('font', attrs={'color': '384953'})
        Last_Week = y[0].contents
        Peak_Position = y[1].contents
        Weeks_on_Chart = y[2].contents
        Total_Weeks_on_all_Chart = y[3].contents
        A.append(title)
        B.append(Name)
        C.append(Last_Week)
        D.append(Peak_Position)
        E.append(Weeks_on_Chart)
        F.append(Total_Weeks_on_all_Chart)
    df = pd.DataFrame(A,columns=['Title'])
    df['Name']=B
    df['Last Week']=C
    df['Peak Position']=D
    df['Weeks on Chart']=E
    df['Total Weeks on all Charts']=F
    df['link/country/date']=week
    df
    return df



alllinks = get_country_links("http://top40-charts.com/charts.php")
links = make_links(alllinks)

frame=[]
frame=pd.DataFrame(frame)
for each in links:
    chart=get_charts(each)
    frame=pd.concat([frame, chart], axis=0)
    frame.append(chart)
    frame.to_csv('charts.csv')



#other chart websites
#norway, week 16, year is 2012
#http://www.norwegiancharts.com/archiv.asp?sparte=s&woche=16&jahr=2012&todo=show
#soup.find_all('td', attrs{class:'text'})

#
