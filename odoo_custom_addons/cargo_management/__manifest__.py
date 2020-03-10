# -*- coding: utf-8 -*-
{
    'name': "Cargo Management",

    'summary': """
        Tracking Fleets.
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Inteligos",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Transporte',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'generic_request'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/main_menu_views.xml',
        'views/shifts_views.xml',
        'views/burden_types_views.xml',
        'views/configuration_of_box_car_views.xml',
        'views/packaging_types_views.xml',
        # 'views/incident_type_views.xml',
        'views/journeys_views.xml',
        'views/journeys_stop_views.xml',
        'views/burden_views.xml',
        'views/incidents.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
