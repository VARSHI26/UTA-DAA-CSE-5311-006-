class KMP:
    def search(self, pattern, text):
        M = len(pattern)
        N = len(text)
        lps = [0] * M
        j = 0 
        self.compute_lps_array(pattern, M, lps)
        i = 0  
        while (N - i) >= (M - j):
            if pattern[j] == text[i]:
                j += 1
                i += 1
            if j == M:
                print(f"Found pattern at index {i - j}")
                j = lps[j - 1]
            elif i < N and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
    def compute_lps_array(self, pattern, M, lps):
        length = 0
        i = 1
        lps[0] = 0
        while i < M:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
if __name__ == "__main__":
    text = "hello this is a test string to say hello and to pattern match word hello"
    pattern = "hello"
    KMP().search(pattern, text)
