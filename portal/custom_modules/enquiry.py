fields = []
tabs = []
table =[]

fields.append({
    'fieldName':'slno',
    'fieldCaption':'Sl.No',
    'fieldType':'string',
    'fieldDefault':1000,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
});

fields.append({
    'fieldName':'No',
    'fieldCaption':'Number',
    'fieldType':'string',
    'fieldDefault':1,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
})

fields.append({
    'fieldName':'Name',
    'fieldCaption':'Name',
    'fieldType':'string',
    'fieldDefault':1,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
})

fields.append({
    'fieldName':'age',
    'fieldCaption':'Age',
    'fieldType':'string',
    'fieldDefault':1,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
})

fields.append({
    'fieldName':'sex',
    'fieldCaption':'Sex',
    'fieldType':'radio',
    'fieldDefault':1,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
})

fields.append({
    'fieldName':'city',
    'fieldCaption':'City',
    'fieldType':'string',
    'fieldDefault':1,
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2'
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








    




