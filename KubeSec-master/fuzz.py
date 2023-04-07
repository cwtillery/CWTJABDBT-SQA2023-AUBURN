import graphtaint.py as g

# Fuzz.py performs fuzzing on 5 methods contained in the graphtaint.py file

# Method 1 - getYAMLFiles()
input1 = [2, 'Hello World!', [7]]

for i in range(len(input1)):
  try:
    res = g.getYAMLFiles(input1(i))
    print(res)
  except Exception as e: print(str(e))


# Method 2 - constructHelmString()
input2 = [(1, "two", 3), None, "string"]

for i in range(len(input2)):
  try:
    res = g.constructHelmString(input2(i))
    print(res)
  except Exception as e: print(str(e))

# Method 3 - getHelmTemplateContent()
input3 = ['random/directory', None, (7, 2)]

for i in range(len(input3)):
  try:
    res = g.getHelmTemplateContent(input3(i))
    print(res)
  except Exception as e: print(str(e))

# Method 4 - getMatchingTemplates()
input4 = [0, "String", None]
input4_2 = [("tu", "ple"), "🐵 🙈 🙉 🙊", None]

for i in range(len(input4)):
  try:
    res = g.getMatchingTemplates(input4(i), input4_5(i))
    print(res)
  except Exception as e: print(str(e))

# Method 5 - getValidTaints()
input5 = ["Not a List", ['invalid list', 2], None]

for i in range(len(input5)):
  try:
    res = g.getValidTaints(input5(i))
    print(res)
  except Exception as e: print(str(e))
