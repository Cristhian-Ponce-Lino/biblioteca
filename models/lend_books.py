from datetime import date

from odoo import models, fields


class LendBooks(models.Model):
    _name = 'biblioteca.lend.books'

    partner_id = fields.Many2one('res.partner', string='Usuario', required=True)
    borrowed = fields.One2many('biblioteca.book', 'lend_book_id', string='Nombre del libro')
    loan_day = fields.Date('Fecha de préstamo', default=date.today())
    return_day = fields.Date('Fecha de devolución', required=True)

    lend_book_wizard_id = fields.Many2one('biblioteca.report.wizard', string='wizard')
