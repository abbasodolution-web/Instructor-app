from odoo import api, fields, models
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    name= fields.Char(string = 'Name', tracking=True)
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    gender = fields.Selection([('male', 'Male'),('female','Female')],string = 'Gender', tracking=True, default='male')
    code = fields.Char(string="Patient Code",readonly=True,copy=False,default="New")
    # code = fields.Char(string = 'Patient Code', readonly = True)
    date_of_birth = fields.Date(string = 'Date of Birth', tracking=True)   
    active = fields.Boolean(string = 'Active', default = True)
    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    ], string="Blood Group", default = 'a+')

    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    notes = fields.Text(string="Notes")


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0


    # @api.model_create_multi
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('code', 'New') == 'New':
                vals['code'] = self.env['ir.sequence'].next_by_code('hospital.patient') or 'New'

        return super().create(vals_list)
    
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         last = self.search([], order='id desc', limit=1)

    #         if last and last.code:
    #             number = int(last.code.replace('PT-', '')) + 1
    #         else:
    #             number = 1

    #         vals['code'] = f"PT-{number}"

    #     return super().create(vals_list)
