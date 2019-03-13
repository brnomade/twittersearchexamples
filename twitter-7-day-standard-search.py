from TwitterSearch import *
import datetime 

def searchInTweeter( aSearch, upperDateYear, upperDateMonth, upperDateDay ):
    try:
        tso = TwitterSearchOrder() 
        tso.set_keywords(aSearch,False) 
        tso.add_keyword('filter:native_video')
        #tso.add_keyword('-filter:retweets')
        tso.set_until(datetime.date(upperDateYear,upperDateMonth,upperDateDay))
        #tso.set_result_type("recent")
        #tso.set_count(5)
        #tso.set_exclude_replies(True)
        #tso.set_include_entities(False) 
        
        ts = TwitterSearch(
            consumer_key = '6iW6gVFmNxLs0khWVxlCnzUJg',
            consumer_secret = 'SNy6UZtheRdNyk6jjvORSKNO0TgomNhdKqUk84FBRzmC8F3pRl',
            access_token = '943494555919413249-eDYtNZX4y9z86smISfInzeDiemN06mL',
            access_token_secret = 'LVzZsSgP5v3bng05OOIPjqXUSuxvb5jaMwOMpY47TjJ7w')
        response = ts.search_tweets(tso)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    else:
        print("Searched in Tweeter using standard 7 day API")
        print("Keywords : ", aSearch)
        print("URL      : ", tso.create_search_url())
        print("Rule     : <not available>")
        counter = 0
        for tweet in response['content']['statuses']:
            #for tweet in ts.search_tweets_iterable(tso):
            x = "http://twitter.com/" + tweet['user']["id_str"] + "/status/" + tweet["id_str"] + '  ' + tweet["created_at"]
            counter = counter + 1
            print(x)
        print("Found: ", counter)
        print("-------")

        
    
print("")
print("Search by Text. Query? - default: 'Kariba Zimbabwe MonkeyBusiness'" )
aString = input()
if len(aString) == 0:
    aSearch = ['Kariba Zimbabwe MonkeyBusiness']
else:
    aSearch = [aString]
searchInTweeter(aSearch,2019,2,5)

print("")
print("Searching by Individual Words. Query? - default: 'Kariba Zimbabwe MonkeyBusiness'")
aString = input()
if len(aString) == 0:
    aString = 'Kariba Zimbabwe MonkeyBusiness'
for word in aString.strip(" ").split(" "):
    searchInTweeter([word],2019,2,5)
