from odoo import fields, models


class TimetablePeriod(models.Model):
    """Manages the period details """
    _name = 'timetable.period'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Timetable Period'

    name = fields.Char(string="Name", required=True, help="Enter Period Name")
    time_from = fields.Float(string='From', required=True,
                             help="Start and End time of Period.")
    time_to = fields.Float(string='To', required=True,
                           help="Start and End time of Period.")
    company_id = fields.Many2one(
        'res.company', string='Company', help="Current company",
        default=lambda self: self.env.company)
