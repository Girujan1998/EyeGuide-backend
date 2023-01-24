def main():
    print('Main function called.')

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