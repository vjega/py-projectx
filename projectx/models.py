from __future__ import unicode_literals

from django.db import models

# Create your models here.

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Menus(models.Model):
	TREE_TYPES = (
		('folder','folder'),
		('card','card'),
		('list','list'),
		('report','report'),
    )
	code = models.AutoField(primary_key=True)
	priority = models.IntegerField()
	name = models.CharField(max_length=200, unique=True)
	caption = models.CharField(max_length=200)
	type = models.CharField(max_length=6, choices=TREE_TYPES)
	parent_code =models.IntegerField()
	module = models.CharField(max_length=100)
	access_level =models.IntegerField()
	active = models.IntegerField()

	class Meta:
		managed = True
		db_table = 'sys_menu'