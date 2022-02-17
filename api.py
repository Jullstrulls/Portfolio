import json, os

#returns json file loaded
def load(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data 
        
def get_techniques(data):
    techniques = []
    for project in data:
        for technique in project["techniques_used"]:
            if technique not in techniques:
                techniques.append(technique)
    return techniques

def get_project(data, id):
    for project in data:
        if project["id"] == id:
            return project
    return {}