# Read file into a DataFrame
df = pd.read_csv(url, ';')

# Read in all sheets of Excel file: xl
xl = pd.read_excel(url, sheetname = None)

# Print the sheetnames to the shell
print(xl.keys())

## Requests using urllib
from urllib.request import urlopen, Request

request = Request(url)
response = urlopen(request)
html = response.read()
print(html)
response.close()

## Requests using requests, Prettify using BeautifulSoup
import requests
from bs4 import BeautifulSoup

resp = requests.get(url)
html_doc = resp.text
soup = BeautifulSoup(html_doc)
pretty_soup = soup.prettify()
guido_title = soup.title
guido_text = soup.get_text()

# Find all 'a' tags (which define hyperlinks)
a_tags = soup.find_all('a')

# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)    # type(json_data) = <class 'dict'>

# API requests
import requests

resp = requests.get(url)
print(r.text)

# Decode the JSON data into a dictionary
json_data = resp.json()
# extract a piece of json
json_data['query']['pages']['24768']['extract']

############################################################################################################

## Twitter API
import tweepy
auth = tweepy.OAuthHandler(<consumer_key>, <consumer_secret>)
auth.set_access_token(<access_token>, <access_token_secret>)

## Streaming tweets
l = MyStreamListener()

# Create your Stream object with authentication
stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords:
stream.filter(track = ['clinton', 'trump', 'sanders', 'cruz'])

## Load and explore twitter data
import json

tweets_data = []
tweets_file = open(file, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

## word search in text
import re

def word_in_text(word, text):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, text)

    if match:
        return True
    return False
  
## text analysis to count how many tweets contain the words 'clinton', 'trump', 'sanders' and 'cruz'
# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

## Plotting twitter data
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()
