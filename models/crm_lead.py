# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class Lead(models.Model):
    _inherit = "crm.lead"

    vat = fields.Char(
        string="TIN",
        help="Tax Identification Number. The first 2 characters are the "
             "country code.")
    x_campo1 = fields.Text(
        string="¿qué necesita la empresa?",
        help="describa que putas esta requeriendo la empresa",
    )

    x_campo2 = fields.Text(
        string="¿qué necesita el usuario?",
        help="describa que putas esta requeriendo el usuario",
    )

    x_campo3 = fields.Text(
        string="¿para que lo necesita?",
        help="",
    )

    x_campo4 = fields.Text(
        string="¿cómo lo necesita?",
        help="",
    )

    x_campo5 = fields.Text(
        string="¿requerimiento funcional?",
        help="",
    )