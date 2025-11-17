candidates = {"Bush": 0, "Dukakis": 0}
shouldContinue = True
while shouldContinue:
    vote = input("For whom do you vote? (! to quit)")
    if (vote == "!"):
        break
    #check if the candidate is in the dictionary
    if (vote in candidates.keys()):
        candidates[vote] += 1
    else:
        #it's a writein
        #could stop and check if that's what they really meant
        candidates[vote] = 1
print("Here are the results")
for key in candidates:
    print(f'{key}: {candidates[key]}')

