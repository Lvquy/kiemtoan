# -*- coding: utf-8 -*-

from odoo import fields, api, models


class Event(models.Model):
    _inherit = 'event.event'


    thoi_khoa_bieu = fields.One2many(comodel_name='details.tkb', inverse_name='ref_event', string='Thời khoá biểu')
    giang_vien = fields.Many2many(comodel_name='hr.employee', column2='department_id', column1='name', string='Giảng viên đứng lớp')

class DetailsTKB(models.Model):
    _name = 'details.tkb'
    _description = 'Chi tiết thời khoá biểu'

    date_tkb = fields.Date(string='Ngày')
    time_tkb = fields.Char(string='Thời gian')
    ref_event = fields.Many2one(comodel_name='event.event', string='Sự kiện', readonly=True)

class EventRegistration(models.Model):
    _inherit = 'event.registration'

    zalo_link = fields.Char(string='Link Zalo', compute='compute_zalo')
    is_dat = fields.Selection([('0','Chưa đạt chứng chỉ'),('1','Đã đạt chứng chỉ')],string='Đạt chứng chỉ', default='0', readonly=True)

    @api.onchange('phone')
    def compute_zalo(self):
        for rec in self:
            if rec.phone != False:
                rec.zalo_link = 'https://zalo.me/'+rec.phone
            else:
                rec.zalo_link = ''

    def confirm_dat(self):
        for rec in self:
            rec.is_dat = '1'

    def confirm_k_dat(self):
        for rec in self:
            rec.is_dat = '0'