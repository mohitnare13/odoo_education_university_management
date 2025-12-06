from odoo import models, fields, api


class UniversityMotherTongue(models.Model):
    _name = 'university.mother.tongue'
    _description = 'University Mother Tongue'

    name = fields.Char(required=True)


class UniversityDivision(models.Model):
    _name = 'university.division'
    _description = 'University Division'

    name = fields.Char(required=True)


class UniversityLanguage(models.Model):
    _name = 'university.language'
    _description = 'University Language'

    name = fields.Char(required=True)


class UniversityHobby(models.Model):
    _name = 'university.hobby'
    _description = 'University Hobby'

    name = fields.Char(required=True)
