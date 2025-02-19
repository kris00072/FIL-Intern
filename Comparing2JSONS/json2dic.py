class JsonTODic:
    def __init__(self,json1,json2):
        self.json1=json1
        self.json2=json2

    def getKeyDifference(self):
        keys1=set(self.json1.keys())
        keys2=set(self.json2.keys())

        keys_only_in_json1=keys1-keys2
        keys_only_in_json2=keys2-keys1

        return {
            "keys_only_in_json1":list(keys_only_in_json1),
            "keys_only_in_json2":list(keys_only_in_json2)
        }

#json1={
    #'name':"kartikey",
    #'class':"first",
    #'cast':'podcast'
#}#

#json2={
    #'name':"krishan",
    #'degree':"Tech",
    #'sport':'soccer'
#} #

import json
with open("Comparing2JSONS/test.json", 'r') as file1, open("Comparing2Jsons/test2.json", 'r') as file2:
    json1 = json.load(file1)  
    json2 = json.load(file2)  


result = JsonTODic(json1, json2)


data = result.getKeyDifference()


print(data)

