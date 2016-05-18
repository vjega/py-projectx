fields = []
tabs = []
table =[]

fields.append({
    'fieldName':'center_code',
    'fieldCaption':'Center code',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
})

fields.append({
    'fieldName':'id',
    'fieldCaption':'Id',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
})

fields.append({
    'fieldName':'Name',
    'fieldCaption':'Name',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
})

fields.append({
    'fieldName':'middle_name',
    'fieldCaption':'Middle Name',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});

fields.append({
    'fieldName':'surname',
    'fieldCaption':'Surname',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});

fields.append({
    'fieldName':'short_code',
    'fieldCaption':'Short code',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});


fields.append({
    'fieldName':'marital_status',
    'fieldCaption':'Marital Status',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});

fields.append({
    'fieldName':'designation',
    'fieldCaption':'Designation',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});

fields.append({
    'fieldName':'sex',
    'fieldCaption':'Sex',
    'fieldType':'radio',
    'fieldDefault':1,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
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
    'fieldClass': 'col-md-2'
});

fields.append({
    'fieldName':'mother_name',
    'fieldCaption':'Mother Name',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});       

fields.append({
    'fieldName':'dob',
    'fieldCaption':'Date of Birth',
    'fieldType':'date',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});

fields.append({
    'fieldName':'qualification',
    'fieldCaption':'Qualification',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});

fields.append({
    'fieldName':'year_of_passing',
    'fieldCaption':'Year of Passing',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});



fields.append({
    'fieldName':'department',
    'fieldCaption':'Department',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});


fields.append({
    'fieldName':'client_name',
    'fieldCaption':'Client Name',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});

fields.append({
    'fieldName':'client_name1',
    'fieldCaption':'Client Name 1',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});

fields.append({
    'fieldName':'project_name',
    'fieldCaption':'Project Name',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});

fields.append({
    'fieldName':'passport_no',
    'fieldCaption':'Passport No',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});

fields.append({
    'fieldName':'passport_doi',
    'fieldCaption':'Passport Issue date',
    'fieldType':'date',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});

fields.append({
    'fieldName':'passport_doe',
    'fieldCaption':'Passport Exp date',
    'fieldType':'date',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});



fields.append({
    'fieldName':'city',
    'fieldCaption':'City',
    'fieldType':'string',
    'fieldDefault':1,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
})



fields.append({
    'fieldName':'dob',
    'fieldCaption':'Date of Birth',
    'fieldType':'date',
    'fieldDefault':1,
    'fieldConstrain':'pk'
})

fields.append({
    'fieldName':'doj',
    'fieldCaption':'Date of joining',
    'fieldType':'date',
    'fieldDefault':None,
    'fieldConstrain':'pk'
})

tabs.append({
    'tabName':'personal',
    'tabCaption':'Personal',
    'field':fields
})

table.append({
    'id':27,
    'name':'enquiry',
    'caption':'Enquiry',
    'table':'employee',
    'tabs':tabs,
    'actions':'',
    'pk':'slno'
})
