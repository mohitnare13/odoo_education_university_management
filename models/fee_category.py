from odoo import fields, models


class FeeCategory(models.Model):
    """For managing the categories for university fees"""
    _name = 'fee.category'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Categories of university fees"

    name = fields.Char('Name', required=True,
                       help='Create a fee category suitable for institution.'
                            ' Like Institutional, Hostel, Transportation, '
                            'Arts and Sports, etc')
    journal_id = fields.Many2one('account.journal',
                                 domain="[('is_fee', '=', 'True')]",
                                 required=True, string='Journal',
                                 help='Setting up of unique journal '
                                      'for each category help to distinguish '
                                      'account entries of each category ')
