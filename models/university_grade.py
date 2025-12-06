from odoo import models, fields, api
from odoo.exceptions import ValidationError


class UniversityGrade(models.Model):
    _name = 'university.grade'
    _description = 'University Grade'
    _order = 'from_percentage desc, to_percentage desc'

    name = fields.Char(
        string="Grade Name",
        required=True,
        help="Grade code, e.g. O, A+, A, B, C, F"
    )
    from_percentage = fields.Float(
        string="From (%)",
        required=True,
        help="Lower limit of percentage for this grade (inclusive)."
    )
    to_percentage = fields.Float(
        string="To (%)",
        required=True,
        help="Upper limit of percentage for this grade (inclusive)."
    )
    grade_point = fields.Float(
        string="Grade Point",
        help="Numeric grade point, e.g. 10 for O, 9 for A+, etc."
    )
    remark = fields.Char(
        string="Remark",
        help="Short description like Outstanding, Excellent, Good, Pass, Fail."
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )

    _sql_constraints = [
        (
            'grade_name_unique',
            'unique(name)',
            'Grade name must be unique!'
        ),
    ]

    # --------------------------
    #   CONSTRAINTS / VALIDATION
    # --------------------------
    @api.constrains('from_percentage', 'to_percentage')
    def _check_percentage_range(self):
        for rec in self:
            # basic range 0–100
            if rec.from_percentage < 0 or rec.to_percentage < 0:
                raise ValidationError("Percentage cannot be negative.")
            if rec.from_percentage > 100 or rec.to_percentage > 100:
                raise ValidationError("Percentage cannot be greater than 100.")
            # from <= to
            if rec.from_percentage > rec.to_percentage:
                raise ValidationError(
                    "‘From (%)’ must be less than or equal to ‘To (%)’. "
                    "Please correct the range for grade %s." % (rec.name or '')
                )

    @api.constrains('from_percentage', 'to_percentage', 'active')
    def _check_overlapping_ranges(self):
        """
        Ensure that the percentage ranges of active grades
        do not overlap with each other.
        """
        for rec in self:
            if not rec.active:
                continue

            domain = [
                ('id', '!=', rec.id),
                ('active', '=', True),
                # Overlap condition:
                # NOT (other.to < this.from OR other.from > this.to)
                ('from_percentage', '<=', rec.to_percentage),
                ('to_percentage', '>=', rec.from_percentage),
            ]
            overlapping = self.search(domain, limit=1)
            if overlapping:
                raise ValidationError(
                    "Grade range %.2f–%.2f overlaps with grade '%s' (%.2f–%.2f). "
                    "Please adjust the ranges so they don't overlap." % (
                        rec.from_percentage,
                        rec.to_percentage,
                        overlapping.name,
                        overlapping.from_percentage,
                        overlapping.to_percentage,
                    )
                )

    # --------------------------
    #   HELPER LOGIC
    # --------------------------
    @api.model
    def get_grade_for_percentage(self, percentage):
        """
        Utility method:
        Given a percentage, return the matching grade record.

        Example usage from other models:
            grade = self.env['university.grade'].get_grade_for_percentage(83.5)
            if grade:
                result.grade_id = grade.id
        """
        if percentage is None:
            return False

        # Normalize if needed (you can adapt this)
        if percentage < 0 or percentage > 100:
            return False

        return self.search([
            ('active', '=', True),
            ('from_percentage', '<=', percentage),
            ('to_percentage', '>=', percentage),
        ], order='from_percentage desc', limit=1)
