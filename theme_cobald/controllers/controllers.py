# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import requests, json, logging
from odoo import http, _
from odoo.http import request
from odoo.addons.website.controllers.main import Website
from odoo.exceptions import UserError


class Website(Website):

    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        return request.render('theme_cobald.home_template', {})


    @http.route('/about', type='http', auth="public", website=True)
    def about_page(self, **kw):
        return request.render('theme_cobald.about_template', {})

    @http.route('/about-details', type='http', auth="public", website=True)
    def about_details_page(self, **kw):
        return request.render('theme_cobald.about_details_template', {})

    @http.route('/merken', type='http', auth="public", website=True)
    def merken_page(self, **kw):
        return request.render('theme_cobald.merken_template', {})

    @http.route('/merken-details', type='http', auth="public", website=True)
    def merken_details_page(self, **kw):
        return request.render('theme_cobald.merken_details_template', {})

    @http.route('/merken-escale-details', type='http', auth="public", website=True)
    def merken_escale_details_page(self, **kw):
        return request.render('theme_cobald.merken_escale_details_template', {})

    @http.route('/merken-ply-details', type='http', auth="public", website=True)
    def merken_ply_details_page(self, **kw):
        return request.render('theme_cobald.merken_ply_details_template', {})

    @http.route('/dealers', type='http', auth="public", website=True)
    def dealers_page(self, **kw):
        return request.render('theme_cobald.dealers_template', {})

    @http.route('/contact', type='http', auth="public", website=True)
    def contact_page(self, **kw):
        return request.render('theme_cobald.contact_template', {})

    @http.route(["/contact-us-thank-you"], type='http', auth="public", website=True, csrf=False)
    def contact_us_thank_you_page(self, page=0, *args, **kwargs):
        if kwargs.get('name'):
            lead = request.env['crm.lead'].sudo().create({
                'name': kwargs.get('name'),
                'contact_name': kwargs.get('contact_name'),
                'phone': kwargs.get('phone'),
                'email_from': kwargs.get('email_from'),
                'description': kwargs.get('description'),
            })
            print("=============LEAD===========",lead)
        return request.redirect('/contactus-thank-you')

    @http.route('/cookie', type='http', auth="public", website=True)
    def cookie_page(self, **kw):
        return request.render('theme_cobald.cookie_template', {})

    @http.route('/cta', type='http', auth="public", website=True)
    def cta_page(self, **kw):
        return request.render('theme_cobald.cta_template', {})

