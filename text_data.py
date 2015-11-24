from sys import argv
from collections import Counter
import re
import collections

# Third party dependencies
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

script, filename = argv

characters = "abcdefghijklmnopqrstuvwxyz "
input_file = open(filename)
text = input_file.read()
input_file.close()
text = text.lower()

common = open('common_words.txt')
common_words = common.read()
common.close()
common_words.lower()
common_wordlist = re.sub("[^\w]", " ", common_words).split()
common_wordlist = set(common_wordlist)

def striptext():
	stripped_text = ""
	for c in text:
		if c not in characters:
			c = ""
		stripped_text += c
	return stripped_text

def makelist(stripped_string):
	wordlist = re.sub("[^\w]", " ", stripped_string).split()
	return wordlist

def removecommon(wordlist, common_wordlist):
	for word in common_wordlist: del wordlist[word]
	return wordlist

def countwords(wordlist):
	counts = Counter(wordlist)
	return counts

count = countwords(makelist(striptext()))

def makecloud(text):
	wordcloud = WordCloud(max_font_size=100).generate(text)
	plt.figure()
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

#makecloud(striptext())

dict_count = dict(count)
keys = dict_count.keys()
items = dict_count.values()

od = collections.OrderedDict(sorted(dict_count.items()))

objects = list(od.keys())
y_pos = np.arange(len(objects))
performance = list(od.values())

sortedod = collections.OrderedDict(sorted(od.items(), key=lambda t: t[1]))

for item in sortedod.keys():
	if item in common_wordlist:
		del sortedod[item]

for item in sortedod.keys():
	if len(item) <= 4:
		del sortedod[item]

for item in sortedod.keys():
	if sortedod[item] <= 50:
		del sortedod[item]

objects = list(sortedod.keys())
y_pos = np.arange(len(objects))
performance = list(sortedod.values())
ind = range(2, len(objects))

i = 0
x = []
while i < len(objects):
	x.append(i)
	i += 1

plt.figure(figsize=(22, 9))
ax = plt.subplot(111)

ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

plt.xticks(x, objects, fontsize=12, rotation='vertical')
plt.yticks(range(0, max(performance), 25), fontsize=12)

plt.xlabel("Word", fontsize=16)
plt.ylabel("Usage", fontsize=16)

plt.tight_layout()
plt.margins(.02)
plt.subplots_adjust(bottom=0.165)
plt.bar(y_pos, performance, width=0.5, align="center")
plt.title('Word Usage in Beloved')

rects = ax.patches
labels =["%d" % rect.get_height() for rect in rects ]

for rect, label in zip(rects, labels):
	height = rect.get_height()
	ax.text(rect.get_x() + rect.get_width()/2, height + 3, label, ha='center', va='bottom', fontsize="7")

plt.grid()
ax.xaxis.grid(False)
plt.savefig('frequency.png')
plt.show()
plt.close()

makecloud(striptext())
