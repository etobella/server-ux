# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib.openupgrade import logged_query, migrate
import json


@migrate()
def migrate(env, version):
    module_ids = env['ir.module.module'].search([
        ('name', '=', 'base_tier_validation_formula'),
        ('state', '=', 'uninstalled')
    ])
    module_ids.sudo().button_install()
    cr = env.cr
    cr.execute("UPDATE tier_definition SET definition_type = 'formula'")
