import requests
from pprint import pprint
import numpy as np
from .models import College,Counsellor
from nltk.corpus import wordnet
from django.db import models
from itertools import product
import httplib2,urllib
import json,os
from azure.storage.blob import BlockBlobService, PublicAccess
subscribe_entity="70d88b730e4944429c03697f8d4587f4"
subscription_key_img = "25fcd5bc41aa4995998304649f8646f7"
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
	return college_suggest

def image_search(interests,college):   
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key_img}
    searchterm=college+" "+ interests
    params  = {"q": searchterm, "license": "public", "imageType": "photo"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    result=[]
    if('queryExpansions' in search_results.keys()):
        for i in search_results['queryExpansions']:
            result.append(i['thumbnail']['thumbnailUrl'])
    return result

    
def get_suggestions (query):
    host = 'api.cognitive.microsoft.com'
    path = '/bing/v7.0/entities'
    mkt = 'en-US'
    params = '?mkt=' + mkt + '&q=' + urllib.pathname2url (query)
    headers = {'Ocp-Apim-Subscription-Key': subscribe_entity}
    conn = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
    result=conn.request ("https://api.cognitive.microsoft.com/"+path+params,'GET',headers=headers)[1]
    result=result.decode('utf8')
    #response = conn.getresponse ()
    #result=response.read ()
    json_array=json.dumps(json.loads(result), indent=4)
    json_obj=json.loads(json_array)
    print()
    result={}
    for key in json_obj:
        if key=="queryContext":
            result["name"]=json_obj[key]["originalQuery"]
        if key=="entities":
            res=json_obj[key]["value"]
            for i in res:
                key=i.keys()
                if "contractualRules" in key :
                    contractVal=i["contractualRules"][1]
                    if contractVal["text"]=="Wikipedia":
                        result["wikiurl"]=contractVal["url"]
                if "image" in key:
                    imageVal=i["image"]
                    imageKey=imageVal.keys()
                    if "thumbnailUrl" in imageKey:
                        result["image"]=imageVal["thumbnailUrl"]
                    if "hostPageUrl" in imageKey:
                        result["logo"]=imageVal["hostPageUrl"]
                    if "provider" in imageKey:
                        provVal=imageVal["provider"]
                        for p in provVal:
                            keyp=p.keys()
                            if "url" in keyp:
                                result["web"]=p["url"]
                if "description" in key:
                    result["desciption"]=i["description"]
    return result
def handle_uploaded_file(filename,container_name):
    block_blob_service = BlockBlobService(account_name='storagedocs', account_key='D91eaRC0yUX8OUAr3zYzWON2EDdsn1pKhlDoO3ZU4z5yDEBP+nS2CVxRHrmvW8zf0k4GQPzdLehAJfGc9tezJA==') 
    container_name = container_name
    block_blob_service.create_container(container_name) 
    block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)
    local_file_name = filename
    full_path_to_file = os.path.join('/home/w1zard/Documents/Student-Connect/', local_file_name)
    block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file)
    counsellor_name=filename.split(".")[0]
    print(counsellor_name)

def retrieve_file_azure(filename,container_name):
    block_blob_service = BlockBlobService(account_name='storagedocs', account_key='D91eaRC0yUX8OUAr3zYzWON2EDdsn1pKhlDoO3ZU4z5yDEBP+nS2CVxRHrmvW8zf0k4GQPzdLehAJfGc9tezJA==') 
    full_path_to_file2 = os.path.join('/home/w1zard/Documents/Student-Connect/dashboard/documents/',filename)
    print("\nDownloading blob to " + full_path_to_file2)
    block_blob_service.get_blob_to_path(container_name, filename, full_path_to_file2)
    
