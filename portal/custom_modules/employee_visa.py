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
    'fieldName':'country',
	'fieldCaption': 'Country',
	'fieldType':'string',
	'fieldDefault':'',
	'fieldConstrain':'pk',
	'fieldClass': 'col-md-2',
	'fieldDisabled' : 'false',
	'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'start_date',
	'fieldCaption': 'Start date',
	'fieldType':'string',
	'fieldDefault':'',
	'fieldConstrain':'pk',
	'fieldClass': 'col-md-2',
	'fieldDisabled' : 'false',
	'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'end_date',
	'fieldCaption': 'End date',
	'fieldType':'string',
	'fieldDefault':'',
	'fieldConstrain':'pk',
	'fieldClass': 'col-md-2',
	'fieldDisabled' : 'false',
	'fieldHidden' : 'false'
});

fields.append({
    'fieldName':'remarks',
	'fieldCaption': 'Remarks',
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
	'name':'empVisa',
	'caption' : 'Employee Visa',
	'table' : 'employee',
	'tabs' : tabs,
	# 'actions': actions,
	'pk':'slno'
})