import json

f = open('data.json')
data = json.load(f)

#input id output type

x=input("Enter id:")
if x=="0001":
    print("valid")
    val = input("Enter value:")
    for a in data[0]:
            if data[0]["batters"]["batter"][0]["id"] == val:
             print(data[0]["batters"]["batter"][0]["type"])
             break
            elif data[0]["batters"]["batter"][1]["id"] == val:
             print(data[0]["batters"]["batter"][1]["type"])
             break
            elif data[0]["batters"]["batter"][2]["id"] == val:
              print(data[0]["batters"]["batter"][2]["type"])
              break
            elif data[0]["batters"]["batter"][3]["id"] == val:
              print(data[0]["batters"]["batter"][3]["type"])
              break
            elif data[0]["topping"][0]["id"] == val:
              print(data[0]["topping"][0]["type"])
              break
            elif data[0]["topping"][1]["id"] == val:
              print(data[0]["topping"][1]["type"])
              break
            elif data[0]["topping"][2]["id"] == val:
              print(data[0]["topping"][2]["type"])
              break
            elif data[0]["topping"][3]["id"] == val:
              print(data[0]["topping"][3]["type"])
              break
            elif data[0]["topping"][4]["id"] == val:
              print(data[0]["topping"][4]["type"])
              break
            elif data[0]["topping"][5]["id"] == val:
              print(data[0]["topping"][5]["type"])
              break
            elif data[0]["topping"][6]["id"] == val:
              print(data[0]["topping"][6]["type"])
              break 
            else:
              print("Invalid value")
            break

elif x=="0002":
        print("valid")
        v = input("Enter value:")
        for b in data[1]:
            if data[1]["batters"]["batter"][0]["id"]==v:
                print(b["batters"]["batter"][0]["type"])
                break
            elif data[1]["topping"][0]["id"] == v:
              print(data[1]["topping"][0]["type"])
              break
            elif data[1]["topping"][1]["id"] == v:
              print(data[1]["topping"][1]["type"])
              break
            elif data[1]["topping"][2]["id"] == v:
              print(data[1]["topping"][2]["type"])
              break
            elif data[1]["topping"][3]["id"] == v:
              print(data[1]["topping"][3]["type"])
              break
            elif data[1]["topping"][4]["id"] == v:
              print(data[1]["topping"][4]["type"])
              break
            else:
                print("Invalid value")
                break
elif x=="0003":
    print("valid")
    value=input("Enter Value:")
    for c in data[2]:
        if data[2]["batters"]["batter"][0]["id"] == value:
             print(data[2]["batters"]["batter"][0]["type"])
             break
        elif data[2]["batters"]["batter"][1]["id"] == value:
             print(data[2]["batters"]["batter"][1]["type"])
             break
        elif data[2]["topping"][0]["id"] == value:
              print(data[2]["topping"][0]["type"])
              break
        elif data[2]["topping"][1]["id"] == value:
              print(data[2]["topping"][1]["type"])
              break
        elif data[2]["topping"][2]["id"] == value:
              print(data[2]["topping"][2]["type"])
              break
        elif data[2]["topping"][3]["id"] == value:
              print(data[2]["topping"][3]["type"])
              break
        else:
            print("Invalid value")
            break