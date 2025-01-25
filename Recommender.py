import random
data = [
    {
        "number": 0,
        "name": "",
        "tags": ["dp", "array"],
        "url": "www.problem/sjksjkskjs",
        "status": True
    }
]

def getAllTags(data):
    tags= set()
    for d in data:
        for tag in d.tags:
            tags.add(tag)
    return list(tags)


def getTagRatios(data):
    #all,solved 
    tags = {tag:[0,0] for tag in getAllTags(data)}

    for d in data:
        for tag in d.tags:
            tags[tag][0] += 1
            if d.solved:
                tags[tag][1] += 1
    return tags

def getTagProblemLists(data): # includes list of all problems
    tags = {tag:[] for tag in getAllTags(data)}
    for d in data:
        for tag in d.tags:
            tags[d.tag].append(d)
    return tags
    

class Card:
    def __init__(self,tag,priority):
        self.tag = tag
        self.priority = priority
    
    
        

class RecommendQueue:
    def insert_card(card):
        pass
    def get_card():
        return Card("a",1)
        
    def update_priority(solved,tags):
        pass

class RecommendationSystem:
    class Problem:
        def __init__(self, id, name, tags, url, solved):
            self.id = id
            self.name = name
            self.tags = tags
            self.url = url
            self.solved = solved

    def initialise_recc(self,data):
        tagRatio = getTagRatios(data)
        priorities = []
        for t,(all,solved) in tagRatio:
            if all == 0:
                ratio = 1
            else:
                ratio = solved/all
            priorities.append([ratio,t])
        
        priorities.sort()
        priorities = [[i,p] for i,(p,tag) in enumerate(priorities)]
        self.Q = RecommendQueue()
        for i,t in priorities:
            card = Card(t,i)
            self.Q.insert_card(card)
        
        self.tagProblemList = getTagProblemLists(data)
        

        return 
            
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.data = []
        self.getProblemById = {}  # Initialize the dictionary

        for d in raw_data:
            p_id = d["number"]
            p_name = d["name"]
            p_tags = d["tags"]
            p_url = d["url"]
            p_solved = d["status"]
            p = RecommendationSystem.Problem(
                p_id,
                p_name,
                p_tags,
                p_url,
                p_solved
            )
            self.data.append(p)
            self.getProblemById[p.id] = p  # Populate the dictionary
        self.initialise_recc(self.data)
        

    def get_problem(self):
        tag = self.Q.get_card()
        if tag in self.tagProblemList:
            randi = random.randint(0, len(self.tagProblemList[tag])-1)
            problem = list(self.tagProblemList[tag])[randi]
            return problem
        raise KeyError

    def update_tags(self,tags):
        self.Q.update_priority(tags)

        
            
R = RecommendationSystem(data)
print(R.tst())
