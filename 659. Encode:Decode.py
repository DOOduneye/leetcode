# Medium — Array
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
# Please implement `encode` and `decode`

# Input: `["lint","code","love","you"`]
# Output: `["lint","code","love","you"]` 
# Explanation: One possible encode method is: `"lint:;code:;love:;you"`

# O(n)
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        delimiter = "#"
        output = ""
        for word in strs:
            output += (str(len(word)) + delimiter + word)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
        i = j + 1 + length


