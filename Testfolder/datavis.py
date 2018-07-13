'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''
from wordcloud import WordCloud

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("twitterdata.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
aPolarity =[]
aSubjectivity=[]
average=0
# Continue your program below!

# Textblob sample:
for tweet in tweetData:
    tb = TextBlob(tweet["text"])
    aPolarity.append(tb.polarity)
    aSubjectivity.append(tb.subjectivity)
# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
t = plt.xlabel('my data', fontsize=14, color='red')
plt.title(r'$\sigma_i=15$')


for i in range(len(aPolarity)):
    average=average+aPolarity[i]
average=average/len(aPolarity)

print(average)
