
from django.test import TestCase
from .models import Project, Profile

# Create your tests here.

class ProjectTestClass(TestCase):

    def setUp(self):
        self.new_project = Project(title='test', description= 'test description', link= 'random link', image= 'random.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))

    def tearDown(self):
        Project.objects.filter(id=1).delete()

    def test_create_project(self):
        self.new_project.save()
        self.assertTrue(len(Project.objects.all())>0)


    
