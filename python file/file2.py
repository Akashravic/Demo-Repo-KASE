try:
    with open("cont.txt","r") as fileob:
        print(fileob.read())
except Exception:
    print("Some issues happened.")