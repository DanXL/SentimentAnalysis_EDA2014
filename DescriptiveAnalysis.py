import os
import re
import json, inspect, pandas, numpy
#from nltk import *
#import numpy;
from pylab import *;
from matplotlib import pyplot
from scipy import stats
import matplotlib


os.getcwd()
os.chdir("C:\Users\Administrator\Desktop\WorkShop")

datause = json.loads(open('feature_empty.txt','r').read())
dataframe_twitter = pandas.DataFrame(datause)


def FreqTable(feature):
    key = []
    value = []
    for iterm in list(set(feature)):
        iter_var = 0;
        key.append(str(iterm))
        for iterm_m in feature:
            if iterm_m == iterm:
                iter_var = iter_var+1;
        value.append(iter_var)
    return value,key


def BarChart(feature,name="",bottom_height=0.05):
    #frame = inspect.currentframe()
    #args, varargs, keywords, values = inspect.getargvalues(frame)
    #print args, varargs, keywords
    value,key = FreqTable(feature)
    #return (value,key)
    fig = pyplot.figure()
    pyplot.title(name+" Distribution", fontsize=20)
    pyplot.ylabel("Frequency",fontsize=16)
    pyplot.bar(numpy.arange(len(key)),value,width=1.0)
    pyplot.xticks(numpy.arange(len(value))+0.4,key,rotation=90, size='medium')
    pylab.subplots_adjust(bottom = 0.01)
    pyplot.savefig(name+".png", dpi=1000)
    pyplot.show()



'''
Language Distribution
'''
data_lang = [x for x in datause['lang'] if x !='Emptyyyyy']
#BarChart(data_lang,'Language')


'''
SignIn Source Distribution
'''
data_source = dataframe_twitter[dataframe_twitter['lang']=='en']['source']

'''
['Echofon', 'Hootsuite', 'TweetAdder v4', 'Mobile Web (M2)', 'Twitter for Windows Phone',
'Tweetbot for iS', 'Twitter for iPhone', 'Twitter for Android', 'RoundTeam', 'Instagram',
'Mobile Web (M5)', 'Twitter for Websites', 'Tweetlogix', 'Cloudhopper', 'Unfollowers.me',
'TweetCaster for iOS', 'twitterfeed', 'PlumeforAndroid', 'dlvr.it', 'Twitter for  Android',
'Twitter for iPad', 'iOS', 'Twitter Web Client', 'Twitter for Mac',
'TweetCaster for Android', 'IFTTT', 'Facebook', 'Twitter for BlackBerry', 'TweetDeck',
'Twitter for Android Tablets']
'''
def BarChart(feature,name="",bottom_height=0.3):
    #frame = inspect.currentframe()
    #args, varargs, keywords, values = inspect.getargvalues(frame)
    #print args, varargs, keywords
    value,key = FreqTable(feature)
    key_new = [key[x] for x in range(len(key)) if value[x] >= 50 ]
    value_new = [x for x in value if x >= 50]
    fig = pyplot.figure()
    pyplot.title(name+" Distribution",fontsize=20)
    pyplot.ylabel("Frequency",fontsize=18)
    pyplot.bar(numpy.arange(len(key_new)),value_new,width=0.8)
    pyplot.xticks(numpy.arange(len(value_new))+0.4,key_new,rotation=90, size='small')
    subplots_adjust(bottom = bottom_height)
    pyplot.savefig(name+".png", dpi=1000)
    pyplot.show()

#[elem for elem in li if li.count(elem) == 1]
    
#BarChart(data_source,'SignIn Gate',0.34)

'''
histogram of Sentiment score
'''
#fig = pyplot.figure()
#x = list(dataframe_twitter[dataframe_twitter['lang'] == 'en']['score']);
#pyplot.hist(x,bins=107,log=True)
#pyplot.ylabel('Frequency',fontsize=16);pyplot.xlabel('Score',fontsize=16);
#pyplot.title('Histogram of Sentiment Score',fontsize=20)
#pyplot.savefig("sentiment_score_dist.png", dpi=1000)
#show()
#print 't-statistic = %6.3f pvalue = %6.4f' %  stats.ttest_1samp(x, 0)
'''t-statistic = 49.995 pvalue = 0.0000'''

'''
score exploration by valid source
'''
#value,key = FreqTable(data_source)
#key_new = [key[x] for x in range(len(key)) if value[x] >= 50 ]
#new_frame = numpy.array(dataframe_twitter)
#source_score = [mean(new_frame[(new_frame[:,6] == ss) & (new_frame[:,3] == 'en'),5]) for ss in key_new]
#
def BarChart_source_score(name="Avg Score by Source",bottom_height=0.3):
    fig = pyplot.figure()
    pyplot.title("Average Sentment Score Over different SignIn Gates",fontsize=20)
    pyplot.ylabel("Average Score",fontsize=18)
    pyplot.xlabel('Source',fontsize=18)
    pyplot.bar(numpy.arange(len(key_new)),source_score,width=1)
    pyplot.xticks(numpy.arange(len(source_score))+0.5,key_new,rotation=90, size='small')
    subplots_adjust(bottom = bottom_height)
    pyplot.savefig(name+".png", dpi=1000)
    pyplot.show()

#source_score_ttest = [stats.ttest_1samp(new_frame[(new_frame[:,6] == ss) & (new_frame[:,3] == 'en'),5],0) for ss in key_new]
#for each in source_score_ttest:
#	print "t=%6.3f p=%6.4f" % each;
'''
t= 0.436 p=0.6632
t= 4.979 p=0.0000
t= 3.914 p=0.0001
t= 6.105 p=0.0000
t= 7.290 p=0.0000
t= 4.016 p=0.0001
t= 2.249 p=0.0250
t=29.600 p=0.0000
t=15.705 p=0.0000
t= 3.547 p=0.0005
t= 2.349 p=0.0214
t=14.301 p=0.0000
t= 4.273 p=0.0000
t= 7.386 p=0.0000
t= 1.893 p=0.0601
t= 0.519 p=0.6042
t=   nan p=   nan
t= 1.776 p=0.0769
t= 2.150 p=0.0341
t= 7.383 p=0.0000
t= 3.842 p=0.0002
t=-21.627 p=0.0000
t= 2.954 p=0.0036
t= 4.214 p=0.0000
t= 1.446 p=0.1490
t= 5.952 p=0.0000
t= 1.744 p=0.0843
t= 1.037 p=0.3046
t= 1.747 p=0.0848
t= 7.993 p=0.0000
t= 2.818 p=0.0061
t= 0.863 p=0.3920
t=12.072 p=0.0000
t= 7.080 p=0.0000
t= 6.289 p=0.0000
t=26.740 p=0.0000
t= 1.214 p=0.2267
t= 3.473 p=0.0005
t= 7.409 p=0.0000
t= 0.393 p=0.6959
t= 7.445 p=0.0000
t= 8.802 p=0.0000
t= 9.942 p=0.0000
t= 5.541 p=0.0000
'''
'''
standard_error
'''
#std = [std(new_frame[(new_frame[:,6] == ss) & (new_frame[:,3] == 'en'),5]) for ss in key_new]
#df = [len(new_frame[(new_frame[:,6] == ss) & (new_frame[:,3] == 'en'),5])-1 for ss in key_new]
#den = sqrt(df)
#se = std/den
'''
array([ 0.18834908,  0.08166488,  0.13796189,  0.09971945,  0.10844998,
        0.11201968,  0.13385574,  0.01056592,  0.0187496 ,  0.18792799,
        0.29303824,  0.08088375,  0.12149484,  0.13157589,  0.16544395,
        0.15796684,  0.        ,  0.1545093 ,  0.35247193,  0.17270403,
        0.2650723 ,  0.0271019 ,  0.19761608,  0.12687558,  0.14966221,
        0.08761825,  0.26641652,  0.32135335,  0.21373835,  0.0682212 ,
        0.14636281,  0.30506   ,  0.04724163,  0.11585473,  0.11236504,
        0.03076309,  0.24076621,  0.11534658,  0.08643559,  0.37701928,
        0.13031919,  0.10319241,  0.07543496,  0.08506183])
'''


'''
twitter_favoriated
'''
#fav = dataframe_twitter[dataframe_twitter['lang']=='en']['favorite_count']

'''
coordinates
'''
#coord = dataframe_twitter[dataframe_twitter['lang']=='en']['coordinates']
'''
i = 0;
coord_new = [];
for each in coord:
    if each != None:
        coord_new.append(tuple(each['coordinates']));
    i = i+1;
mc = matrix(coord_new)
mc = numpy.array(coord_new)
'''
'''
dic_new = {}
x = list(dataframe_twitter[dataframe_twitter['lang'] == 'en']['score'])
i = 0;j=0;
for each_i in range(len(coord)):
    if coord[each_i] != None:
        try:
		dic_new[tuple(coord[each_i]['coordinates'])] = x[each_i];
	i = i +1;
    except KeyError:
	print j;
    j = j+1;

'''


