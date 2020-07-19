

'''
Code to load model and pass values in it to predict result 

filename = 'breast_cancer_model.pkl'
# pickle.dump(model, open(filename, 'wb'))

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

15.30,25.27,102.40,732.4,0.10820,0.16970,0.16830,0.08751,0.1926,0.06540,0.4390,1.0120,3.498,43.50,0.005233,0.030570,0.03576,0.010830,0.01768,0.002967,20.27,36.71,149.30,1269.0,0.1641,0.61100,0.63350,0.20240,0.4027,0.09876

predict_value=loaded_model.predict([[
        12.34,22.22,79.85,464.5,0.10120,0.10150,0.05370,0.02822,0.1551,0.06761,0.2949,1.6560,1.955,21.55,0.011340,0.031750,0.03125,0.011350,0.01879,0.005348,13.58,28.68,87.36,553.0,0.1452,0.23380,0.16880,0.08194,0.2268,0.09082
    ]])
print(predict_value[0])

'''


# save csv file data into mongodb https://gist.github.com/mprajwala/849b5909f5b881c8ce6a

# mongodb+srv://admin:<password>@breastcancerdetection.h1ao7.mongodb.net/<dbname>?retryWrites=true&w=majority


# mongo database name - breastcancerdetection

import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:admin@breastcancerdetection.h1ao7.mongodb.net/breastcancerdetection?retryWrites=true&w=majority")
db = client['breastcancerdetection']
collection = db['breastcancerdetection']
# user_dict = {"_id": 100, "name": "Hemant"}
# collection.insert_one(user_dict)
# print(collection)

# import json
# # import pymongo
# import pandas as pd
# myclient = pymongo.MongoClient()

# df = pd.read_csv('Breast Cancer-Kaggle.csv',encoding = 'ISO-8859-1')
# df.to_json('yourjson.json')
# print(df.head())
# jdf = open('yourjson.json').read()
# for x in collection.find({},{ "id": 842302 }):
# 	print(x)
# # data = json.loads(jdf)  
# # collection.insert_one(data)


import csv
import json
import pandas as pd
# import sys, getopt, pprint
# from pymongo import MongoClient
#CSV to JSON Conversion
# csvfile = open('Breast Cancer-Kaggle.csv', 'r')
# reader = csv.DictReader( csvfile )
# mongo_client=MongoClient() 
# db=mongo_client.october_mug_talk
# db.segment.drop()
# header= [ 'id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean',
#        'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
#        'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
#        'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
#        'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
#        'fractal_dimension_se', 'radius_worst', 'texture_worst',
#        'perimeter_worst', 'area_worst', 'smoothness_worst',
#        'compactness_worst', 'concavity_worst', 'concave points_worst',
#        'symmetry_worst', 'fractal_dimension_worst']

# for each in reader:
#     row={}
#     for field in header:
#         row[field]=each[field]

#     collection.insert_one(row)



################# Find single Records#####################
# bills_post = collection.find_one({'id': "92751"})
# print(bills_post)


df = pd.DataFrame(list(collection.find()))
print(df.head())
print(df.shape)
