from rest_framework.response import Response
from rest_framework.decorators import api_view
from awards.models import Profile, Project, Rate
from .serializers import ProfileSerializer, ProjectSerializer, RateSerializer

@api_view(['GET'])
def get_urls(request):
    api_urls = {
      'projects':'/projects',
      'profiles':'/profiles'
    }
    return Response(api_urls)

@api_view(['GET'])
def get_profiles(request, pk):
    profiles = Profile.objects.filter(id=pk)
    serializer = ProfileSerializer(profiles, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_rate(request):
    serializer = RateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_rates(request):
    rates = Rate.objects.all()
    serializer = RateSerializer(rates, many=True)
    return Response(serializer.data)