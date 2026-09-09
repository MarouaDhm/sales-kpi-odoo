{
    'name': 'Sales KPI',
    'version': '1.0.0',
    'summary': 'Track monthly sales performance KPIs',
    'description': '''
        Sales KPI module for tracking commercial performance.
    ''',
    'category': 'Sales',
    'author': 'Maroua',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/salesperson_views.xml',
        'views/kpi_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}