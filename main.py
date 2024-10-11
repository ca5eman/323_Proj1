import re

#main function for project

#list to print as output

converted_user_input = []

keywords = []

operators = []

separators = []

literals = []

identifiers = []

#lists to compare

list_keywords = ["False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield", "int", "string", "float", "bool", "list", "tuple", "dict", "set", "var"]


list_operators = [

    "+", "-", "*", "/", "//", "%", "**","==", "!=", ">", "<", ">=", "<=","and", "or", "not","&", "|", 
    "^", "~", "<<", ">>","=", "+=", "-=", "*=", "/=", "//=", "%=", "**=","&=", "|=", "^=", "<<=", ">>=",

]

list_separators = [ "(",
    ")", "[", "]", "{", "}",",", ":", ";",".", "@","->"  
]

list_literals = []

list_identifiers = []

lines = []
#file reading

print("File without comments and whitespace: \n")

# Open the file in read mode
with open('data.txt', 'r') as file:
    for line in file:
       lines = [line.strip() for line in file]
#remove comments / whitespace lines
for item in lines:
    if item == "" or item.startswith("#"):
        lines.remove(item)
print("\n".join(lines))
# the hard part is going to be figuring out what is an identifier and what is a separator


user_input = " ".join(lines)


converted_user_input = user_input.split()

# now that we have a list of strings, we have to sort what strings go to what

for item in converted_user_input:
    if item in list_keywords:
        keywords.append(item)    
    elif item in list_operators:
        operators.append(item)   
    elif item in list_separators:
        separators.append(item)         
    elif item[0] == '"':
        literals.append(item)
    elif item[0] == "'":
        literals.append(item)
    elif item.isidentifier():
        identifiers.append(item)
    else:
        literals.append(item)

#now that our lists have been made, just remove similar items
        
keywords = list(set(keywords))

operators = list(set(operators))

separators = list(set(separators))

literals = list(set(literals))

identifiers = list(set(identifiers))

#print out all of our different lexemes
print ("\nList of All Lexemes and their token type: \n")
print("Keywords: ", keywords)

print("Operators: ", operators)

print("Separators: ", separators)

print("Literals: ", literals)

print("Identifiers: ", identifiers)