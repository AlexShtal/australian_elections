class Election:
    def __init__(self, candidates: list, votes: list):
        self.candidates = candidates
        
        formatedVotes = []
        for vote in votes:
            formatedVotes.append([candidates[i-1] for i in vote])
        self.votes = formatedVotes

    def excludeWeak(self, countedVotes: dict):
        while(countedVotes):
            weak = min(countedVotes, key=countedVotes.get)
            for vote in self.votes:
                if vote[0] == weak:
                    vote = moveLeft(vote)
                    return
            countedVotes.pop(weak)
            
            
                
    def countVotes(self) -> dict:
        results = {candidate:0 for candidate in self.candidates}
        for vote in self.votes:
            results[vote[0]]+=1
        
        return results
            
        
    def findWinner(self) -> str:
        countedVotes = self.countVotes()
        allVotes = sum(countedVotes.values())
        
        for _ in range(len(self.candidates)):
            countedVotes = self.countVotes()
            for name, votes in countedVotes.items():
                if votes/allVotes>0.50:
                    return name
            self.excludeWeak(countedVotes)
            
                   
def moveLeft(items: list) -> list:
    for index in range(1, len(items)-1):
        items[index-1] = items[index]
    items[len(items)-1] = 0
    return items

def readFile(path: list):
    result = []
    
    with open(path) as votesFile:
        numberOfTests = int(votesFile.readline())
        votesFile.readline()
        
        for testIndex in range(numberOfTests):
            numberOfCandidates = int(votesFile.readline())
            candidates = []
            for candidateIndex in range(numberOfCandidates):
                candidates.append(votesFile.readline().strip())

            votes = []
            vote = votesFile.readline().strip()
            while(vote):
                votes.append([int(num) for num in vote.split(" ")])
                vote = votesFile.readline().strip()
            
            result.append([candidates, votes])
            
    return result
      
      
data = readFile("Lab_1.4\\test.txt")     
for electionData in data:
    election = Election(*electionData)
    print(election.findWinner())
