# -*- coding: utf-8 -*-
# Part of AktivSoftware See LICENSE file for full copyright and licensing details.
{
    'name': 'Quick Module Upgrade/Uninstall',
    'summary': 'Allow users to upgrade & uninstall apps from kanban',
    'description': """
    With use of this module user can quickly upgrade and uninstall the
    installed module/app directly from kanban view
    """,
    'author': 'Aktiv Software',
    'website': 'www.aktivsoftware.com',
    'category': 'Tools',
    'version': '10.0.1.0.0',
    'depends': ['base'],
    'data': [
        'views/templates.xml',
        'views/module_view.xml'
    ],
    'images': ['static/description/banner.jpg'],
    'auto_install': True,
    'installable': True,
    'application': False
}
