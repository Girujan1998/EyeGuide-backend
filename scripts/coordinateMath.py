def findGPSCoordinates(fourCornerArray, listOfGestures):

    gpsArr = fourCornerArray[0].cornerCords

    # gets the index of the top left, top right, and bottom left nodes
    topLeftIndex = topLeftNode(gpsArr)
    topRightIndex = topRightNode(gpsArr)
    bottomLeftIndex = bottomLeftNode(gpsArr)

    # calculates the ratio of meters to gesture coordinates (units are m/gesture)
    xLongRatio, xLatRatio, yLongRatio, yLatRatio = calcLongAndLatConversions(gpsArr, topLeftIndex, topRightIndex, bottomLeftIndex)

    # iterates through all gestures
    for gesture in listOfGestures:
        # calculates the difference in gesture positioning between the top left corner and the current gesture
        diffX = gesture['x'] - gpsArr[topLeftIndex]['x']
        diffY = gesture['y'] - gpsArr[topLeftIndex]['y']

        # takes the gps values of the top left corner and adds on the gesture difference times the ratio in both x and y
        newLong = gpsArr[topLeftIndex]['long'] + (diffX * xLongRatio) + (diffY * yLongRatio)
        newLat = gpsArr[topLeftIndex]['lat'] + (diffX * xLatRatio) + (diffY * yLatRatio)

        # adds gps coordinate to the newGPSArr list
        gesture['lat'] = newLat
        gesture['long'] = newLong

    return listOfGestures
    

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


def calcLongAndLatConversions(gpsArr, topLeftIndex, topRightIndex, bottomLeftIndex):
    
    xGestureDiff = abs(gpsArr[topLeftIndex]['x'] - gpsArr[topRightIndex]['x'])
    yGestureDiff = abs(gpsArr[topLeftIndex]['y'] - gpsArr[bottomLeftIndex]['y'])

    xToLongValue = (gpsArr[topRightIndex]['long'] - gpsArr[topLeftIndex]['long'])
    xToLatValue = (gpsArr[topRightIndex]['lat'] - gpsArr[topLeftIndex]['lat'])

    yToLongValue = (gpsArr[bottomLeftIndex]['long'] - gpsArr[topLeftIndex]['long'])
    yToLatValue = (gpsArr[bottomLeftIndex]['lat'] - gpsArr[topLeftIndex]['lat'])

    xLongConversion = round(xToLongValue/xGestureDiff, 12)
    xLatConversion = round(xToLatValue/xGestureDiff, 12)
    yLongConversion = round(yToLongValue/yGestureDiff, 12)
    yLatConversion = round(yToLatValue/yGestureDiff, 12)

    return [xLongConversion, xLatConversion, yLongConversion, yLatConversion]
    
