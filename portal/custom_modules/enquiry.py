fields = []
tabs = []

fields.append({
    'fieldName':'slno',
    'fieldCaption':'Sl.No',
    'fieldType':'integer',
    'fieldDefault':1000,
    'fieldConstrain':'pk'
});

fields.append({
    'fieldName':'No',
    'fieldCaption':'Number',
    'fieldType':'integer',
    'fieldDefault':1,
    'fieldConstrain':'pk'
})

fields.append({
    'fieldName':'Name',
    'fieldCaption':'Name',
    'fieldType':'string',
    'fieldDefault':1,
    'fieldConstrain':'pk'
})

fields.append({
    'fieldName':'age',
    'fieldCaption':'Age',
    'fieldType':'string',
    'fieldDefault':1,
    'fieldConstrain':'pk'
})

fields.append({
    'fieldName':'sex',
    'fieldCaption':'Sex',
    'fieldType':'radio',
    'fieldDefault':1,
    'fieldConstrain':'pk'
})

fields.append({
    'fieldName':'city',
    'fieldCaption':'City',
    'fieldType':'string',
    'fieldDefault':1,
    'fieldConstrain':'pk'
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
    'fieldType':'integer',
    'fieldDefault':1,
    'fieldConstrain':'pk'
})

fields.append({
    'fieldName':'doj',
    'fieldCaption':'Date of joining',
    'fieldType':'integer',
    'fieldDefault':None,
    'fieldConstrain':'pk'
})

tabs.append({
    'tabName':'personal',
    'tabCaption':'Personal',
    'field':fields
})








    




