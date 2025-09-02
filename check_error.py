
# with open("app.log") as f:
#     for line in f:
#         if "error" in line.lower():
#             print(line.strip())
import re
pattern = re.compile(r"Error",re.IGNORECASE)

with open("app.log","r") as f:
    count = 0
    for line in f:
        if pattern.search(line):
            count +=1
print("no of error are",count)


