
from odoo import models, fields, api


class SerialWiseWeightReport(models.AbstractModel):
    _name = 'report.libra_scales_report.serial_wise_weight_report_template'
    _description = 'Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        records = self.env['scales.report'].browse(data.get('data')[0]['id'])
        rec = self.env['sale.order'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'scales.report',
            'docs': records,
        }