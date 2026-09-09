from odoo import http
from odoo.http import request


class SalesKpiController(http.Controller):

    @http.route(
        '/api/sales-kpi',
        type='http',
        auth='none',
        methods=['GET'],
        csrf=False
    )
    def get_sales_kpis(self, **kwargs):
        kpis = request.env['sales.kpi'].sudo().search([])

        data = []

        for kpi in kpis:
            data.append({
                'id': kpi.id,
                'commercial': kpi.commercial_id.name,
                'month': kpi.month,
                'year': kpi.year,
                'prospects_contacted': kpi.prospects_contacted,
                'appointments': kpi.appointments,
                'quotations': kpi.quotations,
                'sales': kpi.sales,
                'revenue': kpi.revenue,
                'transformation_rate': kpi.transformation_rate,
                'prospect_to_appointment_rate':
                    kpi.prospect_to_appointment_rate,
                'average_sale_value': kpi.average_sale_value,
            })

        return request.make_json_response(data)

    @http.route(
        '/api/sales-kpi',
        type='http',
        auth='none',
        methods=['POST'],
        csrf=False
    )
    def create_sales_kpi(self, **kwargs):
        import json

        try:
            data = json.loads(
                request.httprequest.data.decode('utf-8')
            )

            kpi = request.env['sales.kpi'].sudo().create({
                'commercial_id': int(data['commercial_id']),
                'month': str(data['month']),
                'year': int(data['year']),
                'prospects_contacted': int(
                    data.get('prospects_contacted', 0)
                ),
                'appointments': int(
                    data.get('appointments', 0)
                ),
                'quotations': int(
                    data.get('quotations', 0)
                ),
                'sales': int(
                    data.get('sales', 0)
                ),
                'revenue': float(
                    data.get('revenue', 0.0)
                ),
            })

            return request.make_json_response({
                'success': True,
                'id': kpi.id,
                'message': 'KPI created successfully',
            })

        except Exception as e:
            return request.make_json_response({
                'success': False,
                'error': str(e),
            }, status=400)