import requests
from pprint import pprint
import numpy as np
from .models import College
from nltk.corpus import wordnet
from django.db import models
from itertools import product

subscription_key="a0cdcb30c0894f918d92c0de8f34d85e"
assert subscription_key

text_analytics_base_url = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0"
sentiment_api_url = text_analytics_base_url + "/sentiment"

def generate_ratings(college_reviews):
	reviews=college_reviews.split(";")
	ratingslist=[]
	for review in reviews:
		if(len(review)>1):
			documents={}
			documents['documents']=[]
			arr=documents.get('documents')
			arr.append({'id': '1', 'language':'en','text':review})
			headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
			response  = requests.post(sentiment_api_url, headers=headers, json=documents)
			sentiments = response.json()
			result=sentiments['documents']
			score=result[0]
			score=score['score']
			ratingslist.append(score)
	score_allotted=np.sum(ratingslist)/len(ratingslist)
	if(score_allotted<0.20):
		return(1)
	elif(score_allotted<0.4):
		return(2)
	elif(score_allotted<0.6):
		return(3)
	elif(score_allotted<0.8):
		return(4)
	else :
		return(5)

def recommend_college(student_income,student_interest,student_ethnic,student_score):
	stud_interest_list=student_interest.split(";")
	college_suggest=[]
	for col in College.objects.all():
		if(student_score>=int(col.score)):
			col_interest=col.specialisation.split(";")
			allsyns1 = set(ss for word in stud_interest_list for ss in wordnet.synsets(word))
			allsyns2 = set(ss for word in col_interest for ss in wordnet.synsets(word))
			best = max((wordnet.wup_similarity(s1, s2) or 0, s1, s2) for s1, s2 in product(allsyns1, allsyns2))
			measure=best[0]
	
			if(measure>0.84):
				ethnic_values=col.ethnicity.split(';')
				if(float(ethnic_values[student_ethnic]) >0.07):
					if(student_income*4*152/100 > int(col.fees)):
						college_suggest.append(col.title)
						print(college_suggest)
	return college_suggest
