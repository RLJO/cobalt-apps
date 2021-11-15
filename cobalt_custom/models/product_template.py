# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    _interval_selection = {'days': 'Days', 'months': 'Months', 'years': 'Years'}

    @api.depends('interval', 'days', 'months', 'years')
    def _compute_due_date(self):
        for alarm in self:
            if alarm.interval == "days":
                alarm.due_date = alarm.start_date + timedelta(days=alarm.days)
            elif alarm.interval == "months":
                alarm.due_date = alarm.start_date + relativedelta(months=alarm.months)
            elif alarm.interval == "years":
                alarm.due_date = alarm.start_date + relativedelta(years=alarm.years)

    start_date = fields.Datetime('Entry Date', default=lambda self: fields.Datetime.now())
    interval = fields.Selection(
        list(_interval_selection.items()), 'Timeset', default='days')
    days = fields.Integer(string='Days')
    months = fields.Integer(string='Months')
    years = fields.Integer(string='Years')
    due_date = fields.Datetime('Expiry Date', store=True, compute='_compute_due_date')