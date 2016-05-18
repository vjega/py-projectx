from django.shortcuts import render
from projectx.models import Employee, Menus
from django.http import HttpResponse
from django.shortcuts import render
# from rest_1 import tab as rest_1_tab 
# from rest_2 import tab as rest_2_tab 

import json

def index(request):
    return render(request, 'custom.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

# def employee(request):
#     return render(request, 'employee.html')

def template_render(request, page_name):
    print "ttttt", page_name
    try:
        dao = __import__(
            'custom_modules.%s' % page_name, globals(), locals(), ['tabs'], -1)
        # print dao.tabs
        # print 'get_method DAO %s @ %s ' % (dao, datetime.now())
        # print "dhamu", dao
        # print "dhamu", page_name % (tab)
        print '>>>>>>>>>>>>>>>>>>>>'
        # print jsodao.tabs       
        print '<<<<<<<<<<<<<<<<<<<<'
        return HttpResponse(json.dumps(dao.table))
    except AttributeError as e:
        print('error')


# def get_method(self, str_format):
#         try:
#             dao = __import__(
#                 'dao.%s' % self.entity, globals(), locals(), [str_format % (self.entity)], -1)
#             # print 'get_method DAO %s @ %s ' % (dao, datetime.now())
#             return getattr(dao, str_format % (self.entity))
#         except AttributeError as e:
#             logging.exception(e)
#             raise FormDataException('could not find method %s for entity %s' % (
#                 str_format % (self.entity), self.entity))

