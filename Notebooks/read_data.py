import json, pickle, os

# cd drive/MyDrive/'Colab Notebooks'/Thesis/PeerRead/code/accept_classify/

# Train Data and Target

p_train_path = "../../data/iclr_2017/train/parsed_pdfs/"
p_train_file = lambda f: p_train_path+f
p_train_file_names = os.listdir(p_train_path)

r_train_path = "../../data/iclr_2017/train/reviews/"
r_train_file = lambda f: r_train_path+f
r_train_file_names = os.listdir(r_train_path)

def getPaper(name):
  with open(p_train_file(name)) as jsonFile:
    file = json.load(jsonFile)
    jsonFile.close()
  if not file['metadata']['sections'] is None:
    text=[x['text'] for x in file['metadata']['sections']] 
    all_text = ' '.join(text)
    return all_text

def getReviewFinal(name):
  with open(r_train_file(name)) as jsonFile:
    file = json.load(jsonFile)
    jsonFile.close()
  return file['accepted']

train_data   = []
train_target = []
for id,name in enumerate(tqdm(p_train_file_names)):
   if getPaper(name):
     train_data.append(getPaper(name))
     train_target.append(getReviewFinal(r_train_file_names[id]))
     
# Validation Data and Target
p_valid_path = "../../data/iclr_2017/dev/parsed_pdfs/"
p_valid_file = lambda f: p_valid_path+f
p_valid_file_names = os.listdir(p_valid_path)

r_valid_path = "../../data/iclr_2017/dev/reviews/"
r_valid_file = lambda f: r_valid_path+f
r_valid_file_names = os.listdir(r_valid_path)

def getPaper(name):
  with open(p_valid_file(name)) as jsonFile:
    file = json.load(jsonFile)
    jsonFile.close()
  if not file['metadata']['sections'] is None:
    text=[x['text'] for x in file['metadata']['sections']] 
    all_text = ' '.join(text)
    return all_text

def getReviewFinal(name):
  with open(r_valid_file(name)) as jsonFile:
    file = json.load(jsonFile)
    jsonFile.close()
  return file['accepted']

val_data   = []
val_target = []
for id,name in enumerate(tqdm(p_valid_file_names)):
   if getPaper(name):
     val_data.append(getPaper(name))
     val_target.append(getReviewFinal(r_valid_file_names[id]))
     
# Test Data

p_test_path = "../../data/iclr_2017/test/parsed_pdfs/"
p_test_file = lambda f: p_test_path+f
p_test_file_names = os.listdir(p_test_path)

r_test_path = "../../data/iclr_2017/test/reviews/"
r_test_file = lambda f: r_test_path+f
r_test_file_names = os.listdir(r_test_path)

def getPaper(name):
  with open(p_test_file(name)) as jsonFile:
    file = json.load(jsonFile)
    jsonFile.close()
  if not file['metadata']['sections'] is None:
    text=[x['text'] for x in file['metadata']['sections']] 
    all_text = ' '.join(text)
    return all_text

def getReviewFinal(name):
  with open(r_test_file(name)) as jsonFile:
    file = json.load(jsonFile)
    jsonFile.close()
  return file['accepted']

test_data   = []
test_target = []
for id,name in enumerate(tqdm(p_test_file_names)):
   if getPaper(name):
     test_data.append(getPaper(name))
     test_target.append(getReviewFinal(r_test_file_names[id]))
     
     
# ONCE ONLY
all_data = [train_data, train_target, val_data, val_target, test_data, test_target]
with open('../../my_data/01-Paper-Acceptance/paper_review', 'wb') as f:
   pickle.dump(all_data, f)  

# with open('../../my_data/01-Paper-Acceptance/paper_review', "rb") as f:
#  all_data=pickle.load(f)
# train_data, train_target, val_data, val_target, test_data, test_target = all_data     
     
