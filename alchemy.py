print('''
Welcome to alchemy!!! Combine the 4 basic elements (earth, water, air, fire) to make new products!
''')




items = [
["earth", "", ""],
["water", "", ""],
["air", "", ""],
["fire", "", ""],
["steam", "water", "fire"],
["bubbles", "water", "air"],
["river", "earth", "water"],
["lava", "fire", "earth"],
["smoke", "fire", "air"],
["sauna", "steam", "earth"],
["waterfall", "river", "air"],
["metal", "lava", "earth"],
["rust", "metal", "air"],
["bacteria", "river", "bubbles"],
["obsidian", "lava", "water"],
["atmosphere", "earth", "sauna"],
["life", "bacteria", "atmosphere"],
["tree", "life", "water"],
["wood", "tree", "obsidian"],
["spear", "wood", "obsidian"],
["death", "spear", "life"],
["engine", "steam", "metal"],
["vehicle", "engine", "metal"],
["","",""]
]

madeitems = [
["earth", "", ""],
["water", "", ""],
["air", "", ""],
["fire", "", ""]
]


while True:

    print("\n")
    source1 = input("Item: ")
    source2 = input(source1 + " + ")
    print("\n")

    if (source1 == "quit" or source2 == "quit"):
        break

    i = 0

    for i in range(len(items)-1):
        if (source1 == items[i][1] and source2 == items[i][2]) or (source2 == items[i][1] and source1 == items[i][2]):
            
            madeitems.append(items[i])
            #look up how to remove newly madeitem from items list something like del [:-1]
            
            print(f"You have synthesized {items[i][0]}! \n")
            break
        elif (i == len(items)-2):
            print("That doesn't seem to work :< \n")
            
            
    
    print("@@@|\------------------------------------/|@@@ \n Elements made:")
    for i in range(len(madeitems)):
        print(madeitems[i][0], end=", ")


