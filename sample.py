import json
f = open('data.json')
data = json.load(f)
# print(data[0]["batters"]["batter"][2]["id"])
# print(data[0]["topping"][2]["type"])

def sample():
   # try :
        if id=="0001":
            if val :
                if int(val) in range(1001,1010):
                    s=int(val[-1])-1
                    print(data[0]["batters"]["batter"][int(s)]["type"])
                else:
                    if int(val) in range(5001,5010):
                        s=int(val[-1])-1
                        print(data[0]["topping"][int(s)]["type"])

                    
            
        if id=="0002":
            if val :
                if int(val) in range(1001,1999):
                    s=int(val[-1])-1
                    print(data[1]["batters"]["batter"][int(s)]["type"])
                else:
                    if int(val) in range(5001,6000):
                        s=int(val[-1])-1
                        print(data[1]["topping"][int(s)]["type"])

            
        if id=="0003":
            if val:
                if int(val) in range(1001,1999):
                    s=int(val[-1])-1
                    print(data[2]["batters"]["batter"][int(s)]["type"])  
                else:
                    if int(val) in range(5001,6000):
                        s=int(val[-1])-1
                        print(data[2]["topping"][int(s)]["type"])
                        
   # except IndexError:
      #  print("not valid")
        
    
    
id=input("Enter the ID: ")   
print(id,"Valid Data")

val=input("Enter the VALUE id: ")

sample()