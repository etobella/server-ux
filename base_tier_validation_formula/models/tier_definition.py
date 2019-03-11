# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class TierDefinition(models.Model):
    _inherit = 'tier.definition'

    python_code = fields.Text(
        string='Tier Definition Expression',
        help="Write Python code that defines when this tier confirmation "
             "will be needed. The result of executing the expresion must be "
             "a boolean.",
        default="""# Available locals:\n#  - rec: current record""",
    )
    definition_type = fields.Selection(
        selection_add=[('formula', 'Formula')]
    )
