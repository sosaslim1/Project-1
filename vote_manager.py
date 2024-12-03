class VoteManager:
    def __init__(self):
        """Function that starts the vote tally while making a directory to store these votes"""
        self.candidates = {"John": 0, "Jane": 0}

    def cast_vote(self, candidate_name: str):
        """function that adds the votes to the person selcted"""
        if candidate_name in self.candidates:
            self.candidates[candidate_name] += 1
        else:
            raise ValueError(f"Candidate {candidate_name} not found!")

    def get_results(self) -> dict:
        """gets the votes from the code and counts the votes for the two people together"""
        return self.candidates
