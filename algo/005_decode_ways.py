"""
75. Decode Ways (Leetcode)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = {"": 1}

        def numDecodingsFromDigits(digits: list[int]) -> int:
            digits_str = "".join([str(d) for d in digits])
            try:
                return mapping[digits_str]
            except KeyError:
                pass

            value = 1

            if len(digits) == 0:
                pass
            elif len(digits) == 1:
                pass
            elif digits[0] > 2:
                value = numDecodingsFromDigits(digits[1:])
            elif digits[0] == 1:
                value = numDecodingsFromDigits(digits[1:]) + numDecodingsFromDigits(
                    digits[2:]
                )
            elif digits[1] > 6:
                value = numDecodingsFromDigits(digits[2:])
            else:
                value = numDecodingsFromDigits(digits[1:]) + numDecodingsFromDigits(
                    digits[2:]
                )

            # update mapping
            mapping[digits_str] = value
            return value

        digits = [int(c) for c in s]
        value = numDecodingsFromDigits(digits)
        return value

    def numDecodings2(self, s: str) -> int:
        n = len(s)
        memo = {}

        def dp(i: int) -> int:
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]

            # Single digit (1-9)
            result = dp(i + 1)

            # Two digits (10-26)
            if i + 1 < n and int(s[i : i + 2]) <= 26:
                result += dp(i + 2)

            memo[i] = result
            return result

        return dp(0)


assert Solution().numDecodings(s="226") == 3
assert Solution().numDecodings2(s="226") == 3
print("All test cases passed")
