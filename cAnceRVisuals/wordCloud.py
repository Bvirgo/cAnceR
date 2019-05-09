from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import urllib
import requests
import matplotlib.pyplot as plt
import csv
from pylab import figure, axes, pie, title, show
from matplotlib import pyplot as plt

#importing csv file and getting names of the cancers and amount of them.
with open('create_barchart.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    line_count = 0
    wordsstr = ''
    for row in readCSV:
        if (line_count == 0 or line_count == 1):
            line_count += 1
        else:          
            num = int(float(row[0].split(";")[1]))
            if (num < 1):
                num = 1            
            for x in range(num):
                    wordsstr = wordsstr + row[0].split(";")[0] + ' '

#creating mask to world cloud. Shape of a hexagon.
mask = np.array(Image.open('hexagon.png'))

# This function takes in your text and your mask and generates a wordcloud. 
def generate_wordcloud(wordsstr, mask):
    word_cloud = WordCloud(width = 512, height = 512, background_color='white', collocations=False, stopwords=STOPWORDS, mask=mask).generate(wordsstr)
    plt.figure(figsize=(11,11),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('footest8.svg')
    plt.show()
    
#Run the following to generate your wordcloud
generate_wordcloud(wordsstr, mask)