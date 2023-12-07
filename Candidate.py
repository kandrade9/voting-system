class Candidate:
    def __init__(self, name):
        self.name = name
        self.vote_count = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return self.name

    def get_vote_count(self):
        return self.vote_count

    def __repr__(self):
        return self.name + ": " + str(self.get_vote_count())

