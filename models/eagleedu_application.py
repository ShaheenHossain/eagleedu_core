# -*- coding: utf-8 -*-

from eagle import models, fields, api, _
from datetime import date

from datetime import datetime
from dateutil.relativedelta import relativedelta


class EagleeduApplication(models.Model):
    _name = 'eagleedu.application'
    _description = 'This is Student Application Form'
    # _order = 'id desc'
    _inherit = ['mail.thread']

    application_no = fields.Char(string='Application No.', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))

    application_date = fields.Datetime('Application Date', default=lambda self: fields.datetime.now())  # , default=fields.Datetime.now, required=True
    name = fields.Char(string='Student Name', required=True, help="Enter Name of Student")
    st_name_b = fields.Char(string='Student Bangla Name')
    st_image = fields.Binary(string='Image', help="Provide the image of the Student")
    st_father_name = fields.Char(string="Father's Name", help="Proud to say my father is", required=False)
    st_father_name_b = fields.Char(string="বাবার নাম", help="Proud to say my father is")
    st_father_occupation = fields.Char(string="Father's Occupation", help="father Occupation")
    st_father_email = fields.Char(string="Father's Email", help="father Occupation")
    father_mobile = fields.Char(string="Father's Mobile No", help="Father's Mobile No")
    st_mother_name = fields.Char(string="Mother's Name", help="Proud to say my mother is", required=False)
    st_mother_name_b = fields.Char(string="মা এর নাম", help="Proud to say my mother is")
    st_mother_occupation = fields.Char(string="Mother Occupation", help="Proud to say my mother is")
    st_mother_email = fields.Char(string="Mother Email", help="Proud to say my mother is")
    mother_mobile = fields.Char(string="Mother's Mobile No", help="mother's Mobile No")
    date_of_birth = fields.Date(string="Date Of birth", help="Enter your DOB")
    age = fields.Char(string="Age", compute="_compute_age")

    register_id = fields.Many2one('eagleedu.register', string="Admission Register", required=False,
                                      help="Enter the admission register Name")

    academic_year_id = fields.Many2one('eagleedu.academic.year', related='register_id.academic_year', string='Academic Year',
                                       help="Choose Academic year for which the admission is choosing")


    @api.multi
    @api.depends('date_of_birth')
    def _compute_age(self):
        for emp in self:
            age = relativedelta(datetime.now().date(), fields.Datetime.from_string(emp.date_of_birth)).years
            emp.age = str(age) + " Years"


    # age = fields.Char(string='Age', compute='_compute_age')
    #
    # @api.depends('date_of_birth')
    # def _compute_age(self):
    #     for rec in self:
    #         dt = rec.date_of_birth
    #         d2 = date.today()
    #         d1 = datetime.strptime(dt, "%Y-%m-%d").date()
    #         rd = relativedelta(d2, d1)
    #         rec.age = str(rd.years) + ' years ' + str(rd.months) + ' months ' + str(rd.days) + ' days'


    # age = fields.Integer(string="Age",  compute='_compute_student_age')

    # @api.depends('date_of_birth')
    # def _compute_student_age(self):
    #     '''Method to calculate student age'''
    #     current_dt = date.today()
    #     for rec in self:
    #         if rec.date_of_birth:
    #             start = rec.date_of_birth
    #             age_calc = ((current_dt - start).days / 365.24)
    #             # Age should be greater than 0
    #             if age_calc > 0.0:
    #                 rec.age = age_calc

    # @api.constrains('date_of_birth')
    # def check_age(self):
    #     '''Method to check age should be greater than 5'''
    #     current_dt = date.today()
    #     if self.date_of_birth:
    #         start = self.date_of_birth
    #         age_calc = ((current_dt - start).days / 365)
    #         # Check if age less than 5 years
    #         if age_calc < 5:
    #             raise ValidationError(_('''Age of student should be greater
    #              than 5 years!'''))


    st_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                                string='Gender', required=False, track_visibility='onchange',
                                help="Your Gender is ")
    st_blood_group = fields.Selection([('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('o+', 'O+'), ('o-', 'O-'),
                                    ('ab-', 'AB-'), ('ab+', 'AB+')],
                                   string='Blood Group', track_visibility='onchange',
                                   help="Your Blood Group is ")
    st_passport_no = fields.Char(string="Passport No.", help="Proud to say my father is", required=False)
    nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict',default=19,
                                help="Select the Nationality")
    academic_year = fields.Many2one('eagleedu.academic.year', string='Academic Year',
                                       help="Choose Academic year for which the admission is choosing")

    house_no = fields.Char(string='House No.', help="Enter the House No.")
    road_no = fields.Char(string='Area/Road No.', help="Enter the Area or Road No.")
    post_office = fields.Char(string='Post Office', help="Enter the Post Office Name")
    city = fields.Char(string='City', help="Enter the City name")
    bd_division_id = fields.Many2one('eagleedu.bddivision', string= 'State / Division')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',default=19,
                                 help="Select the Country")
    if_same_address = fields.Boolean(string="Permanent Address same as above", default=True,
                                     help="Tick the field if the Present and permanent address is same")
    per_village = fields.Char(string='Village Name', help="Enter the Village Name")
    per_po = fields.Char(string='Post Office Name', help="Enter the Post office Name ")
    per_ps = fields.Char(string='Police Station', help="Enter the Police Station Name")
    per_dist_id = fields.Many2one('eagleedu.bddistrict', string='District', help="Enter the City of District name")
    per_bd_division_id = fields.Many2one('eagleedu.bddivision', string='State / Division', help="Enter the City of District name")
    per_country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', default=19,
                                     help="Select the Country")
    guardian_name = fields.Char(string="Guardian's Name", help="Proud to say my guardian is")
    religious_id = fields.Many2one('eagleedu.religious', string="Religious", help="My Religion is ")

    #for import previous data
    class_id = fields.Many2one('eagleedu.class.division')
    academic_year = fields.Many2one('eagleedu.academic.year', string='Academic Year')
    group_division = fields.Many2one('eagleedu.group_division')
    student_id=fields.Char('Student Id')
    roll_no = fields.Integer('Roll No')
    section=fields.Char('Section')

    state = fields.Selection([('draft', 'Draft'), ('verification', 'Verify'),
                               ('approve', 'Approve'), ('done', 'Done')],
                              string='Status', required=True, default='draft', track_visibility='onchange')

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)
    email = fields.Char(string="Student Email", help="Enter E-mail id for contact purpose")
    phone = fields.Char(string="Student Phone", help="Enter Phone no. for contact purpose")
    mobile = fields.Char(string="Student Mobile", help="Enter Mobile num for contact purpose")
    nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict',default=19,
                                  help="Select the Nationality")

    guardian_relation = fields.Many2one('eagleedu.guardian.relation', string="Relation to Guardian",  required=False,
                                        help="Tell us the Relation toyour guardian")
    #### guardian Details
    guardian_name = fields.Char(string="Guardian's Name", help="Proud to say my guardian is",required=False)
    guardian_mobile = fields.Char(string="guardian's Mobile No", help="guardian's Mobile No")
    description = fields.Text(string="Note")

    @api.onchange('guardian_relation')
    def guardian_relation_changed(self):
        for rec in self:
            if rec.guardian_relation.name:
                if  rec.guardian_relation.name=='Father':
                    rec.guardian_mobile = rec.father_mobile
                    rec.guardian_name=rec.st_father_name
                elif  rec.guardian_relation.name=='Mother':
                    rec.guardian_mobile = rec.mother_mobile
                    rec.guardian_name = rec.st_mother_name




    @api.model
    def create(self, vals):
        """Overriding the create method and assigning the the sequence for the record"""
        if vals.get('application_no', _('New')) == _('New'):
            vals['application_no'] = self.env['ir.sequence'].next_by_code('eagleedu.application') or _('New')
        res = super(EagleeduApplication, self).create(vals)
        return res

    # def _compute_age(born):
    #     today = date.today()
    #     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


    # @api.depends('date_of_birth')
    # def _compute_age(self):
    #     for rec in self:
    #         dt = rec.date_of_birth
    #         d2 = date.today()
    #         d1 = datetime.strptime(dt, "%Y-%m-%d").date()
    #         rd = relativedelta(d2, d1)
    #         rec.age = str(rd.years) + ' years ' + str(rd.months) + ' months ' + str(rd.days) + ' days'

    @api.multi
    def send_to_verify(self):
        """Return the state to done if the documents are perfect"""
        for rec in self:
            rec.write({
                'state': 'verification'
            })


    @api.multi
    def application_verify(self):
        """Return the state to done if the documents are perfect"""
        for rec in self:
            rec.write({
                'state': 'approve'
            })



    @api.multi
    def create_student(self):
        """Create student from the application and data and return the student"""
        for rec in self:
            values = {
                'name': rec.name,
                'st_name_b': rec.st_name_b,
                'st_image': rec.st_image,
                # 'guardian_relation': rec.guardian_relation.id,
                # 'guardian_name': guardian,
                'application_no': rec.id,
                'st_father_name': rec.st_father_name,
                'st_father_name_b': rec.st_father_name_b,
                'father_mobile': rec.father_mobile,
                'st_father_occupation': rec.st_father_occupation,
                'st_mother_name': rec.st_mother_name,
                'st_mother_name_b': rec.st_mother_name_b,
                'mother_mobile': rec.mother_mobile,
                'st_mother_occupation': rec.st_mother_occupation,
                'st_gender': rec.st_gender,
                'date_of_birth': rec.date_of_birth,
                'st_blood_group': rec.st_blood_group,
                'st_passport_no': rec.st_passport_no,
                'nationality': rec.nationality.id,
                'academic_year': rec.academic_year.id,
                # 'standard_class': rec.standard_class.id,
                'admission_class': rec.register_id.standard.id,
                'group_division': rec.group_division.id,
                'house_no': rec.house_no,
                'road_no': rec.road_no,
                'post_office': rec.post_office,
                'city': rec.city,
                'bd_division_id': rec.bd_division_id.id,
                'country_id': rec.country_id.id,
                'per_village': rec.per_village,
                'per_po': rec.per_po,
                'per_ps': rec.per_ps,
                'per_dist_id': rec.per_dist_id.id,
                'per_bd_division_id': rec.per_bd_division_id.id,
                'per_country_id': rec.per_country_id.id,
                'guardian_name': rec.guardian_name,
                'religious_id': rec.religious_id.id,
                # 'is_student': True,
                'student_id': rec.student_id,
                'roll_no': rec.roll_no,
                'application_no': rec.application_no,
            }
            student = self.env['eagleedu.student'].create(values)
            rec.write({
                'state': 'done'
            })
            return {
                'name': _('Student'),
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'eagleedu.student',
                'type': 'ir.actions.act_window',
                'res_id': student.id,
                'context': self.env.context
            }



class EagleeduBddivision(models.Model):
    _name = 'eagleedu.bddivision'
    _description = 'This the Bangladesh Division'
    name = fields.Char()

class EagleeduBddistrict(models.Model):
    _name = 'eagleedu.bddistrict'
    _description = 'This the Bangladesh District'
    name = fields.Char()

class EagleeduReligious(models.Model):
    _name = 'eagleedu.religious'
    _description = 'This the Religion'
    name = fields.Char()

class EagleeduOrganization(models.Model):
    _description = 'This the Organization'
    _inherit = 'res.company'



