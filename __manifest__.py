# -*- coding: utf-8 -*-
{
    'name': "Biblioteca",
    'summary': """
        Préstamos de libros para las personas que son amante de la literatura
        """,
    'description': """
        Módulo de préstamo de libros
    """,

    'author': "Joel Ponce Lino",
    'company': 'Manexware S.A.',
    'website': "https://www.manexware.com",
    'contributors': [
        'Gean Vásconez <gean.vasconez@manexware.com>'
    ],
    'category': 'Préstamo',
    'version': '15.1.0',
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['report_xlsx'],
    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/author.xml',
        'views/book.xml',
        'views/lend_books.xml',
        'wizard/biblioteca_report_wizard.xml',
        'wizard/biblioteca_report_template.xml',
        'report/report_xlsx.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
}