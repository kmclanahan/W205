from __future__ import absolute_import, print_function, unicode_literals

import re
from streamparse.bolt import Bolt

################################################################################
# Function to check if the string contains only ascii chars
################################################################################
def ascii_string(s):
  return all(ord(c) < 128 for c in s)

class ParseTweet(Bolt):

    def process(self, tup):
        tweet = tup.values[0]  # extract the tweet
        place = tup.values[1]

        threats = ["war", "military", "danger", "violence", "unrest"]
        disasters = ["quake", "tsunami", "hurricaine"]

        # Split the tweet into words
        words = tweet.split()

        # Filter out the hash tags, RT, @ and urls
        valid_words = []
        for word in words:

            # Filter the hash tags
            if word.startswith("#"): continue

            # Filter the user mentions
            if word.startswith("@"): continue

            # Filter out retweet tags
            if word.startswith("RT"): continue

            # Filter out the urls
            if word.startswith("http"): continue

            # Strip leading and lagging punctuations
            aword = word.strip("\"?><,'.:;)")

            # remove special characters
            aword = aword.replace("'", "")
            aword = aword.replace("\\", "")
            aword = aword.replace("\/", "")

            # now check if the word contains only ascii
            if len(aword) > 0 and ascii_string(word):
                valid_words.append([aword.lower()])

        if not valid_words: return

        category = "None"
        string = ""

        for word in valid_words:
            if word in threats:
                category = "Threat"
            elif word in disasters:
                category = "Disaster"
            string += word[0] + " "
        # Emit all the words
        self.emit([string, category, place])

        # tuple acknowledgement is handled automatically
