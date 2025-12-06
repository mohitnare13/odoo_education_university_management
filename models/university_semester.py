from odoo import api, fields, models


class UniversitySemester(models.Model):
    """Used to manage the semester of department"""
    _name = 'university.semester'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "University Semester"

    name = fields.Char(string="Name", help="Name of the semester",
                       compute="compute_semester_name")
    semester_no = fields.Integer(string="Semester", help="Semester number",
                                 required=True)
    department_id = fields.Many2one('university.department',
                                    string="Department",
                                    required=True,
                                    help="In which department the semester "
                                         "belongs to")
    syllabus_ids = fields.One2many('university.syllabus',
                                   'semester_id',
                                   help="Syllabus of semester",
                                   string="Syllabus")

    @api.depends('semester_no','department_id')
    def compute_semester_name(self):
        """ Updates the name field dynamically based on the
        department code and semester number."""
        for rec in self:
            if rec.department_id and rec.semester_no:
                rec.name = f"{rec.department_id.code}/Sem {rec.semester_no}"
            else:
                rec.name = False


