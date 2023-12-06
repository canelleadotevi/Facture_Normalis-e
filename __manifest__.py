# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Facture Normalisée',
    'version' : '1.0',
    'summary': 'Invoices & Payments',
    'sequence': 10,
    'description': """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Accounting && Finance',
    'website': '',
    'depends': ['base_setup'],
    'data': [
      
        'views/invoice_report.xml',
        'views/invoice_payment_view.xml',
        'views/invoice_invoice_views.xml',
        'views/invoice_group_views.xml',
        'views/invoice_journal_views.xml',
        'views/invoice_invoice_tag_views.xml',
        'views/invoice_bank_statement_views.xml',
        'views/invoice_reconcile_model_views.xml',
        'views/invoice_tax_views.xml',
        'views/invoice_full_reconcile_views.xml',
        'views/invoice_payment_term_views.xml',
        'views/invoice_payment_method.xml',
        'views/res_partner_bank_views.xml',
        'views/report_statement.xml',
        'views/terms_template.xml',
        'views/res_company_views.xml',
        'views/product_view.xml',
        'views/invoice_analytic_plan_views.xml',
        'views/invoice_analytic_account_views.xml',
        'views/invoice_analytic_distribution_model_views.xml',
        'views/invoice_analytic_line_views.xml',
        'views/report_invoice.xml',
        'report/account_invoice_report_view.xml',
        'views/invoice_cash_rounding_view.xml',
        'views/ir_module_views.xml',
        'views/res_config_settings_views.xml',
        'views/partner_view.xml',
        'views/invoice_journal_dashboard_view.xml',
        'views/invoice_portal_templates.xml',
        'views/report_payment_receipt_templates.xml',
        'views/invoice_incoterms_view.xml',
        'views/digest_views.xml',
        'report/invoice_hash_integrity_templates.xml',
        'views/res_currency.xml',
        'views/invoice_menuitem.xml',
        'views/bill_preview_template.xml',
        'views/uom_uom_views.xml',
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'auto-install':False,
    'icon':'static/src/img/BLOLAB.png',
    'post_init_hook': '',
    'assets': {
        'web._assets_primary_variables': [
            'invoice/static/src/scss/variables.scss',
        ],
        'web.assets_backend': [
            
        ],
        'web.assets_frontend': [
            'invoice/static/src/js/account_portal_sidebar.js',
            'invoice/static/src/js/account_portal.js',
        ],
        'web.assets_tests': [
            'invoice/static/tests/tours/**/*',
        ],
        'web.qunit_suite_tests': [
            'invoice/static/tests/helpers/*.js',
            'invoice/static/tests/*.js',
        ],
        'web.report_assets_common': [
            'invoice/static/src/css/report_invoice.css',
        ],
        'web.report_assets_pdf': [
            'invoice/static/src/css/report_invoice.css',
        ],
    },
    'license': 'LGPL-3',
}
