# -*- coding: utf-8 -*-




from odoo import models, api,fields


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    transaction_type = fields.Many2one('account.bank.statement.transaction.type',string='Transaction Type',)


class AccountBankStatementTransactionType(models.Model):
    _name = 'account.bank.statement.transaction.type'
    _description = 'Transaction type'

    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')


