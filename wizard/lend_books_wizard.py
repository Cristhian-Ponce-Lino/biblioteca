from odoo import models, fields, api


class ReportWizard(models.Model):
    _name = 'biblioteca.report.wizard'

    name = fields.Char(string="Reporte", default="report")

    lend_book_id = fields.Many2one('biblioteca.lend.books', string='Usuario: ')
    loan_day = fields.Date('Fecha Inicial: ', required=True)
    return_day = fields.Date('Fecha de Entrega: ', required=True)

    lend_book_ids = fields.One2many(
        'biblioteca.lend.books',
        'lend_book_wizard_id',
        string='Nombre de libro'
    )

    def action_report_pdf(self):
        return self.env.ref('biblioteca.report_pdf_wizard').report_action(self)

    @api.onchange('loan_day', 'return_day')
    def search_action_filter(self):
        filter = self.env['biblioteca.lend.books'].search(
            [('loan_day', '>=', self.loan_day), ('loan_day', '<=', self.return_day)])
        if filter:
            self.lend_book_ids = [(6, 0, filter.ids)]

    def action_report_excel(self):
        report_action = self.env.ref('biblioteca.report_xlsx_book').report_action(self)
        report_action['close_on_report_download'] = True
        return report_action





