class VoteManager:
    def __init__(self):
        self.candidates = {"John": 0, "Jane": 0}

    def cast_vote(self, candidate_name: str):
        if candidate_name in self.candidates:
            self.candidates[candidate_name] += 1
        else:
            raise ValueError(f"Candidate {candidate_name} not found!")

    def get_results(self) -> dict:
        return self.candidates
