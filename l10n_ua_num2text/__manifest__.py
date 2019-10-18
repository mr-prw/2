# -*- coding: utf-8 -*-
# Copyright 2018 Yurii Razumovskyi <https://garazd.biz>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    'name' : 'Numbers to Ukrainian text',
    'version': '12.0.1.0.1',
    'category': 'Tools',
    'author': 'Garazd Creation',
    'website' : 'https://garazd.biz',
    'license': 'LGPL-3',
    'summary': 'Convert numbers to Ukrainian text',
    'description': """
This module allows converting numbers into Ukrainian text (Сума прописом/Сумма прописью).

USING:
======

    import decimal

    from odoo.addons.l10n_ua_num2text import num2t4ua

    ...

    # return string

    num2t4ua.num2text(int(value)))

    ...

    # return string with the currency (грн, коп)

    num2t4ua.decimal2text(decimal.Decimal(value)))


Технічна підтримка та розробка
==============================

Контакти для зв'язку з нами:

* support@garazd.biz
* `https://garazd.biz/page/contactus`_
.. _https://garazd.biz/page/contactus: https://garazd.biz/page/contactus

Пакети технічної підтримки: https://garazd.biz/page/odoo-support
    """,
    'images': ['static/description/banner.png'],
    'depends' : [],
    'data': [],
    'application': False,
    'installable': True,
    'auto_install': False,
}
