from odoo import models, fields


class SalesKpiSalesperson(models.Model):
    _name = 'sales.kpi.salesperson'
    _description = 'Salesperson'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')