from odoo import models, fields, api


class SalesKpi(models.Model):
    _name = 'sales.kpi'
    _description = 'Monthly Sales KPI'

    commercial_id = fields.Many2one(
        'sales.kpi.salesperson',
        string='Commercial',
        required=True
    )

    month = fields.Selection([
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ], string='Month', required=True)

    year = fields.Integer(
        string='Year',
        required=True
    )

    prospects_contacted = fields.Integer(
        string='Prospects Contacted',
        default=0
    )

    appointments = fields.Integer(
        string='Appointments Obtained',
        default=0
    )

    quotations = fields.Integer(
        string='Quotations Sent',
        default=0
    )

    sales = fields.Integer(
        string='Sales Completed',
        default=0
    )

    revenue = fields.Float(
        string='Revenue Generated',
        default=0.0
    )

    transformation_rate = fields.Float(
        string='Transformation Rate (%)',
        compute='_compute_kpis',
        store=True
    )

    prospect_to_appointment_rate = fields.Float(
        string='Prospect → Appointment (%)',
        compute='_compute_kpis',
        store=True
    )

    average_sale_value = fields.Float(
        string='Average Sale Value',
        compute='_compute_kpis',
        store=True
    )

    @api.depends(
        'prospects_contacted',
        'appointments',
        'sales',
        'revenue'
    )
    def _compute_kpis(self):
        for record in self:
            # Sales / Prospects × 100
            if record.prospects_contacted > 0:
                record.transformation_rate = (
                    record.sales / record.prospects_contacted
                ) * 100
            else:
                record.transformation_rate = 0.0

            # Appointments / Prospects × 100
            if record.prospects_contacted > 0:
                record.prospect_to_appointment_rate = (
                    record.appointments / record.prospects_contacted
                ) * 100
            else:
                record.prospect_to_appointment_rate = 0.0

            # Revenue / Sales
            if record.sales > 0:
                record.average_sale_value = (
                    record.revenue / record.sales
                )
            else:
                record.average_sale_value = 0.0