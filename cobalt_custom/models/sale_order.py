# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_vendor_id = fields.Many2one("res.partner",string="Vendor")
    sale_vendor_price = fields.Float("Vendor Price")



class ProductTemplate(models.Model):
    _inherit = 'product.template'

    sale_vendor_id = fields.Many2one("res.partner",string="Vendor")
    sale_vendor_price = fields.Float("Vendor Price")