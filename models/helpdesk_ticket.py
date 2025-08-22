from odoo import models,fields,api

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    x_customer_name = fields.Char(string="User Name")
    x_customer_phone = fields.Char(string="Phone")
    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street 2")
    city = fields.Char(string="City")
    state_id = fields.Many2one('res.country.state', string="State")
    cost = fields.Char(string="Cost")
    technician_name = fields.Char(string="Technician name")
    country_id = fields.Many2one('res.country', string="Country")
    x_case_number = fields.Char(string="Case Number")
    x_issue_description = fields.Text(string="Problem")
    x_purchase_date = fields.Date(string="Purchase Date")
    x_case_date = fields.Date(string="Case Date")