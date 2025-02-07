import os

class FindFiles:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def find_text_files(self):
        
        text_files = []
        for root, _, files in os.walk(self.folder_path): 
            for file in files:
                if file.endswith('.txt'):
                    text_files.append(os.path.join(root, file))  

        return text_files

fileFinder = FindFiles("C:\\fl") 
print(fileFinder.find_text_files()) 
