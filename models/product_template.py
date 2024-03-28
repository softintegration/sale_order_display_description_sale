# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    set_description_sale = fields.Boolean('Replace the description in the Sale order by the Description sale', default=False)
