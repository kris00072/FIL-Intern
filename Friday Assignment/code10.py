class dictConvert:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def convert(self):
        keys = list(self.dictionary.keys())
        values = list(self.dictionary.values())
        return keys, values

exampleDictionary={"KEY1":"VALUE1","KEY2":"VALUE2","KEY3":"VALUE3"}    
Lists=dictConvert(exampleDictionary) 
print(Lists.convert()) 