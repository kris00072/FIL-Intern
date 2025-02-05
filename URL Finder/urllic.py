import re

with open(r"C:\\fl\\f2\\fidelity.txt", "r") as fs:
    fileContent = fs.read()
    print("File Content:\n", fileContent)

  
    versionPattern = r"\w*v\d+\.\d+\.\d+"  

    
    valid_versions_in_file = re.findall(versionPattern, fileContent)
    print("\nValid Versions in file:", valid_versions_in_file)

#clientserver based models - Study It
