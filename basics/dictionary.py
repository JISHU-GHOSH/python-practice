capitals={"usa":"washinton dc",
          "india":"delhi",
          "china":"beijing",
          "russia":"moscow"}



print(capitals.get("usa"))
print()

if capitals.get("japan"):
    print("key in dic")
else:
    print("key not in dic")
print()

capitals.update({"china":"laupai"})#updates something in the dic
print()

for country,capital in capitals.items():
    print(country,":",capital)
print()    

capitals.pop("china")#remove something in dic
print(capitals)

#capitals.clear()# clears dic

keys=capitals.keys()
print(keys)

values=capitals.values()
print(values)