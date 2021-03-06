# © 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Sale Commercial Partner',
    'summary': "Add stored related field 'Commercial Entity' on sale orders",
    'version': '11.0.1.0.0',
    'author': 'Akretion,Odoo Community Association (OCA)',
    'website': 'http://www.akretion.com',
    'category': 'Sales',
    'license': 'AGPL-3',
    "contributors": [
        "Serpent Consulting Services Pvt. Ltd. <support@serpentcs.com>",
    ],
    'depends': [
        'sale'
    ],
    'data': [
        'views/sale.xml',
    ],
    'installable': True,
}
