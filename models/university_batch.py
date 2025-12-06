from odoo import api, fields, models


class UniversityBatch(models.Model):
    """For managing batches of every department in the university"""
    _name = 'university.batch'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "University Batches"

    @api.model
    def create(self, vals):
        """Return the name as a str of semester + academic year"""
        semester_id = self.env['university.semester'].browse(
            vals['semester_id'])
        academic_year_id = self.env['university.academic.year'].browse(
            vals['academic_year_id'])
        name = str(semester_id.name + ' - ' + academic_year_id.name)
        vals['name'] = name
        return super(UniversityBatch, self).create(vals)

    name = fields.Char(string="Name", help="Name of the Batch", readonly=True)
    semester_id = fields.Many2one('university.semester',
                                  string="Semester",
                                  help="Select the semester")
    department_id = fields.Many2one(related='semester_id.department_id',
                                    string="Department",
                                    help="In which department this "
                                         "batch belongs to")
    academic_year_id = fields.Many2one('university.academic.year',
                                       string="Academic Year", required=True,
                                       help="Select the academic year")
    batch_strength = fields.Integer(string='Batch Strength',
                                    help="Total strength of the batch")
    faculty_id = fields.Many2one('university.faculty',
                                 string='Faculty', help="Batch tutor/Faculty")
    batch_student_ids = fields.One2many('university.student',
                                        'batch_id',
                                        string="Students",
                                        help="Students of this Batch")
