#solved
class Solution:
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        # constraints
        # keep the translation in dict
        # exceptions

        if len(s) == 1:
            return self.roman_dict[s]

        converted_int = 0
        i = 0
        while i < len(s):
            curr = s[i]
            _next = s[i]
            if i != len(s) - 1:
                _next = s[i + 1]
            if (curr == "I" and _next == "V") or (curr == "I" and _next == "X"):
                # exception 1
                converted_int += self.roman_dict[_next] - self.roman_dict[curr]
            elif (curr == "X" and _next == "L") or (curr == "X" and _next == "C"):
                # exception 2
                converted_int += self.roman_dict[_next] - self.roman_dict[curr]
            elif (curr == "C" and _next == "D") or (curr == "C" and _next == "M"):
                # exception 3
                converted_int += self.roman_dict[_next] - self.roman_dict[curr]
            # genereal case
            else:
                converted_int += self.roman_dict[curr]
                i += 1
                continue
            i += 2
        return converted_int
