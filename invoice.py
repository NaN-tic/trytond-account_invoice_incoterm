# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Bool, Eval

__all__ = ['Invoice']


class Invoice:
    __name__ = 'account.invoice'
    __metaclass__ = PoolMeta
    incoterm = fields.Many2One('incoterm', 'Incoterm',
        states={
            'readonly': Eval('state') != 'draft',
            },
        depends=['state'])
    incoterm_place = fields.Char('Incoterm Name Place',
        states={
            'required': Bool(Eval('incoterm')),
            'invisible': ~Bool(Eval('incoterm')),
            'readonly': Eval('state') != 'draft',
            },
        depends=['state', 'incoterm'])
