import strops.strops as st

# Take input from user
s = input("Enter the main string: ")
ss = input("Enter the substring: ")

# Display the span of the substring
span = st.getspan(s, ss)
print(f"Span of substring '{ss}' in '{s}': {span}")

# Test other functions
print("Reversed words:", st.reverseWords(s))
print("Without punctuation:", st.removePunctuation(s))
print("Word count:", st.countWords(s))
print("Character frequency map:", st.charecterMap(s))
print("Title case:", st.makeTitle(s))
print("Normalized spaces:", st.normalizeSpaces(s))
print("Transformed string:", st.transform(s))
print("String permutations:", st.getPermutations(s))
