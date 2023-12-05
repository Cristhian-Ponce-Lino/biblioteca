from odoo import models
from datetime import datetime


class biblioteca_report_xlsx(models.AbstractModel):
    _name = 'report.biblioteca.report_xlsx_ex'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, name):
        for obj in name:
            report_name = obj.name
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})

            format_header = workbook.add_format({'font_size': 10, 'align': 'center', 'right': True, 'left': True,
                                                 'bottom': True, 'top': True, 'bold': True, 'text_wrap': True,
                                                 'bg_color': '#BCBCBC'
                                                 })

            format_body_left = workbook.add_format({'font_size': 10, 'align': 'center',
                                                    'bold': False, 'text_wrap': True})

            # ancho de columnas
            COLUM_SIZES = [15, 15, 25, 25, 25]
            for position in range(len(COLUM_SIZES)):
                sheet.set_column(position, position, COLUM_SIZES[position])
            sheet.merge_range('A1:D1', "Reporte de préstamo de libros", format_header)

            sheet.autofilter('A2:A1000')
            sheet.write(1, 0, 'Usuario', format_header)
            sheet.write(1, 1, 'Nombre de Libro', format_header)
            sheet.write(1, 2, 'Fecha de préstamo', format_header)
            sheet.write(1, 3, 'Fecha de devolución', format_header)


            prueba = obj.lend_book_ids
            row = 2
            date_format = workbook.add_format({'num_format': 'dd-mm-yyyy'})
            sheet.set_column(7, 8, None, date_format)

            for v in prueba:
                # Obtener los datos de los campos de lend_book_ids
                partner_id = v.partner_id.name or ''
                return_day = v.return_day or ''
                loan_day = v.loan_day or ''

                # Escribir datos en las celdas correspondientes
                sheet.write(row, 0, partner_id, format_body_left)
                sheet.write(row, 2, datetime.combine(loan_day, datetime.min.time()), date_format)
                sheet.write(row, 3, datetime.combine(return_day, datetime.min.time()), date_format)

                # Tratar con los registros relacionados (campo borrowed)
                for account in v.borrowed:
                    sheet.write(row, 1, account.name or '', format_body_left)
                    row += 1

                # Agregar una fila en blanco entre registros lend_book_ids
                row += 1
