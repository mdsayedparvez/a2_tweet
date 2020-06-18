#!/usr/bin/env python3
import sys
import json
import fileinput
def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True
list_of_word = ["han", "hon", "den", "det", "denna", "denne","hen"]
count = 0
for line in fileinput.input():
    if not line.strip():
        continue
    tweets = line.split("^M")
    for tweet in tweets:
             isValid = validateJSON(tweet)
                if (isValid == True):
            json_data = json.loads(tweet)
	     if (json_data["retweeted"] == False):
                count = count + 1
               tweet_words = json_data["text"].split()
                for search_word in list_of_word:
                    for tweet_word in tweet_words:
                        if (search_word == tweet_word.lower()):
                            print (("Counting the number of tweets mentioning each pronoun %s\t%s") % (search_word,1))
                            break


