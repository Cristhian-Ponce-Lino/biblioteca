from odoo import models, fields, api


class Book(models.Model):
    _name = 'biblioteca.book'

    name = fields.Char('Nombre del libro: ', required=True)
    author = fields.Many2many('biblioteca.author', string='Autor: ', required=True)
    publisher = fields.Char('Editorial: ')
    publish_date = fields.Integer('Año de publicación: ')
    pages_count = fields.Integer('Número de páginas: ')
    state = fields.Selection([('available', 'Disponible'), ('borrowed', 'Prestado')], 'Estado: ', default='available')
    language = fields.Selection([('español', 'Español'), ('ingles', 'Ingles')], 'Idioma: ', default='español')
    description = fields.Text('Descripción: ')

    lend_book_id = fields.Many2one(
        comodel_name='biblioteca.lend.books',
        string='Prestado a: ')
