def main():
    print('Main function called.')

    # stores the list of gesture locations of all placed nodes
    listOfGestures = []

    # stores the newly generated gps coordinates
    newGpsArr = []

    # stores the four corners' gps locations
    gpsArr = []

    insertToList(gpsArr, 43.474638, -80.545803)  # Top Left
    insertToList(gpsArr, 43.475416, -80.54362)   # Top Right
    insertToList(gpsArr, 43.475079, -80.543384)  # Bottom Right
    insertToList(gpsArr, 43.474301, -80.545574)  # Bottom Left

    # stores the four corners' gesture locations
    gesturePos = []

    insertGesturePos(gesturePos, 1, 1)   # Top Left
    insertGesturePos(gesturePos, 13, 1)  # Top Right
    insertGesturePos(gesturePos, 13, 6)  # Bottom Right
    insertGesturePos(gesturePos, 1, 6)   # Bottom Left

    # gets the index of the top left, top right, and bottom left nodes
    topLeftIndex = topLeftNode(gesturePos)
    topRightIndex = topRightNode(gesturePos)
    bottomLeftIndex = bottomLeftNode(gesturePos)

    # calculates the ratio of meters to gesture coordinates (units are m/gesture)
    xLongRatio, xLatRatio, yLongRatio, yLatRatio = calcLongAndLatConversions(gpsArr, gesturePos, topLeftIndex, topRightIndex, bottomLeftIndex)

    # iterates through all gestures
    for gesture in listOfGestures:
        # calculates the difference in gesture positioning between the top left corner and the current gesture
        diffX = gesture['x'] - gesturePos[topLeftIndex]['x']
        diffY = gesture['y'] - gesturePos[topLeftIndex]['y']

        # takes the gps values of the top left corner and adds on the gesture difference times the ratio in both x and y
        newLong = gpsArr[topLeftIndex]['long'] + (diffX * xLongRatio) + (diffY * yLongRatio)
        newLat = gpsArr[topLeftIndex]['lat'] + (diffX * xLatRatio) + (diffY * yLatRatio)

        # adds gps coordinate to the newGPSArr list
        insertToList(newGpsArr, newLong, newLat)
    
    # prints out all gps coordinates
    for gps in newGpsArr:
        print(gps["long"], ",", gps["lat"])



    # G's code!!!

    # x = 72  # Gesture X Location
    # y = 33  # Gesture Y Location

    # xDistance = 194
    # yDistance = 40

    # newLong1, newLat1 = getNewGPSCord(gpsArr, 3, 0, yDistance, y)
    # newLong2, newLat2 = getNewGPSCord(gpsArr, 0, 1, xDistance, x)

    # print(newLong1, newLat1)
    # print(newLong2, newLat2)

    # newLong = 0
    # newLat = 0

    # # newLong = newLong1 - newLong2 
    # # newLat = newLat1 - newLat2

    # newLong = -newLong1 + newLong2 
    # newLat = newLat1 + newLat2

    # # If Top Right Was Middle Node
    # newLong = -newLong1 - newLong2 
    # newLat = -newLat1 + newLat2

    # print(str(gpsArr[0]['long'] + newLong) + ',' + str(gpsArr[0]['lat'] + newLat))

def findGPSCoordinates(gpsArr, gesturePos, listOfGestures):

    # stores the newly generated gps coordinates
    newGpsArr = []

    # gpsArr has 4 corner gps data
    # gesturePos has 4 corner gesture data
    # listOfGestures has just the gestures

    # gets the index of the top left, top right, and bottom left nodes
    topLeftIndex = topLeftNode(gesturePos)
    topRightIndex = topRightNode(gesturePos)
    bottomLeftIndex = bottomLeftNode(gesturePos)

    # calculates the ratio of meters to gesture coordinates (units are m/gesture)
    xLongRatio, xLatRatio, yLongRatio, yLatRatio = calcLongAndLatConversions(gpsArr, gesturePos, topLeftIndex, topRightIndex, bottomLeftIndex)

    # iterates through all gestures
    for gesture in listOfGestures:
        # calculates the difference in gesture positioning between the top left corner and the current gesture
        diffX = gesture['x'] - gesturePos[topLeftIndex]['x']
        diffY = gesture['y'] - gesturePos[topLeftIndex]['y']

        # takes the gps values of the top left corner and adds on the gesture difference times the ratio in both x and y
        newLong = gpsArr[topLeftIndex]['long'] + (diffX * xLongRatio) + (diffY * yLongRatio)
        newLat = gpsArr[topLeftIndex]['lat'] + (diffX * xLatRatio) + (diffY * yLatRatio)

        # adds gps coordinate to the newGPSArr list
        insertToList(newGpsArr, newLong, newLat)
    
    # prints out all gps coordinates
    for gps in newGpsArr:
        print(gps["long"], ",", gps["lat"])

    return newGpsArr

def topLeftNode(gesturePos):
    for i in range(len(gesturePos)):
        topLeft = gesturePos[i]
        left = 0
        top = 0
        for j in range(len(gesturePos)):
            if i == j:
                continue
            if topLeft['x'] < gesturePos[j]['x']:
                left += 1
            if topLeft['y'] < gesturePos[j]['y']:
                top += 1
        if left >= 2 and top >= 2:
            return i
    return -1

def bottomLeftNode(gesturePos):
    for i in range(len(gesturePos)):
        bottomLeft = gesturePos[i]
        left = 0
        bottom = 0
        for j in range(len(gesturePos)):
            if i == j:
                continue
            if bottomLeft['x'] < gesturePos[j]['x']:
                left += 1
            if bottomLeft['y'] > gesturePos[j]['y']:
                bottom += 1
        if left >= 2 and bottom >= 2:
            return i
    return -1

def topRightNode(gesturePos):
    for i in range(len(gesturePos)):
        topRight = gesturePos[i]
        right = 0
        top = 0
        for j in range(len(gesturePos)):
            if i == j:
                continue
            if topRight['x'] > gesturePos[j]['x']:
                right += 1
            if topRight['y'] < gesturePos[j]['y']:
                top += 1
        if right >= 2 and top >= 2:
            return i
    return -1


def calcLongAndLatConversions(gpsArr, gesturePos, topLeftIndex, topRightIndex, bottomLeftIndex):
    
    xGestureDiff = abs(gesturePos[topLeftIndex]['x'] - gesturePos[topRightIndex]['x'])
    yGestureDiff = abs(gesturePos[topLeftIndex]['y'] - gesturePos[bottomLeftIndex]['y'])

    xToLongValue = (gpsArr[topRightIndex]['long'] - gpsArr[topLeftIndex]['long'])
    xToLatValue = (gpsArr[topRightIndex]['lat'] - gpsArr[topLeftIndex]['lat'])

    yToLongValue = (gpsArr[bottomLeftIndex]['long'] - gpsArr[topLeftIndex]['long'])
    yToLatValue = (gpsArr[bottomLeftIndex]['lat'] - gpsArr[topLeftIndex]['lat'])

    xLongConversion = round(xToLongValue/xGestureDiff, 12)
    xLatConversion = round(xToLatValue/xGestureDiff, 12)
    yLongConversion = round(yToLongValue/yGestureDiff, 12)
    yLatConversion = round(yToLatValue/yGestureDiff, 12)

    return [xLongConversion, xLatConversion, yLongConversion, yLatConversion]
    


# Getting New Long And Lat For Gesture Position
def getNewGPSCord(gpsArr, firstIndex, secondIndex, dist, gestLoc):
    longDiff = gpsArr[firstIndex]['long'] - gpsArr[secondIndex]['long']
    latDiff = gpsArr[firstIndex]['lat'] - gpsArr[secondIndex]['lat']

    longRatio = longDiff / dist
    latRatio = latDiff / dist

    longValue = (gestLoc - 1) * longRatio
    latValue = (gestLoc - 1) * latRatio

    newLong = longValue
    newLat = latValue

    print(newLong, newLat)

    return abs(newLong), abs(newLat)

# Insert GPS Coord Into List
def insertToList(gpsArr, long, lat):
    gpsArr.append(
        {
            'long': long,
            'lat': lat
        }
    )

# Insert Gesture Postion Into List
def insertGesturePos(gesturePos, x, y):
    gesturePos.append(
        {
            'x': x,
            'y': y
        }
    )

if __name__ == "__main__":
    main()