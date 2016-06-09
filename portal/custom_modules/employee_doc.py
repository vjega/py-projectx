fields = []
tabs = []
table =[]

fields.append({
    'fieldName':'emp_id',
    'fieldCaption':'Employee Id',
    'fieldType':'string',
    'fieldDefault':'',
    'fieldConstrain':'pk',
    'fieldClass': 'col-md-2',
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'code',
    'fieldCaption':'Code',
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
    'fieldDisabled' : 'false',
    'fieldHidden' : 'false'
});

tabs.append({
    'tabName':'general',
    'tabCaption':'General',
    'field':fields
})

table.append({
    'id':27,
    'name':'Employee',
    'caption':'Employee',
    'table':'employee',
    'tabs':tabs,
    #'actions':actions,
    'pk':'slno'
})