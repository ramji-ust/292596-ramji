# Strops - A String Operations Module

## 📌 Overview
`strops` is a lightweight Python module that provides various string operations such as substring span detection, word reversal, punctuation removal, and more.

## 🚀 Features
- **getspan(s, ss)** → Find the start and end indices of a substring.
- **reverseWords(s)** → Reverse the words in a sentence.
- **removePunctuation(s)** → Remove all punctuation from a string.
- **countWords(s)** → Count the number of words in a string.
- **charecterMap(s)** → Generate a character frequency map.
- **makeTitle(s)** → Convert a string to title case.
- **normalizeSpaces(s)** → Replace multiple spaces with a single space.
- **transform(s)** → Custom transformation (default: lowercase and remove spaces).
- **getPermutations(s)** → Generate all unique permutations of a string.

## 🛠 Installation
# Clone the repository:
git clone https://github.com/yourusername/strops.git
cd strops_project

# Create a virtual environment:
python -m venv venv

# Activate the virtual environment:
venv\Scripts\activate

# Install the module
pip install .

## Usage

import strops.strops as st

s = "Hello, world! Welcome to the hackathon"
ss = "world"

# Find the span of a substring
print(st.getspan(s, ss))  # Output: (7, 12)

# Reverse words
print(st.reverseWords(s))  # Output: "hackathon the to Welcome world! Hello,"

# Remove punctuation
print(st.removePunctuation(s))  # Output: "Hello world Welcome to the hackathon"

# Count words
print(st.countWords(s))  # Output: 6

# Get character frequency map
print(st.charecterMap(s))

# Convert to title case
print(st.makeTitle(s))  # Output: "Hello, World! Welcome To The Hackathon"

# Normalize spaces
print(st.normalizeSpaces(s))

# Transform string
print(st.transform(s))

# Get string permutations
print(st.getPermutations("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
