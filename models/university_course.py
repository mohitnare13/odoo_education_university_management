from odoo import fields, models


class UniversityCourse(models.Model):
    """Used to managing the courses of university"""
    _name = 'university.course'
    _description = "University Courses"

    name = fields.Char(string="Name", required=True, help="Name of the course")
    category = fields.Selection(
        [('ug', 'Under Graduation'), ('pg', 'Post Graduation'),
         ('diploma', 'Diploma')], string="Course Category", required=True,
        help="In which category the course belong")
    no_semester = fields.Integer(string="No.of Semester",
                                 help="No.of semesters in each course")
