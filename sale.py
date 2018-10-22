# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Sale']


class Sale(metaclass=PoolMeta):
    __name__ = 'sale.sale'

    def _get_invoice_sale(self):
        invoice = super(Sale, self)._get_invoice_sale()

        if self.incoterm:
            invoice.incoterm = self.incoterm
            invoice.incoterm_place = self.incoterm_place
        return invoice
