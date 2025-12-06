from odoo import fields, models


class FeeStructureLines(models.Model):
    _name = 'fee.structure.line'
    _description = "Fee Structure lines"

    fee_structure_id = fields.Many2one('fee.structure',
                                       help="Relation to fee.structure",
                                       string='Fee Structure',
                                       ondelete='cascade', index=True)
    category_id = fields.Many2one(related='fee_structure_id.category_id',
                                  string="Category",
                                  help="Fee category of structure")
    fee_type_id = fields.Many2one('fee.type', string='Fee',
                                  required=True, help="Select fee types")
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  default=lambda
                                      self: self.env.user.company_id.currency_id.id,
                                  help="Currency of current company")
    fee_amount = fields.Float('Amount', required=True,
                              help="Amount of the each fee type",
                              related='fee_type_id.lst_price')
    payment_type = fields.Selection(string='Payment Type',
                                    help="Payment type of fee type",
                                    related="fee_type_id.payment_type")
    fee_description = fields.Text('Description', help="Fee type "
                                                      "description",
                                  related='fee_type_id.description_sale')
