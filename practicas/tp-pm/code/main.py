import pm
print(pm.existChar("hola", "c"))
print(pm.isPalindrome("hooh"))
print(pm.getBiggestIslandLen("hhhhhhoola2222dd"))
print(pm.isAnagram("holaaas", "aaasloh"))
print(pm.isAnagram("holaaas", "aaasldh"))
print(pm.verifyBalancedParentheses("())()()()()"))
print(pm.verifyBalancedParentheses("()()()()()"))
print(pm.verifyBalancedParentheses(")()()()()()"))
print(pm.verifyBalancedParentheses("(()()()()())"))
print(pm.reduceLen("aabcddefffffg"))
print(pm.reduceLen("aaaaaaaaaaaa"))
print(pm.reduceLen("aaaaaaaaaaa"))
print(pm.reduceLen("aadaaeaafaadaaaaa"))
print(pm.isContained("asslrdcrveldsajsac", "arveja"))
print(pm.isContained("asslrdcrveldsajsc", "arveja"))
print(pm.isContained("asslrdcrveldsajsca", "arveja"))
print(pm.isContained("aarvejasslrdcrveldsajsca", "arveja"))
print("-isPatternContained-")
print(pm.isPatternContained("holamigo", "hqaigo", "q"))
print(pm.isPatternContained("holamigo", "hqaigo", "a"))
print(pm.isPatternContained("holamigo", "hqaigoo", "q"))
print(pm.isPatternContained("holamiigo", "hqaigo", "q"))

print(pm.biggestPrefix("asdjasjdasjholasdkasjdasj", "hodlas"))
print(pm.biggestPrefix("ababacasdad", "ababaca"))
print(pm.biggestPrefix("absabcababacasdad", "ababaca"))

print(pm.KMP("asdjasjdasjholasdkasjdasj", "hodlas"))
print(pm.KMP("ababacasdad", "ababaca"))
print(pm.KMP("absabcababacasdad", "ababaca"))
print(pm.finiteAutomatonMatcher("asdbaababaca", "ababaca"))
print(pm.finiteAutomatonMatcher("asdbaababaca", "ababdaca"))
print(pm.finiteAutomatonMatcher("asdbaababaca", "ab"))