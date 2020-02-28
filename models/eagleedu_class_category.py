# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _

class EagleeduClassCategory(models.Model):
    _name='eagleedu.class.category'
    _description='Class Category list'
    name=fields.Char(string='Class Category')
    code=fields.Char(string='Category code')