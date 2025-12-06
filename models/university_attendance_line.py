from odoo import fields, models


class UniversityAttendanceLine(models.Model):
    """For recording if the student is present during the day or not."""
    _name = 'university.attendance.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Attendance Lines'

    name = fields.Char(string='Name', help="Name of the attendance")
    attendance_id = fields.Many2one('university.attendance',
                                    string='Attendance Id',
                                    help="Relation field to attendance module")
    student_id = fields.Many2one('university.student',
                                 string='Student',
                                 help="Students of the batch")
    is_present_morning = fields.Boolean(string='Morning',
                                        help="Is student is present in the "
                                             "morning")
    is_present_afternoon = fields.Boolean(string='After Noon',
                                          help="Is student is present in "
                                               "the afternoon")
    full_day_absent = fields.Integer(string='Full Day',
                                     help="Is student full day absent or not ")
    half_day_absent = fields.Integer(string='Half Day',
                                     help="Is student half day absent or not ")
    batch_id = fields.Many2one('university.batch', string="Batch",
                               required=True,
                               help="Select batch for the attendance")
    date = fields.Date(string='Date', required=True, help="Attendance date")
