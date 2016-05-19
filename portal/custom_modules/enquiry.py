fields = []
tabs = []
table = []

fields.append({
    'fieldName':'slno',
    'fieldCaption':'Sl.No',
    'fieldType':'string',
    'fieldDefault':1000,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'true',
    'fieldHidden' : 'true'
});

fields.append({
    'fieldName':'No',
    'fieldCaption':'Number',
    'fieldType':'string',
    'fieldDefault':1,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'true',
    'fieldHidden' : 'false'
})

fields.append({
    'fieldName':'Name',
    'fieldCaption':'Name',
    'fieldType':'string',
    'fieldDefault':1,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
})

fields.append({
    'fieldName':'age',
    'fieldCaption':'Age',
    'fieldType':'string',
    'fieldDefault':1,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'true',
    'fieldHidden' : 'false'
})

fields.append({
    'fieldName':'sex',
    'fieldCaption':'Sex',
    'fieldType':'radio',   #'select', 
    'fieldDefault':1,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2' ,
    'fieldOptions': [        
        {'id': 'sex', 'name':'Male'}, 
        {'id': 'sex', 'name':'Female'},
        {'id': 'sex', 'name':'Transgender'}
        ],        
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'

})

fields.append({
    'fieldName':'city',
    'fieldCaption':'City',
    'fieldType':'textarea',
    'fieldDefault':1,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
})

tabs.append({
    'tabName':'general',
    'tabCaption':'General',
    'field':fields
})

fields = []

fields.append({
    'fieldName':'dob',
    'fieldCaption':'Date of Birth',
    'fieldType':'date',
    'fieldDefault':1,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'true',
    'fieldHidden' : 'false'
})

fields.append({
    'fieldName':'doj',
    'fieldCaption':'Date of joining',
    'fieldType':'select',
    'fieldDefault':None,
    'fieldConstrain':'pk',
    'fieldOptions': [
        {'id': 'doj', 'name':'Chennai'}, 
        {'id': 'doj', 'name':'Pune'},
        {'id': 'doj', 'name':'Us'}
        ],
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'true',
    'fieldHidden' : 'false'
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
