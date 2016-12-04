from eventregistry import *
import pandas as pd

#log in

#EventRegistry.login('emily.carter@y7mail.com', 'pipypony')

er = EventRegistry()
import os
print os.getcwd()

#get the concept URI
#this should probably be a function
#directory is dodgy use $(pwd) in bash to get current director

f = []
f=pd.DataFrame(f)
file = pd.read_csv(r'entries.csv')
entries = file['Artist']

def get_uri(entries):
    for person in entries:
        sugegestion = er.suggestConcepts(person)
        A=[]
        B=[]
        A.apend(er.format(suggestion))
        B.apend(person)
        
        print er.format(suggestion)
    return suggestion


start_date = ['2015-03-01', '2014-03-01', '2013-03-01']
end_date = ['2015-05-30', '2014-05-30', '2013-03-01']

start_date = pd.DataFrame(start_date)
end_date = pd.DataFrame(end_date)

dates = pd.concat([start_date, end_date],axis=0)
#using the same list as R google trends get a list of all things to track entrants_list
suggestions = get_uri(entries)
for person in suggestions:
    personUri = er.getConceptUri(person)

    for date in dates:
        q = GetCounts(personUri, startDate = dates[1,dates], endDate = dates[2,dates], source="geo")
        ret = er.execQuery(q)
print er.format(ret)

# return the same data but only for a small date range
#q.setDateRange("2015-05-15", "2015-05-20")
#ret = er.execQuery(q)
#print er.format(ret)

# get geographic spreadness of the concept Obama
#obamaUri = er.getConceptUri("Obama")
#q = GetCounts(obamaUri, source="geo")
#ret = er.execQuery(q)

# get the sentiment expressed about Obama
#q = GetCounts(obamaUri, source="sentiment")
#ret = er.execQuery(q)


# get social shared information for resulting articles
#q = QueryArticles(conceptUri = er.getConceptUri("Apple"))
#q.addRequestedResult(RequestArticlesInfo(
#                                         count = 5,
#                                         sortBy = "socialScore",
#                                         returnInfo = ReturnInfo(
#                                                                 articleInfo = ArticleInfoFlags(socialScore = True))))
#ret = er.execQuery(q)
#print er.format(ret)