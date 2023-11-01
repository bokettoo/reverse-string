string = input("type something ")
reversed_string = ""
for i in range(len(string) - 1, -1, -1):
  reversed_string=reversed_string + string[i]
print(reversed_string)
