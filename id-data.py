import json

f = open('data.json')
data = json.load(f)



#input type output id


x=input("Enter id:")
if x=="0001":
    print("valid")
    val = input("Enter Type:")
    for a in data[0]:
            if data[0]["batters"]["batter"][0]["type"] == val:
             print(data[0]["batters"]["batter"][0]["id"])
             break
            elif data[0]["batters"]["batter"][1]["type"] == val:
             print(data[0]["batters"]["batter"][1]["id"])
             break
            elif data[0]["batters"]["batter"][2]["type"] == val:
              print(data[0]["batters"]["batter"][2]["id"])
              break
            elif data[0]["batters"]["batter"][3]["type"] == val:
              print(data[0]["batters"]["batter"][3]["id"])
              break
            elif data[0]["topping"][0]["type"] == val:
              print(data[0]["topping"][0]["id"])
              break
            elif data[0]["topping"][1]["type"] == val:
              print(data[0]["topping"][1]["id"])
              break
            elif data[0]["topping"][2]["type"] == val:
              print(data[0]["topping"][2]["id"])
              break
            elif data[0]["topping"][3]["type"] == val:
              print(data[0]["topping"][3]["id"])
              break
            elif data[0]["topping"][4]["type"] == val:
              print(data[0]["topping"][4]["id"])
              break
            elif data[0]["topping"][5]["type"] == val:
              print( data[0]["topping"][5]["id"])
              break
            elif data[0]["topping"][6]["type"] == val:
              print(data[0]["topping"][6]["id"])
              break 
            else:
              print("Invalid value")
            break

elif x=="0002":
        print("valid")
        v = input("Enter Type:")
        for b in data[1]:
            if data[1]["batters"]["batter"][0]["type"]==v:
                print(b["batters"]["batter"][0]["id"])
                break
            elif data[1]["topping"][0]["type"] == v:
              print(data[1]["topping"][0]["id"])
              break
            elif data[1]["topping"][1]["type"] == v:
              print(data[1]["topping"][1]["id"])
              break
            elif data[1]["topping"][2]["type"] == v:
              print(data[1]["topping"][2]["id"])
              break
            elif data[1]["topping"][3]["type"] == v:
              print(data[1]["topping"][3]["id"])
              break
            elif data[1]["topping"][4]["type"] == v:
              print(data[1]["topping"][4]["id"])
              break
            else:
                print("Invalid value")
                break
elif x=="0003":
    print("valid")
    value=input("Enter Type:")
    for c in data[2]:
        if data[2]["batters"]["batter"][0]["type"] == value:
             print(data[2]["batters"]["batter"][0]["id"])
             break
        elif data[2]["batters"]["batter"][1]["type"] == value:
             print(data[2]["batters"]["batter"][1]["id"])
             break
        elif data[2]["topping"][0]["type"] == value:
              print(data[2]["topping"][0]["id"])
              break
        elif data[2]["topping"][1]["type"] == value:
              print(data[2]["topping"][1]["id"])
              break
        elif data[2]["topping"][2]["type"] == value:
              print(data[2]["topping"][2]["id"])
              break
        elif data[2]["topping"][3]["type"] == value:
              print(data[2]["topping"][3]["id"])
              break
        else:
            print("Invalid value")
            break


