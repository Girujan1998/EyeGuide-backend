from rest_framework.views import APIView
from rest_framework.response import Response

from .models import StoreGPSData
from .models import StoreCornerCordsData

class GPSView(APIView):
    def get(self, request, format=None):
        gpsDict = {}

        try:
            gpsObjects = StoreGPSData.objects.all()
    
            for gpsItem in gpsObjects:
                gpsDict[gpsItem.name] = gpsItem.gpsCord

            return Response(gpsDict, status=200)
        except:
            return Response(status=404)

    def post(self, request, format=None):
        gpsItems = request.data['gps']
        bad_gpsItems = []

        for gpsItem in gpsItems:
            try:
                new_gpsItem = StoreGPSData(name=gpsItem['name'], gpsCord=gpsItem['gpsCord'])
                new_gpsItem.save()
            except:
                bad_gpsItems.append(gpsItem)
        
        if len(bad_gpsItems) > 0:
            return Response({"INVALID GPS DATA": bad_gpsItems}, status=200)
        else:
            return Response(status=200)

class CornerCordsView(APIView):
    def get(self, request, format=None):
        gpsCornerCordItems = request.query_params['buildingName']

        try:
            gpsCornerCordObjects = None
            try:
                gpsCornerCordObjects = StoreCornerCordsData.objects.get(buildingName=gpsCornerCordItems)
            except:
                return Response({}, status=200)

            return Response({"buildingName": gpsCornerCordObjects.buildingName, "cords": gpsCornerCordObjects.cornerCords}, status=200)
        except:
            return Response(status=404)

    def post(self, request, format=None):
        gpsCornerCordItems = request.data['gpsCornerCord']
        bad_gpsCornerCordItems = []
        print(gpsCornerCordItems)
        print(gpsCornerCordItems[0]['buildingName'])
        print(StoreCornerCordsData.objects.all())
        print(StoreCornerCordsData.objects.get(buildingName='1a'))

        try:
            gpsCornerCordObjects = StoreCornerCordsData.objects.get(buildingName=gpsCornerCordItems[0]['buildingName'])
            print("here" + gpsCornerCordObjects)
            gpsCornerCordObjects.cornerCords = gpsCornerCordItems[0]['cornerCords']
            print("here2" + gpsCornerCordObjects.cornerCords)
            gpsCornerCordObjects.save()
            print("here3")
        except:
            print("here4")
            for gpsCornerCordItem in gpsCornerCordItems:
                try:
                    new_gpsCornerCordItem = StoreCornerCordsData(buildingName=gpsCornerCordItem['buildingName'], cornerCords=gpsCornerCordItem['cornerCords'])
                    new_gpsCornerCordItem.save()
                except:
                    bad_gpsCornerCordItems.append(gpsCornerCordItem)

        if len(bad_gpsCornerCordItems) > 0:
            return Response({"INVALID GPS CORNER CORD DATA": bad_gpsCornerCordItems}, status=200)
        else:
            return Response(status=200)