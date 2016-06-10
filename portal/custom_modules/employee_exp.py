fields = []
tabs = []
table = []

fields.append({
    'fieldName':'slno',
	'fieldCaption': 'Sl No',
	'fieldType':'string',
	'fieldDefault':'',
	'fieldConstrain':'pk',
	'fieldClass': 'col-md-2',
	'fieldDisabled' : 'false',
	'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'emp_id',
	'fieldCaption': 'Employee Id',
	'fieldType':'string',
	'fieldDefault':'',
	'fieldConstrain':'pk',
	'fieldClass': 'col-md-2',
	'fieldDisabled' : 'false',
	'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'company_name',
	'fieldCaption': 'Company name',
	'fieldType':'string',
	'fieldDefault':'',
	'fieldConstrain':'pk',
	'fieldClass': 'col-md-2',
	'fieldDisabled' : 'false',
	'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'total_exp',
	'fieldCaption': 'Total exp',
	'fieldType':'string',
	'fieldDefault':'',
	'fieldConstrain':'pk',
	'fieldClass': 'col-md-2',
	'fieldDisabled' : 'false',
	'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'doj',
	'fieldCaption': 'Date of Join',
	'fieldType':'string',
	'fieldDefault':'',
	'fieldConstrain':'pk',
	'fieldClass': 'col-md-2',
	'fieldDisabled' : 'false',
	'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'dol',
	'fieldCaption': 'Date of Leaving',
	'fieldType':'string',
	'fieldDefault':'',
	'fieldConstrain':'pk',
	'fieldClass': 'col-md-2',
	'fieldDisabled' : 'false',
	'fieldHidden' : 'false'
});
fields.append({
    'fieldName':'designation',
	'fieldCaption': 'Designation',
	'fieldType':'string',
	'fieldDefault':'',
	'fieldConstrain':'pk',
	'fieldClass': 'col-md-2',
	'fieldDisabled' : 'false',
	'fieldHidden' : 'false'
});
fields.append({
    'fieldName':'ctc',
	'fieldCaption': 'CTC',
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
	'id' : 28,
	'name':'empExp',
	'caption' : 'Employee Experience',
	'table' : 'employee',
	'tabs' : tabs,
	# 'actions': actions,
	'pk':'slno'
})