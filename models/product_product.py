# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class ProductProduct(models.Model):
    _inherit = "product.product"

    def get_product_multiline_description_sale(self):
        """ Inherit this to override the undesired behaviour
        """
        name = self.display_name
        if self.set_description_sale and self.description_sale:
            name = self.description_sale
        else:
            name = super(ProductProduct,self).get_product_multiline_description_sale()
        return name
