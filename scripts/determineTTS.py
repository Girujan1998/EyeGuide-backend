import math

def tts(hash, pathData):

    tts = []
    direction = None
    straightCounter = 0

    tts.append([pathData[0], "Starting Navigation"])
    tts.append([pathData[0], "Now navigating to " + hash[pathData[len(pathData)-1]]['name']])

    print(tts)

    straightStartNode = hash[pathData[0]]
    print("starting loop")
    for i in range(len(pathData)-2):
        
        # print("calculating turn")
        direction = calculateTurn(hash[pathData[i]], hash[pathData[i+1]], hash[pathData[i+2]])
        # print("turn calculated")

        print(direction)


        if direction == 'S':
            # print("straight")
            straightCounter+=1

        elif direction == 'L':
            # print("left detected")
            if(straightCounter != 0):
                # print("have been going straight")    
                currNode = hash[pathData[i+1]]
                dist = int(112000*distance(straightStartNode, currNode))
                # print("check dist > 10") 
                if(dist > 10):
                    # print("appending for >10 left case") 
                    tts.append([straightStartNode["guid"], "Go straight for " + str(dist) + " meters"])
                
                for j in range(i-1,0,-1):
                    dist = int(112000*distance(hash[pathData[j]], currNode))
                    if (dist >= 2):
                        # print("appending for >2 left case") 
                        tts.append([hash[pathData[j]]["guid"], "Turn left in 2 meters"])
                        break
            # print("appending turn left case")     
            tts.append([pathData[i+1],"Turn left"])
            straightStartNode = hash[pathData[i+1]]
            straightCounter = 0

        elif direction == 'R':
            # print("right detected")
            if(straightCounter != 0):
                # print("have been going straight")    
                currNode = hash[pathData[i+1]]
                dist = int(112000*distance(straightStartNode, currNode))
                # print("check dist > 10") 
                if(dist > 10):
                    # print("appending for >10 right case")
                    tts.append([straightStartNode["guid"], "Go straight for " + str(dist) + " meters"])
                
                for j in range(i-1,0,-1):
                    print("j: ", j)
                    dist = int(112000*distance(hash[pathData[j]], currNode))
                    # print("distance calculated")
                    if (dist >= 2):
                        # print("appending for >2 right case") 
                        tts.append([hash[pathData[j]]["guid"], "Turn right in 2 meters"])
                        break

            # print("appending for turn right case") 
            tts.append([pathData[i+1],"Turn right"])
            straightStartNode = hash[pathData[i+1]]
            straightCounter = 0
        # print("current state of tts:", tts)

    tts.append([pathData[len(pathData)-1], "You have arrived at " + hash[pathData[len(pathData)-1]]["name"]])
    return tts

# calculates gps distance between two given nodes
def distance (node1, node2):
    return math.sqrt((node2["lat"] - node1["lat"])**2 + (node2["long"] - node1["long"])**2)

# given that user is traveling on node path node1 -> node2 -> node3
# outputs whether this set of 3 nodes means user is walking straight, or turning right/left
def calculateTurn (node1, node2, node3):
    # print("start calculating turn function")
    leftTurn = isLeft(node1, node2, node3)
    # print("done calculating left, calculate angle")
    angle = calcAngle(node1, node2, node3)
    print("isLeft: ", leftTurn)
    print("angle:", angle)
    # print("angle calculated")
    MIN_STRAIGHT_RANGE = 135
    if(angle > MIN_STRAIGHT_RANGE):
        return "S"
    return "L" if leftTurn else "R"

# determines if node3 is to the left of the line made by connecting node1 and node2
def isLeft (node1, node2, node3):
    # note: will not work if building is on equator, prime meridian, or international date line
    crossProduct = (node2["lat"] - node1["lat"])*(node3["long"] - node1["long"]) - (node2["long"] - node1["long"])*(node3["lat"] - node1["lat"])
    condition = (node1["lat"] < 0) ^ (node1["long"] < 0)
    return crossProduct <= 0 if condition else crossProduct > 0

# calculates the angle made by the points node1, node2, node3
def calcAngle (node1, node2, node3):
    AB = math.sqrt((node2["lat"]-node1["lat"])**2 + (node2["long"]-node1["long"])**2)
    BC = math.sqrt((node2["lat"]-node3["lat"])**2 + (node2["long"]-node3["long"])**2)
    AC = math.sqrt((node3["lat"]-node1["lat"])**2 + (node3["long"]-node1["long"])**2)

    cosInput = (BC*BC+AB*AB-AC*AC)/(2*BC*AB)
    cosInput = -1 if cosInput < -1 else cosInput
    cosInput = 1 if cosInput > 1 else cosInput

    return math.acos(cosInput) * 180 / math.pi


# determines if node3 is to the left of the line made by connecting node1 and node2
def isLeftCoords (aX, aY, bX, bY, cX, cY):
    return ((bX - aX)*(cY - aY) - (bY - aY)*(cX - aX)) > 0

# calculates the angle made by the points node1, node2, node3
def calcAngleCoords (aX, aY, bX, bY, cX, cY):
    AB = math.sqrt((bX-aX)**2 + (bY-aY)**2)
    BC = math.sqrt((bX-cX)**2 + (bY-cY)**2)
    AC = math.sqrt((cX-aX)**2 + (cY-aY)**2)

    cosInput = (BC*BC+AB*AB-AC*AC)/(2*BC*AB)
    cosInput = -1 if cosInput < -1 else cosInput
    cosInput = 1 if cosInput > 1 else cosInput

    return math.acos(cosInput) * 180 / math.pi


# print(isLeftCoords(43.468836612888715, -80.54182422090803,43.468856168567555, -80.54183502439687 ,43.46886962664793, -80.54179573917715))
# print(calcAngleCoords(43.468836612888715, -80.54182422090803,43.468856168567555, -80.54183502439687 ,43.46886962664793, -80.54179573917715))