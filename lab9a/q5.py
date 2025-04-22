def filterFaculty(faculty:list):
    return list(filter(lambda x: True if len(x)>8 else False, faculty))
print(filterFaculty(["dfkjgjvf","FISJDSWWR","refffefee","AASDF","Dsdfdfdfrgdafjdgjgi"]))
