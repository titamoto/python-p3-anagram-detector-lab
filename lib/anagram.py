class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, list):
        answer = []
        for w in list:
            if sorted([letter for letter in self.word]) == sorted([letter for letter in w]):
                answer.append(w)
        return answer