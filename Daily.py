

from bs4 import BeautifulSoup
from urllib2 import urlopen
import lxml
import pandas as pd


BASE_URL = "http://esctracker.com/"


def make_soup(BASE_url):
    html = urlopen(BASE_url).read()
    return BeautifulSoup(html, "lxml")

def itunes(BASE_URL):
    soup = make_soup(BASE_URL)
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    for div in soup.find_all('div', attrs={'class', 'block_content'}):
        songa = div.find('h3')
        song = songa.get_text()

        for country in div.find_all('label'):
            
            charts = country.get_text().split(' ')

            A.append(charts[0])
            B.append(charts[1])
            C.append(song[0])
            D.append(song[1])
            E.append(div.p.contents)

    df = pd.DataFrame(A,columns=['Position on Chart'])
    df['Country']=B
    df['Song Name']=C
    df['Artist']=D
    df['Artist Country']=E
#create another column that is year, 2016 for everything
    df
    df.to_csv('charts2016.csv', encoding='utf-8')
# country names with spaces still don't work, and special characters get stuffed up


#now do the same thing just in other tabs

def youtube(section_url):
    soup=make_soup(section_url)
    Aa = []
    Bb = []
    for div in soup.find_all('div', attrs={'class', 'block_content'}):
        label = div.label.contents
        Aa.append(label)
        span = div.span.contents
        Bb.append(span)
    df2=pd.DataFrame(Aa, columns=['Youtube Views'])
    df2['Country'] = Bb
    df2
    df2.to_csv('Youtube.views2016.csv',encoding='utf-8')
#add spotify when available



x= "http://esctracker.com/"
y= "http://esctracker.com/youtube"

make_soup(x)
itunes(x)
youtube(y)
print("itunes")

#IT WORKS!!!!!! ITS STILL STUFFY AND HAS /CODES EVERYWHERE, AND ONLY DISPLAYS ONE LETTER BUT IT WORKS!!!!!!