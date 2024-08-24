# -*- coding: utf-8 -*-
{
    'name': 'Dropdown',
    'version': '4.0',
    'summary': 'This is a summary of my module',
    'sequence': 10,
    'description': 'Detailed description of my module',
    'category': 'Tools',
    'website': 'https://github.com/TienActor',
    'depends': ['base','account','hr','web','mail'],
     'assets': {
         'web.assets_backend': [
            'discuss_custom/static/src/js/external_libraries.js',
            'discuss_custom/static/src/xml/external_libraries.xml',
            # 'discuss_custom/static/src/xml/owl_connect.xml',
            # 'student/static/src/xml/dropdown_menu.xml',
        ],
    },
    'data': [
           "security/ir.model.access.csv",
           "views/menu_view.xml",
        #    "controller/controller_user.py",
        #  "views/dropdown.xml",
        #    "views/test.xml"
       #    "views/assets.xml",
    ],
    'demo': [],
   

    'installable': True,
    'application': True,
    'auto_install': False,
}