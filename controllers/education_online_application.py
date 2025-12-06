import base64
from odoo import http
from odoo.http import request


class OnlineAdmission(http.Controller):
    """Controller for taking online admission"""

    @http.route('/university', type='http', auth='public', website=True)
    def university_contact_us(self):
        """To redirect to contact page."""
        return request.render('education_university_management.university')

    @http.route('/applyonline', type='http', auth='public', website=True)
    def online_admission(self):
        """To pass certain default field values
                                    to the website registration form."""
        vals = {
            'department': request.env['university.department'].sudo().search(
                [('semester_ids', '!=', False)]),
            'course': request.env['university.course'].sudo().search([]),
            'semester': request.env['university.semester'].sudo().search([]),
            'batch': request.env['university.batch'].sudo().search([]),
            'year': request.env['university.academic.year'].sudo().search([]),
            'doc_type': request.env['university.document.type'].sudo().search([]),
            'countries': request.env['res.country'].sudo().search([]),
            'states': request.env['res.country.state'].sudo().search([]),
        }
        return request.render(
            'education_university_management.online_admission',vals)

    @http.route('/admission/submit', type='http', auth='public',
                website=True)
    def register_admission(self, **post):
        """ This will create a new student application with the values."""
        if post:
            guardian = request.env['res.partner'].sudo().create({
                'name': post.get('father'),
                'is_parent': True
            })
            application = request.env['university.application'].sudo().create({
                'name': post.get('first_name'),
                'last_name': post.get('last_name'),
                'mother_name': post.get('mother'),
                'father_name': post.get('father'),
                'mobile': post.get('phone'),
                'email': post.get('email'),
                'date_of_birth': post.get('date'),
                'academic_year_id': post.get('academic_year'),
                'mother_tongue': post.get('tongue'),
                'course_id': post.get('course'),
                'department_id': post.get('department'),
                'semester_id': post.get('semester'),
                'street': post.get('street'),
                'per_street': post.get('communication_address'),
                'street2': post.get('street2'),
                'city': post.get('city'),
                'zip': post.get('zip'),
                'state_id': int(post.get('state_id')) if post.get('state_id') else False,
                'country_id': int(post.get('country_id')) if post.get('country_id') else False,
                'nationality_id': int(post.get('country_id')) if post.get('country_id') else False,
                'father_occupation' : post.get('father_occupation'),
                'mother_occupation' : post.get('mother_occupation'),
                'religion' : post.get('religion'),
                'caste' : post.get('caste'),

                'guardian_id': guardian.id,
                'image': base64.b64encode((post.get('image')).read()),
                'prev_institute': post.get('prev_institute'),
                'prev_course': post.get('prev_course'),
                'prev_result': post.get('prev_result'),

            })
            if post.get('att'):
                doc_attachment = request.env['ir.attachment'].sudo().create({
                    'name': post.get('att').filename,
                    'res_name': 'Document',
                    'type': 'binary',
                    'datas': base64.encodebytes((post.get('att')).read()),
                })
                request.env['university.document'].sudo().create({
                    'document_type_id': post.get('doc_type'),
                    'attachment_ids': doc_attachment,
                    'application_ref_id': application.id
                })
        return request.render(
            "education_university_management.submit_admission",
            {})
