from odoo import models, fields
from odoo.exceptions import UserError


class UniversityNotice(models.Model):
    _name = 'university.notice'
    _description = 'University Notice Board'

    subject = fields.Char(required=True)
    expiry_date = fields.Date()
    description = fields.Text()

    user_line_ids = fields.One2many(
        'university.notice.user.line',
        'notice_id',
        string="User Lines"
    )

    def send_by_email(self):
        mail_template = self.env.ref('education_university_management.notice_board_email_template', False)
        if not mail_template:
            raise UserError("Email Template Not Found. Please create the template.")

        if not self.user_line_ids:
            raise UserError("No users found to send email.")

        for line in self.user_line_ids:
            if not line.login:
                continue
            mail_template.email_to = line.login
            mail_template.send_mail(self.id, force_send=True)

        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Emails sent successfully!',
                'type': 'rainbow_man',
            }
        }


class UniversityNoticeUserLine(models.Model):
    _name = 'university.notice.user.line'
    _description = 'Notice User Details'

    notice_id = fields.Many2one('university.notice')
    user_id = fields.Many2one('res.users', string="Name")
    login = fields.Char(related="user_id.login", store=True)
    language = fields.Selection(related="user_id.lang", store=True)
    last_authentication = fields.Datetime(related="user_id.login_date", store=True)
    status = fields.Boolean(related="user_id.active", store=True)
