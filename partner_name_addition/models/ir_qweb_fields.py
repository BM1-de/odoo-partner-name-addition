# Copyright 2026 Baumgärtner Marketing GmbH
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, models


class IrQwebFieldContact(models.AbstractModel):
    _inherit = "ir.qweb.field.contact"

    @api.model
    def get_available_options(self):
        options = super().get_available_options()
        options["no_name_addition"] = {
            "type": "boolean",
            "string": self.env._("Without name addition"),
            "description": self.env._(
                "Do not print the name addition in the address, for layouts that "
                "print it on their own"
            ),
        }
        return options

    @api.model
    def value_to_html(self, value, options):
        if value and options.get("no_name_addition"):
            value = value.with_context(skip_name_addition=True)
        return super().value_to_html(value, options)
