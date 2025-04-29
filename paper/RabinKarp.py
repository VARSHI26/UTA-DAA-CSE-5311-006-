class RabinKarp:
    def __init__(self):
        self.d = 256  
    def search(self, pattern, text, primeNumber):
        M = len(pattern)
        N = len(text)
        p = 0 
        t = 0  
        h = 1
        for i in range(M - 1):
            h = (h * self.d) % primeNumber
        for i in range(M):
            p = (self.d * p + ord(pattern[i])) % primeNumber
            t = (self.d * t + ord(text[i])) % primeNumber
        for i in range(N - M + 1):
            if p == t:
                match = True
                for j in range(M):
                    if text[i + j] != pattern[j]:
                        match = False
                        break
                if match:
                    print(f"Pattern found at index {i}")
            if i < N - M:
                t = (self.d * (t - ord(text[i]) * h) + ord(text[i + M])) % primeNumber
                if t < 0:
                    t += primeNumber
if __name__ == "__main__":
    text = "hello this is a test string to say hello and to pattern match word hello"
    pattern = "hello"
    RabinKarp().search(pattern, text, 101)
