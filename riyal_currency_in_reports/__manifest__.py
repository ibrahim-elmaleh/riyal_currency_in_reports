
##############################################################################
{
    'name': 'Riyal currency in reports',
    'version': '16.0',
    'category': 'Accounting',
     'author': "Elmale7",
    'description': """
    -  Saudi Riyal Currency  .
    """,
    'license': 'AGPL-3',
    'depends': ['account'],
    'data': [],
    'assets': {
        'web.assets_backend': ['riyal_currency_in_reports/static/src/css/style.css'],
        'web.assets_frontend': ['riyal_currency_in_reports/static/src/css/style.css',


        ],
        'web.assets_common': ['riyal_currency_in_reports/static/src/css/style.css'],
        'web.report_assets_common': ['riyal_currency_in_reports/static/src/css/style.css'],
        'web.report_assets_pdf': ['riyal_currency_in_reports/static/src/css/style.css'],
        'web.assets_qweb': ['riyal_currency_in_reports/static/src/css/style.css'],
        "point_of_sale.assets": ['riyal_currency_in_reports/static/src/css/style.css'],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
