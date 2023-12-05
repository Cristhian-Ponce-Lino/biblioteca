from odoo import models, fields, api

from odoo.exceptions import ValidationError
from datetime import date, datetime


class LendBooks(models.Model):
    _name = 'biblioteca.lend.books'

    partner_id = fields.Many2one('res.partner', string='Nombres: ', required=True)
    borrowed = fields.One2many('biblioteca.book', 'lend_book_id', string='Títulos prestados')
    loan_day = fields.Date('Fecha de préstamo: ', default=date.today())
    return_day = fields.Date('Fecha de devolución: ', required=True)


    lend_book_wizard_id = fields.Many2one('biblioteca.report.wizard', string='wizard')
