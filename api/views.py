from rest_framework.views import APIView
from rest_framework.response import Response

from .models import StoreGPSData
from .models import StoreCornerCordsData
from .models import StoreNodeData

import sys
sys.path.append("..")
from scripts import coordinateMath
from scripts import aStarSearch
from scripts import determineTTS

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
            
            return Response({"buildingName": gpsCornerCordObjects.buildingName, "cornerCords": gpsCornerCordObjects.cornerCords}, status=200)
        except:
            return Response(status=404)

    def post(self, request, format=None):
        gpsCornerCordItem = request.data.get('gpsCornerCord')
        bad_gpsCornerCordItems = []

        existingItems = StoreCornerCordsData.objects.all().filter(buildingName=gpsCornerCordItem['buildingName'])
        if len(existingItems) == 0:
            try:
                new_gpsCornerCordItem = StoreCornerCordsData(buildingName=gpsCornerCordItem['buildingName'], cornerCords=gpsCornerCordItem['cornerCords'])
                new_gpsCornerCordItem.save()
            except:
                bad_gpsCornerCordItems.append(gpsCornerCordItem)
        else:
            gpsCornerCordObjects = existingItems[0]
            gpsCornerCordObjects.cornerCords = gpsCornerCordItem['cornerCords']
            gpsCornerCordObjects.save()

        if len(bad_gpsCornerCordItems) > 0:
            return Response({"INVALID GPS CORNER CORD DATA": bad_gpsCornerCordItems}, status=200)
        else:
            return Response(status=200)


class NodeView(APIView):
    def get(self, request, format=None):
        getType = request.query_params.get('getType')
        buildingName = request.query_params.get('buildingName')
        floorName = request.query_params.get('floorName')
        currentNodeName = request.query_params.get('startingNode')
        destinationNodeName = request.query_params.get('destination')
        
        try:
            if getType == 'get-route':
                print("get route type get")
                jsonNodes = StoreNodeData.objects.all().filter(buildingName=buildingName, floorName=floorName)
                
                destinationNodeGuidList = []
                currentNodeGuid = None
                for node in jsonNodes[0].nodes:
                    if node['name'] == currentNodeName:
                        currentNodeGuid = node['guid']
                    if node['name'] == destinationNodeName:
                        destinationNodeGuidList.append(node['guid'])
                
                print("right before search")
                minCost = 40075017
                minPath = None
                hash = aStarSearch.genHash(jsonNodes[0].nodes)
                for destNodeGuid in destinationNodeGuidList:
                    print("running a star search")
                    print(currentNodeGuid)
                    print(destNodeGuid)
                    print(hash)
                    print(jsonNodes[0].nodes)
                    path, cost = aStarSearch.aStar(jsonNodes[0].nodes, currentNodeGuid, destNodeGuid, hash)
                    print("a star just ran")
                    if cost < minCost:
                        minCost = cost
                        minPath = path
                print("nodes:", jsonNodes[0].nodes)
                print("min path found",minPath)
                tts = determineTTS.tts(hash, minPath)
                print("tts found",tts)
                return Response({"path": minPath, "tts": tts, "nodeList": jsonNodes[0].nodes}, status=200)

            elif getType == 'get-buildings':
                nodeObjects = StoreNodeData.objects.all()
                nodes = {}
                for node in nodeObjects:
                    if nodes.get(node.buildingName):
                        nodes[node.buildingName]['floorName'].append(node.floorName)
                    else:
                        nodes[node.buildingName] = {
                            'buildingName': node.buildingName,
                            'floorName': [node.floorName]
                            }
                print("got nodes from table", nodes)
                buildingList = []
                for buildingName in nodes:
                    buildingList.append(nodes[buildingName])
                print("found buildings: ", buildingList)
                result = {'nodes': buildingList}
                return Response(result, status=200)
            elif getType == 'get-building-data':
                nodeObjects = StoreNodeData.objects.all()
                nodes = {}
                print("all node objects from table",nodeObjects)
                for node in nodeObjects:
                    
                    # filter destination nodes here
                    filteredNodes = {destinationNode['name'] for destinationNode in node.nodes if destinationNode['type'] == 'DestinationNodeState'}
                    if nodes.get(node.buildingName):
                        nodes[node.buildingName]['floorNames'].append(node.floorName)
                        nodes[node.buildingName]['destinationNodes'].append(filteredNodes)
                    else:
                        nodes[node.buildingName] = {
                            'buildingName': node.buildingName,
                            'floorNames': [node.floorName],
                            'destinationNodes': [filteredNodes]
                            }
                print("after loop")
                buildingList = []
                
                # buildingList = [nodes[buildingName] for buildingName in node]
                for buildingName in nodes:
                    buildingList.append(nodes[buildingName])
                result = {'nodes': buildingList}
                print(result)
                return Response(result, status=200)
            
            return Response(status=404)
        except:
            return Response(status=404)

    def post(self, request, format=None):
        nodeItem = request.data['node']
        bad_nodeItems = []

        fourCornerItems = StoreCornerCordsData.objects.all().filter(buildingName=nodeItem['buildingName'])
        
        convertedList = coordinateMath.findGPSCoordinates(fourCornerItems, nodeItem['nodes'])
        print(convertedList)
        try:
            new_nodeItem = StoreNodeData(buildingName=nodeItem['buildingName'], floorName=nodeItem['floorName'], nodes=convertedList)
            new_nodeItem.save()
        except:
            bad_nodeItems.append(nodeItem)
        
        if len(bad_nodeItems) > 0:
            return Response({"INVALID NODE DATA": bad_nodeItems}, status=200)
        else:
            return Response(status=200)