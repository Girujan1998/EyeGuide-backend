def main():
    print('Main function called.')

    conversionStyle = ["xToLong", "xToLat"]

    listOfGestures = []

    gpsArr = []

    insertToList(gpsArr, 43.474638, -80.545803)  # Top Left
    insertToList(gpsArr, 43.475416, -80.54362)   # Top Right
    insertToList(gpsArr, 43.475079, -80.543384)  # Bottom Right
    insertToList(gpsArr, 43.474301, -80.545574)  # Bottom Left

    gesturePos = []

    insertGesturePos(gesturePos, 1, 1)   # Top Left
    insertGesturePos(gesturePos, 13, 1)  # Top Right
    insertGesturePos(gesturePos, 13, 6)  # Bottom Right
    insertGesturePos(gesturePos, 1, 6)   # Bottom Left

    topLeftIndex = topLeftNode(gesturePos)
    topRightIndex = topRightNode(gesturePos)
    bottomLeftIndex = bottomLeftNode(gesturePos)


    conversion, xConvert, yConvert = calcLongAndLatConversions(gpsArr, gesturePos, topLeftIndex, topRightIndex, bottomLeftIndex)

    newGpsArr = []
    if conversion == conversionStyle[0]:
        # convert x gestures to longtitudes and y gestures to latitudes
        for gesture in listOfGestures:
            diffX = gesture.x - gesturePos[topLeftIndex].x
            diffY = gesture.y - gesturePos[topLeftIndex].y
            newGPSx = gpsArr[topLeftIndex]['long'] + diffX * xConvert
            newGPSy = gpsArr[topLeftIndex]['lat'] + diffY * yConvert
            insertToList(newGpsArr, newGPSx, newGPSy)
        
    else:
        # convert x gestures to latitudes and y gestures to longtitudes
        for gesture in listOfGestures:
            diffX = gesture.x - gesturePos[topLeftIndex].x
            diffY = gesture.y - gesturePos[topLeftIndex].y
            newGPSx = gpsArr[topLeftIndex]['lat'] + diffX * xConvert
            newGPSy = gpsArr[topLeftIndex]['long'] + diffY * yConvert
            insertToList(newGpsArr, newGPSy, newGPSx)



    x = 72  # Gesture X Location
    y = 33  # Gesture Y Location

    xDistance = 194
    yDistance = 40

    newLong1, newLat1 = getNewGPSCord(gpsArr, 3, 0, yDistance, y)
    newLong2, newLat2 = getNewGPSCord(gpsArr, 0, 1, xDistance, x)

    print(newLong1, newLat1)
    print(newLong2, newLat2)

    newLong = 0
    newLat = 0

    # newLong = newLong1 - newLong2 
    # newLat = newLat1 - newLat2

    newLong = -newLong1 + newLong2 
    newLat = newLat1 + newLat2

    # If Top Right Was Middle Node
    # newLong = -newLong1 - newLong2 
    # newLat = -newLat1 + newLat2

    print(str(gpsArr[0]['long'] + newLong) + ',' + str(gpsArr[0]['lat'] + newLat))

    # diff y (y1 - y2)
    # diff x
    # say diff y = 30m
    # say diff y (gesture) = 40 gesture units
    # 30m = 40 gesture units
    # y = 20 gesture units
    # 20 * 30m/40 gesture units = 15m

def topLeftNode(gesturePos):
    for i in range(len(gesturePos)):
        topLeft = gesturePos[i]
        left = 0
        top = 0
        for j in range(len(gesturePos)):
            if i == j:
                continue
            if topLeft.x < gesturePos[j].x:
                left += 1
            if topLeft.y > gesturePos[j].y:
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
            if bottomLeft.x < gesturePos[j].x:
                left += 1
            if bottomLeft.y < gesturePos[j].y:
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
            if topRight.x > gesturePos[j].x:
                right += 1
            if topRight.y > gesturePos[j].y:
                top += 1
        if right >= 2 and top >= 2:
            return i
    return -1


def calcLongAndLatConversions(gpsArr, gesturePos, topLeftIndex, topRightIndex, bottomLeftIndex):

    
    # maxLat, maxLong = 0
    
    # for i in range(len(gpsArr)):
    #     for j in range(i, len(gpsArr)):
    #         currLongDiff = abs(gpsArr[i]['long'] - gpsArr[i]['long'])
    #         if currLongDiff > maxLong:
    #             maxLong = currLongDiff
    #             maxLongPair = [i,j]
    #         currLatDiff = abs(gpsArr[i]['lat'] - gpsArr[i]['lat'])
    #         if currLatDiff > maxLat:
    #             maxLat = currLatDiff
    #             maxLatPair = [i,j]
    
    yGestureDiff = abs(gesturePos[topLeftIndex] - gesturePos[topRightIndex])
    xGestureDiff = abs(gesturePos[topLeftIndex] - gesturePos[bottomLeftIndex])

    xToLongValue = abs(gpsArr[topLeftIndex]['long'] - gpsArr[topRightIndex]['long'])
    xToLatValue = abs(gpsArr[topLeftIndex]['lat'] - gpsArr[topRightIndex]['lat'])


    if xToLongValue > xToLatValue:
        # convert x to longtitute, y to latitude
        xGestureToLongConversion = xGestureDiff/xToLongValue
        yGestureToLatConversion = yGestureDiff/(abs(gpsArr[topLeftIndex]['lat'] - gpsArr[bottomLeftIndex]['lat']))
        return ["xToLong", xGestureToLongConversion, yGestureToLatConversion]
    else:
        # convert y to longtitude, x to latitude
        xGestureToLatConversion = xGestureDiff/xToLatValue
        yGestureToLongConversion = yGestureDiff/(abs(gpsArr[topLeftIndex]['long'] - gpsArr[bottomLeftIndex]['long']))
        return ["xToLat", xGestureToLatConversion, yGestureToLongConversion]

    


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