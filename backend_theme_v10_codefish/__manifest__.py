# -*- coding: utf-8 -*-
# Copyright 2016, 2017 Openworx
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "CodeFish Dark Theme",
    "summary": "Odoo 10.0 community backend theme",
    "version": "10.0.0.0.1",
    "category": "Themes/Backend",
    "website": "https://www.codefish.com.eg",
	"description": """
		Backend theme for Odoo 10.0 community edition.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "CodeFish",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
	'web_responsive',
    ],
    "data": [
        'views/assets.xml',
        'views/res_company_view.xml',
        'views/users.xml',
        'views/sidebar.xml',
    ],
}

