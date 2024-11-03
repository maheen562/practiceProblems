class Solution {
    public boolean isSubsequence(String s, String t) {
        int str1Index = 0;
        char[] sArr = s.toCharArray(); // Convert string s to a character array
        
        if (s.equals("")){
            return true;
        }
        // Loop through each character of string t
        for (char ch : t.toCharArray()) {
            if (str1Index < sArr.length && ch == sArr[str1Index]) { // Check bounds and character match
                str1Index++; // Move to the next character in s
            }
            if (str1Index == sArr.length) { // If we've matched all characters in s
                return true;
            }
        }
        
        // If we didn't find all characters of s in t, return false
        return false;
    }
}