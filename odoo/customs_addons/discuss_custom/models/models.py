from odoo import fields,models

class Student(models.Model):
    _name="school.student"
    _description="Lập trình module mới"

    user=fields.Many2one('res.partner',string='User',domain="[('is_company','=',False),('active', '=','True')]", )
    class_id=fields.Integer(string="Đã lưu")
    division=fields.Char("Lịch sử")
 