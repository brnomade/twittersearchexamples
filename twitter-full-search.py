from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results


def searchInTweeter( aSearch, upperDateYear, upperDateMonth, upperDateDay ):
    premium_search_args = load_credentials("~/.twitter_keys.yaml",
                                       yaml_key="search_tweets_fullsearch_dev",
                                       env_overwrite=False)

    rule = gen_rule_payload(aSearch + " has:videos", 
                            # -is:retweet -> good test for a enterprise subscription
                            to_date= (str(upperDateYear) + "-" + str(upperDateMonth) + "-" + str(upperDateDay)),
                            results_per_call=100)

    try:
        tweets = collect_results(rule,
                        max_results=100,
                        result_stream_args=premium_search_args) 
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    else:
        print("Searched in Tweeter using full search since 2006 API")
        print("Keywords : ", aSearch)
        print("URL      : <not available>")
        print("Rule     : ", rule)
        counter = 0
        for tweet in tweets:
            print("http://twitter.com/" + tweet['user']["id_str"] + "/status/" + tweet["id_str"] + '  ' + tweet["created_at"])
            counter = counter + 1
        print("Found: ", counter)
        print("-------")

            
            
            
print("")
print("Search by Text. Query? - default: 'Kariba Zimbabwe MonkeyBusiness'" )
aString = input()
if len(aString) == 0:
    aSearch = 'Kariba Zimbabwe MonkeyBusiness'
else:
    aSearch = aString
searchInTweeter(aSearch,2015,2,5)

print("")
print("Searching by Individual Words. Query? - default: 'Kariba Zimbabwe MonkeyBusiness'")
aString = input()
if len(aString) == 0:
    aString = 'Kariba Zimbabwe MonkeyBusiness'
for word in aString.strip(" ").split(" "):
    searchInTweeter(word,2015,2,5)