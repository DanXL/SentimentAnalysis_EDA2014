#!/usr/bin/python2.7 
# -*- coding: utf-8 -*-

import os, re, json, inspect
input_file = "output.txt"

os.getcwd()
os.chdir("C:\Users\dan.xi\Documents\CUFE\2014 Spring\Final Project\SentimentAnalysis")




'''create score_dictionary to store AFINN-111'''
afinn_dic = {}
afinn = open("AFINN-111.txt","r")
afinn_list = afinn.readlines()
afinn.close()
for term_i in range(len(afinn_list)):
	afinn_tmp = afinn_list[term_i].strip().split('\t')
	afinn_dic[afinn_tmp[0]] = int(afinn_tmp[1])




'''shape the raw data to big table with AFINN-111 score on each twitter sentence'''	
import numpy;
i = 0; j = 0;
inputfile = open(input_file,"r")
data = [];user_id=[];
features_twitter = [u'id_str',u'text',u'source',u'coordinates',u'retweet_count',u'favorite_count',u'lang'];
features_user = [u'id_str',u'location',u'time_zone',u'geo_enabled',u'followers_count',u'friends_count',u'listed_count',u'created_at',u'favourites_count',u'timezone',u'statuses_count',u'lang',u'profile_backgroud_color',u"profile_sidebar_border_color",u'profile_sidebar_fill_color',u'profile_text_color',u'profile_use_background_image']
twitters = []
twitters_data = {}
twitter_number = 0;feature_number=0;

#generate dictionary twitters_data to store data separated by features ;
for eachf in features_twitter:
    feature_number = feature_number+1;
    twitters_data[str(eachf)] = [];
#reshape raw data in inputfile;
for eachline in inputfile:
    #chking processing;
    if numpy.mod(i,100000) == 0:
        print i;
    eachline.encode('ascii','ignore')
    twitter_number = twitter_number+1; 
    twitter_content = [];
    dic = json.loads(eachline);
    data.append(dic);
    for feature in features_twitter:
        try:
            twitter_content.append(dic[feature])
            twitters_data[feature].append(dic[feature])
        except KeyError:
            twitter_content.append("Emptyyyyy")
            twitters_data[feature].append("Emptyyyyy")
    twitters.append(twitter_content)
inputfile.close()


print "Read Finished!";
print "Start Write!"

feature_noempty = {}
feature_noempty['score'] = []
hh = 0
for eachFeature in features_twitter:
    hh = hh+1
    print hh;
    feature_noempty[eachFeature] = twitters_data[eachFeature]
    for i in range(len(feature_noempty[eachFeature])): 
        try:
            if eachFeature == "source":
                tmp = feature_noempty[eachFeature][i]
                try:
                    feature_noempty[eachFeature][i] = tmp[tmp.index('>')+1:tmp.index('<',tmp.index('>'))]
                except:
                    feature_noempty[eachFeature][i] = tmp[tmp.index('<')+1:tmp.index('>',tmp.index('<'))]
            tmp2 = feature_noempty[eachFeature][i].encode('ascii','ignore')
            feature_noempty[eachFeature][i] = tmp2.strip()
            #print eachFeature
            if eachFeature == 'text':
                score = 0;
                txt = re.sub('[^A-Za-z0-9]+',' ',feature_noempty[eachFeature][i]).lower().strip().split(' ');
                for eachWord in txt:
                    try:
                        score = score + afinn_dic[eachWord];
                    except:
                        pass
                feature_noempty["score"].append(score)
        except:
            pass




'''dump the data dic into an extra file'''
json.dump(feature_noempty, open("feature_empty.txt",'w'));
