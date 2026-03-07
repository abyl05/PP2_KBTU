import re
#1
s = input()
if re.fullmatch(r"ab*", s):
    print("Match")
else:
    print("No match")


#2
s = input()
if re.fullmatch(r"ab{2,3}", s):
    print("Match")
else:
    print("No match")


#3
s = input()
matches = re.findall(r"[a-z]+_[a-z]+", s)
print(matches)


#4
s = input()
matches = re.findall(r"[A-Z][a-z]+", s)
print(matches)


#5
s = input()
if re.fullmatch(r"a.*b", s):
    print("Match")
else:
    print("No match")


#6
s = input()
result = re.sub(r"[ ,\.]", ":", s)
print(result)


#7
s = input()
parts = s.split('_')
camel = parts[0] + ''.join(word.capitalize() for word in parts[1:])
print(camel)


#8
s = input()
parts = re.split(r"(?=[A-Z])", s)
print(parts)


#9
s = input()
result = re.sub(r"(?<!^)(?=[A-Z])", " ", s)
print(result)


#10
s = input()
result = re.sub(r"([A-Z])", r"_\1", s).lower()
if result.startswith('_'):
    result = result[1:]
print(result)