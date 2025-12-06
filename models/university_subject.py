from odoo import fields, models


class UniversitySubject(models.Model):
    """For managing subjects of every courses"""
    _name = 'university.subject'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "University Subjects"

    name = fields.Char(string="Subject", help="Name of the subject")
    is_language = fields.Boolean(string="Language",
                                 help="Tick if this subject is a language")
    is_lab = fields.Boolean(string="Lab", help="Tick if this subject is a Lab")
    code = fields.Char(string="Code", help="Enter the Subject Code")
    type = fields.Selection(
        [('compulsory', 'Compulsory'), ('elective', 'Elective')],
        string='Type', default="compulsory",
        help="Choose the type of the subject")
    weightage = fields.Float(string='Weightage', default=1.0,
                             help="Enter the weightage for this subject")
    description = fields.Text(string='Description',
                              help="Description about the subject")
