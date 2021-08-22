import json


def getComments(filename):
  with open(filename) as jsonFile:
    file = json.load(jsonFile)
    jsonFile.close()

  logs = []
  for item in file['reviews']:
    if item['IS_META_REVIEW'] == False:
      if 'RECOMMENDATION' in item and 'REVIEWER_CONFIDENCE' in item:
        logs.append(item['comments'])
  text = logs[:len(logs)//2] # return first half only             
  all_text = ' '.join(text)        
  return all_text

def getReviewFinal(filename):
  with open(filename) as jsonFile:
    file = json.load(jsonFile)
    jsonFile.close()
  return file['accepted']

def getPaper(filename):
  with open(filename) as jsonFile:
    file = json.load(jsonFile)
    jsonFile.close()
  if not file['metadata']['sections'] is None:
    text=[x['text'] for x in file['metadata']['sections']] 
    all_text = ' '.join(text)
    return all_text
    
def getReviewScore(filename):
    with open(filename) as jsonFile:
        file = json.load(jsonFile)
        jsonFile.close()

    logs = []
    for item in file['reviews']:
        if item['IS_META_REVIEW'] == False:
            if 'RECOMMENDATION' in item and 'REVIEWER_CONFIDENCE' in item:
                logs.append(item['RECOMMENDATION'])
    return round(sum(logs)/len(logs))            