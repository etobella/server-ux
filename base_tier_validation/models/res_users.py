# Copyright 2019 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, exceptions, fields, models, modules


class Users(models.Model):
    _inherit = 'res.users'

    review_ids = fields.Many2many(
        string="Reviews", comodel_name="tier.review"
    )
    
    @api.model
    def review_user_count(self):        
        user_reviews = {}
        for review in self.env.user.review_ids.filtered(
                lambda r: r.status == 'pending'):
            model = review.env[review.model].browse(review.res_id)
            if not user_reviews.get(review['model']):
                user_reviews[review.model] = {
                    'name': model._description,
                    'model': review.model,
                    'icon': modules.module.get_module_icon(
                        self.env[review.model]._original_module),
                    'pending_count': 0
                }
            user_reviews[review.model]['pending_count'] += 1
        return list(user_reviews.values())
