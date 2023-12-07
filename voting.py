import Candidate

num_of_candidates = int(input("Number of candidates: "))
list_of_candidates = []
candidate_strings = []
for i in range(num_of_candidates):
    candidate_name = input(f"Name of candidate {i + 1}: ").lower()
    list_of_candidates.append(Candidate(candidate_name))
    candidate_strings.append(candidate_name)
print(list_of_candidates)

num_of_voters = int(input("Number of voters: "))
while num_of_voters <= 0:
    num_of_voters = int(input("Number of voters GREATER than 0: "))

user_votes = []
i = 0
while i < num_of_voters:
    vote = input("Vote: ")
    user_votes.append(vote.lower())
    i += 1

def vote(votes, candidates):
    for vote in votes:
        if vote in candidates:
            index = candidates.index(vote)
            candidate = list_of_candidates[index]
            candidate.vote_count += 1
    return list_of_candidates

print(vote(user_votes, candidate_strings))





