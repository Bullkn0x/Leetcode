'''
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""
 

Note:

S consists of lowercase English letters only.
1 <= S.length <= 1000
'''

class Solution(object):
    def removeVowels(self, S):
        vow='aeiou'
        result=''
        for i in range(len(S)):
            if S[i] not in vow:
                result+=S[i]
                
        return result
        """
        :type S: str
        :rtype: str
        """
        