fields = []
tabs = []
table =[]

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