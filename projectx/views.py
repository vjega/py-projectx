from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from projectx.models import Menus, Employee, Candidate, Assetmaster, Documents, Projects, Courses, Circulars, Reporting, Location, CompanySettings, User, Group
from projectx.serializers import MenuSerializer, EmployeeSerializer, CandidateSerializer, AssetsSerializer, DocumentsSerializer , ProjectsSerializer, CoursesSerializer, CircularsSerializer, ReportingSerializer, LocationSerializer, CompanySettingsSerializer, UserSerializer, GroupSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'POST'])
def menu_list(request):
    """
    List all Menus, or create a new snippet.
    """
    if request.method == 'GET':
        menu = Menus.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def employee_list(request):
    """
    List all Employee, or create a new snippet.
    """
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def employee_detail(request, emp_id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        employee = Employee.objects.get(emp_id=emp_id)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'POST'])
def candidate_list(request):
    """
    List all Candidate, or create a new snippet.
    """
    if request.method == 'GET':
        candidate = Candidate.objects.all()
        serializer = CandidateSerializer(candidate, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CandidateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def candidate_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        candidate = Candidate.objects.get(id=id) 
    except Candidate.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CandidateSerializer(candidate)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CandidateSerializer(candidate, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        candidate.delete()
        return HttpResponse(status=204)

# def candidate_selected(request, is_selected):
def candidate_selected(request):
    """
    List all Candidate, or create a new snippet.
    """
    if request.method == 'GET':
        candidate = Candidate.objects.filter(is_selected = 100)
        serializer = CandidateSerializer(candidate, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CandidateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def candidate_rejected(request, is_rejected):
    """
    List all Candidate, or create a new snippet.
    """
    if request.method == 'GET':
        candidate = Candidate.objects.filter(is_selected = 0)
        serializer = CandidateSerializer(candidate, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CandidateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def assets_list(request):
    """
    List all assets, or create a new snippet.
    """
    if request.method == 'GET':
        assetsmaster = Assetmaster.objects.all()
        serializer = AssetsSerializer(assetsmaster, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AssetsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def assets_detail(request, code): 
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        assetsmaster = Assetmaster.objects.get(code=code)
    except Assetmaster.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AssetsSerializer(assetsmaster)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AssetsSerializer(assetsmaster, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        assetsmaster.delete()
        return HttpResponse(status=204)

def assets_selected(request, assets_slno):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        assetsmaster = Assetmaster.objects.filter(assets_slno = assets_slno)
    except Assetmaster.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AssetsSerializer(assetsmaster)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AssetsSerializer(assetsmaster, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        assetsmaster.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
def documents_list(request):
    """
    List all documents, or create a new snippet.
    """
    if request.method == 'GET':
        documents = Documents.objects.all()
        serializer = DocumentsSerializer(documents, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DocumentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def projects_list(request):
    """
    List all projects, or create a new snippet.
    """
    if request.method == 'GET':
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def courses_list(request):
    """
    List all coursess, or create a new snippet.
    """
    if request.method == 'GET':
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CoursesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def circulars_list(request):
    """
    List all circulars, or create a new snippet.
    """
    if request.method == 'GET':
        circulars = Circulars.objects.all()
        serializer = CircularsSerializer(circulars, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CircularsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def circulars_detail(request, slno):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        circulars = Circulars.objects.get(slno=slno)
    except Circulars.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CircularsSerializer(circulars)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CircularsSerializer(circulars, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'POST'])
def reporting_list(request):
    """
    List all reportings, or create a new snippet.
    """
    if request.method == 'GET':
        reporting = Reporting.objects.all()
        serializer = ReportingSerializer(reporting, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReportingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def reporting_detail(request, project):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        reporting = Reporting.objects.get(project=project)
    except Reporting.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReportingSerializer(reporting)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReportingSerializer(reporting, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        reporting.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
def location_list(request):
    """
    List all location, or create a new snippet.
    """
    if request.method == 'GET':
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def location_detail(request, code):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        location = Location.objects.get(code=code)
    except Location.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LocationSerializer(location, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        location.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'POST'])
def companysettings_list(request):
    """
    List all companysettings, or create a new snippet.
    """
    if request.method == 'GET':
        companysettings = CompanySettings.objects.all()
        serializer = CompanySettingsSerializer(companysettings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompanySettingsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def companysettings_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        companysettings = CompanySettings.objects.get(id=id)
    except CompanySettings.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CompanySettingsSerializer(companysettings)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CompanySettingsSerializer(companysettings, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        location.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all user, or create a new snippet.
    """
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def user_detail(request, user_id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        location.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'POST'])
def group_list(request):
    """
    List all group, or create a new snippet.
    """
    if request.method == 'GET':
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def group_detail(request, group_id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        group = Group.objects.get(group_id=group_id)
    except Group.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GroupSerializer(group)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GroupSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        location.delete()
        return HttpResponse(status=204)










