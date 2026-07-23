class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        answer = [""] * len(words)
        for word in words:
            position = int(word[-1]) - 1
            answer[position] = word[:-1]
        return " ".join(answer)