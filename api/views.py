from platform import platform
from django.shortcuts import render
from rest_framework.response import Response
from .models import Songs,platforma
from .serializers import SongsSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
# Create your views here.
from django.http import JsonResponse
class SongsAPI(APIView):
 def get(self, request, pk=None, format=None,song=None,artist=None):
  id = pk
  print(id)
  if id:
    s = platforma.objects.get(platformname=id)   
    stu = Songs.objects.filter(pk=s.pk)
    serializer = SongsSerializer(stu,many=True)
    print(type(serializer.data))
    a=[]
    d=[]
    p=[]
    saa=[]
    for i in serializer.data:
          a.append(i['artist_name'])
          d.append(i['duration'])
          s = Songs.objects.get(artist_name=i['artist_name'])
          sa = platforma.objects.get(pk=s.pk)   
          p.append(sa.platformname)
          saa.append(i['song_title'])
    return Response({"artist_name": a,"duration":d,"platform":p,"song_title":saa})
    print(stu)
  if song:
    stu = Songs.objects.filter(song_title=song)
    serializer = SongsSerializer(stu,many=True)
    print(type(serializer.data))
    a=[]
    d=[]
    p=[]
    saa=[]
    for i in serializer.data:
          a.append(i['artist_name'])
          d.append(i['duration'])
          s = Songs.objects.get(artist_name=i['artist_name'])
          sa = platforma.objects.get(pk=s.pk)   
          p.append(sa.platformname)
          saa.append(i['song_title'])
    return Response({"artist_name": a,"duration":d,"platform":p,"song_title":saa})
    
  if artist:
    stu = Songs.objects.filter(artist_name=artist)
    serializer = SongsSerializer(stu,many=True)
    a=[]
    d=[]
    p=[]
    saa=[]
    for i in serializer.data:
          a.append(i['artist_name'])
          d.append(i['duration'])
          s = Songs.objects.get(artist_name=i['artist_name'])
          sa = platforma.objects.get(pk=s.pk)   
          p.append(sa.platformname)
          saa.append(i['song_title'])
    return Response({"artist_name": a,"duration":d,"platform":p,"song_title":saa})    
    
        
  #stu = Songs.objects.all()
  stu = Songs.objects.all()
  s = []
  for i in stu:
      m = Songs( song_title=str(i.song_title))
      
  
  
  
#   for i in stu:
#       s.append(i)
  print(s)     
  
  serializer = SongsSerializer(stu,many=True)
  print(serializer.data)
  json_data = JSONRenderer().render(serializer.data)
  print(json_data)
  #return Response({"song_title": serializer.data})
  #return Response(json_data)
  l = []
  for i in serializer.data:
        print(i['song_title'])
        l.append(i['song_title'])
  data={
    "song_title":l
  }
      
  return JsonResponse(data,safe=False)
  return Response({"song_title": data})

 def post(self, request, format=None):
  serializer = SongsSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  # a=request.data
  # print(a)
  # return Response({'msg':'Complete Data Updated'})

 def put(self, request, pk, format=None):
  id = pk
  stu = Songs.objects.get(pk=id)
  serializer = SongsSerializer(stu, data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Complete Data Updated'})
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 def patch(self, request, pk, format=None):
  id = pk
  stu = Songs.objects.get(pk=id)
  serializer = SongsSerializer(stu, data=request.data, partial=True)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Partial Data Updated'})
  return Response(serializer.errors)

 def delete(self, request, pk, format=None):
  id = pk
  stu = Songs.objects.get(pk=id)
  stu.delete()
  return Response({'msg':'Data Deleted'})