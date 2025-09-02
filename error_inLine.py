with open("app.log")as f :
    for line in f:
        if "error" in line.lower():
            print(line.strip())
