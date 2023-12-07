from odoo import models, fields


class Authors(models.Model):
    _name = 'biblioteca.author'
    _rec_name = 'name'

    name = fields.Char('Nombres: ', required=True)
    birthday = fields.Date('Fecha de nacimiento: ')
    nationality = fields.Char('Nacionalidad: ')
    sex = fields.Selection(
        [
            ('masculino', 'Masculino'),
            ('femenino', 'Femenino')
        ],
        'Género: ',
        default='masculino'
    )
