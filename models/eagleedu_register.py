from eagle import fields, models, api, _
from eagle.exceptions import ValidationError
from datetime import datetime

class EagleeduRegister(models.Model):
    _name='eagleedu.register'
    _description='this admission register book'
    name=fields.Char('Register Book Name', compute='get_name')
    class_category=fields.Many2one('eagleedu.class.category',required=True, track_visibility='onchange')
    standard=fields.Many2one('eagleedu.class', required=True)
    # class_id=fields.Many2one('eagleedu.class', related='class_category.class_id')
    academic_year=fields.Many2one('eagleedu.academic.year', "For the year" , required=True)
    start_time = fields.Datetime(string='Application Starts on',default=lambda self: fields.datetime.now())
    end_time = fields.Datetime(string='Application ends on',default=lambda self: fields.datetime.now())
    active=fields.Boolean('Is active', default='True')

    # starting_day_of_current_year = datetime.now().date().replace(month=1, day=1)
    # ending_day_of_current_year = datetime.now().date().replace(month=12, day=31)


    @api.onchange('class_category', 'standard','academic_year')
    def get_name(self):
        for rec in self:
            if rec.class_category and rec.standard and rec.academic_year:
                rec.name=rec.class_category.name + rec.standard.name +'-'+rec.academic_year.name+' '+'Admission'



    #
    # partner_id = fields.Many2one('res.parner', string="Partner")
    #
    # phone = fields.Char(string="Identification", related='partner_id .phone')
    #

    # @api.onchange('class_category')
    # def set_class(self):
    #     for rec in self:
    #         self.standard==self.class_category

            #
            # if rec.class_category:
            #     rec.standard=rec.class_category.standard


    # @api.onchange('partner_id')
    # def on_change_field(self):
    #     self.phone = self.partner_id.phone

    # @api.onchange('class_category')
    # def set_class(self):
    #     for rec in self:
    #         if rec.class_category:
    #             rec.standard=rec.class_category.standard
    #
    # PACKAGE_TYPE_SELECTION = []
    #
    # class test(osv.osv):
    #     _name = "Test"
    #
    # _columns = {
    #     'selection': fields.selection(PACKAGE_TYPE_SELECTION, string='Selection'),
    # }

    # @api.onchange ('class_category', 'standard')
    # def get_name(self):
    #     for rec in self:
    #         if rec.class_category and rec.standard:
    #             rec.name =rec.class_category.name + '-' +rec.standard.name
    #
    #
    # @api.onchange('standard','academic_year')
    # def get_name(self):
    #     for rec in self:
    #         if rec.standard and rec.academic_year:
    #             rec.name=rec.standard.name +'-'+rec.academic_year.name+' '+'Admission'