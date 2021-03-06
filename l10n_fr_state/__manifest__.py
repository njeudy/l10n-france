# -*- coding: utf-8 -*-
# © 2013-2016 GRAP (Sylvain LE GAL https://twitter.com/legalsylvain)
# © 2015-2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': u'French States (Régions)',
    'summary': u'Populate Database with French States (Régions)',
    'version': '10.0.1.0.0',
    'category': 'French Localization',
    'author': "GRAP,Akretion,Odoo Community Association (OCA)",
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': ['base'],
    'pre_init_hook': 'create_fr_state_xmlid',
    'data': ['data/res_country_state_data.yml'],
    'images': ['static/src/img/screenshots/1.png'],
    'installable': True,
}
