from odoo import fields, models


class AccountJournal(models.Model):
    """Inherited account.journal model for adding a field to
                        determine the journal is fee journal or not"""
    _inherit = 'account.journal'

    is_fee = fields.Boolean('Is University fee?', default=False,
                            help="Enable if the journal for university "
                                 "fee management")
