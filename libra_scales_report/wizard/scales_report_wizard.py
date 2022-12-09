# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
from datetime import date, datetime, timedelta


class SalemanDailyReport(models.TransientModel):
    _name = "scales.report"
    _description = "Daily Sale Report Wizard"

    start_date = fields.Date(string='Start Date', required=True, default=date.today())
    end_date = fields.Date(string='End Date', required=True, default=date.today())
    report_name = fields.Selection([('weighemnt_report', 'Weighemnt Report'),
                                     ('serial_wise_weight_report', 'Serial Wise Weight Report'),
                                     ('vehicle_wise_report', 'Vehicle Wise Report'),
                                     ('customers_weight_report', 'Customers Weight Report'),
                                     ('products_report', 'Products Report'),
                                     ('party_name', 'Party Name'),
                                     ('product_name', 'Product Name')], default='weighemnt_report')


    customer_name = fields.Many2many('res.partner', string='Customer Name')
    so_order = fields.Selection([('draft', 'Quotation'), ('done', 'Confirmed'), ('both', 'Both')], default="draft", string='State')
    user_id = fields.Many2one('res.users', string='User',  default=lambda self: self.env.user, required=True)
    company_id = fields.Many2one('res.company', string='Company',  default=lambda self: self.env.user.company_id,
                                 required=True)
    file = fields.Binary('Download Report')
    name = fields.Char()

    def generate_scales_report(self):

        data = self.read()
        if self.report_name == 'weighemnt_report':
            return self.env.ref('libra_scales_report.weighment_report_action').sudo().report_action(self, {'data': data})

        elif self.report_name == 'serial_wise_weight_report':
            return self.env.ref('libra_scales_report.serial_wise_weight_report_action').sudo().report_action(self, {'data': data})

        elif self.report_name == 'vehicle_wise_report':
            return self.env.ref('libra_scales_report.vehicle_wise_report_action').sudo().report_action(self, {'data': data})

        elif self.report_name == 'customers_weight_report':
            return self.env.ref('libra_scales_report.customer_weight_report_action').sudo().report_action(self, {'data': data})

        elif self.report_name == 'products_report':
            return self.env.ref('libra_scales_report.products_report_action').sudo().report_action(self, {'data': data})

        elif self.report_name == 'party_name':
            return self.env.ref('libra_scales_report.party_name_report_action').sudo().report_action(self, {'data': data})

        elif self.report_name == 'product_name':
            return self.env.ref('libra_scales_report.product_name_report_action').sudo().report_action(self, {'data': data})





