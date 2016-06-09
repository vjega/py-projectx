from employee_doc import table as doc_table
fields = []
tabs = []
table =[]
actions =[]
tabs_set = []

fields.append({
    'fieldName':'center_code',
    'fieldCaption':'Center code',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'emp_id',
    'fieldCaption':'Emp id',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'true',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'id',
    'fieldCaption':'Org Emp Id',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'name',
    'fieldCaption':'Name',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'true',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'middle_name',
    'fieldCaption':'Middle Name',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'surname',
    'fieldCaption':'Surname',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'short_code',
    'fieldCaption':'Short code',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'qualification',
    'fieldCaption':'Qualification',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'blood_group',
    'fieldCaption':'Blood Group',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

tabs.append({
    'tabName':'general',
    'tabCaption':'General',
    'field':fields
})

fields = []

fields.append({
    'fieldName':'father_name',
    'fieldCaption':'Father Name',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});
fields.append({
    'fieldName':'mother_name',
    'fieldCaption':'Mother Name',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});
fields.append({
    'fieldName':'dob',
    'fieldCaption':'Date of Birth',
    'fieldType':'date',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'true',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'sex',
    'fieldCaption':'Father Name',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'marital_status',
    'fieldCaption':'Marital Status',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'year_of_passing',
    'fieldCaption':'Year of Passing',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

tabs.append({
    'tabName':'personal',
    'tabCaption':'Personal',
    'field':fields
})

fields = []

fields.append({
    'fieldName':'department',
    'fieldCaption':'Department',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'designation',
    'fieldCaption':'Designation',
    'fieldType':'textarea',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'client_name',
    'fieldCaption':'Client Name',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'client_name1',
    'fieldCaption':'Client Name 1',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'project_name',
    'fieldCaption':'Project Name',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'passport_no',
    'fieldCaption':'Passport No',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'passport_doi',
    'fieldCaption':'Passport Issue date',
    'fieldType':'date',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'passport_doe',
    'fieldCaption':'Passport Exp date',
    'fieldType':'date',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'true',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'doj',
    'fieldCaption':'Date of joining',
    'fieldType':'date',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

tabs.append({
    'tabName':'official',
    'tabCaption':'Official Details',
    'field':fields
})

tabs_set.insert(0, tabs) 

tabs = []
tabs.append({
    'id' : 'employee_doc',
    'name' : 'Document',
    'type' : 'list',
    'filename' : doc_table #'employee_doc'
})
tabs.append({
    'id' : 'employee_visa',
    'name' : 'Visa',
    'type' : 'list',
    'filename' : 'employee_visa'
})
tabs.append({
    'id' : 'emp_experience',
    'name' : 'Experience',
    'type' : 'list',
    'filename' : 'emp_experience'
})

print doc_table 

tabs_set.insert(1,tabs)

actions.append({
    'id' : 'set_password',
    'name' : 'Set Password',
    'class' : 'btn-primary',
    'params' : 'emp_id,emp_name',
    'action_method' : 'vm.save_password()'
})

actions.append({
    'id' : 'Almuni',
    'name' : 'Alumni',
    'class' : 'btn-primary',
    'params' : 'emp_id,emp_name',
    'action_method' : 'vm.change_alumni()'
})

actions.append({
    'id' : 'generate_appraisal',
    'name' : 'Generate Appraisal',
    'class' : 'btn-info',
    'params' : 'emp_id,emp_name',
    'action_method' : 'vm.generate_appraisal()'
})

actions.append({
    'id' : 'generate_payslip',
    'name' : 'Generate Payslip',
    'class' : 'btn-danger',
    'params' : 'emp_id,emp_name',
    'action_method' : 'vm.generate_payslip()'
})

table.append({
    'id':27,
    'name':'Employee',
    'caption':'Employee',
    'table':'employee',
    # 'tabs':tabs,
    'tabs':tabs_set,
    'actions':actions,
    'pk':'slno'
})
# print tabs_set[0]

