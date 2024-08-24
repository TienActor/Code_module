import json
from odoo import http
from odoo.http import request

class UserDropdownController(http.Controller):

    @http.route('/user_dropdown_data', type='http',website=True, auth='public', methods=['GET'], csrf=False)
    def get_users(self):
        # Truy vấn dữ liệu người dùng từ cơ sở dữ liệu
        users = request.env['res.partner'].sudo().search_read(
            [('is_company', '=', False), ('active', '=', True)],
            ['id', 'name']
        )
        # Trả về dữ liệu dưới dạng JSON
        return request.make_response(json.dumps(users), headers=[('Content-Type', 'application/json')])
