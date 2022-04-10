from rest_framework.response import Response
from rest_framework.decorators import api_view
from awards.models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer, RateSerializer


@api_view(['GET'])
def getProfiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addRate(request):
    serializer = RateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)