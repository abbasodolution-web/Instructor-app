from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    
    patient_id = fields.Many2one('hospital.patient', string = "Patient Name")
    gender = fields.Selection(related = 'patient_id.gender', readonly = True)
    appointment_time = fields.Datetime(string = "Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string = "Booking Date", default=fields.Date.context_today)
    code = fields.Char(string="Patient Code",readonly=True)
    age = fields.Integer(string="Age",readonly =True)
    text = fields.Text(string='Description')
    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    ], string="Blood Group")

    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    notes = fields.Text(string="Notes")
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], string="Priority", default='0')
    state = fields.Selection(
    [
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ]
        , default = 'draft', string = 'Status', required = True
    )

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.code = self.patient_id.code
        self.age = self.patient_id.age
        self.blood_group = self.patient_id.blood_group
        self.phone = self.patient_id.phone
        self.email = self.patient_id.email
        self.notes = self.patient_id.notes

    def action_test (self):
        print("Button Clicked")

    
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
    
    def action_confirm(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        self.state = 'done'
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Patient Completed Successfully!',
                'type': 'rainbow_man',
            }
        }
    
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'

    