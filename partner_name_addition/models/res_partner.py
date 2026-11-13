# Copyright 2026 Baumgärtner Marketing GmbH
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models

#: first line of the address of a contact: the name of its company
PARENT_LINE = "%(parent_name)s\n"


class ResPartner(models.Model):
    _inherit = "res.partner"

    name_addition = fields.Char(
        help="Second name line printed in the address, below the name: for example "
        "a trade name, a department or the name of a practice. Contacts of a "
        "company without an own name addition use the one of the company.",
    )

    def _get_name_addition(self):
        """Name addition used in the address of this partner.

        Its own value first; contacts and addresses of a company fall back to the
        name addition of the company (the commercial partner).
        """
        self.ensure_one()
        if self.env.context.get("skip_name_addition"):
            return ""
        return (
            self.name_addition or self.commercial_partner_id.name_addition or ""
        ).strip()

    def _prepare_display_address(self, without_name=False):
        address_format, args = super()._prepare_display_address(
            without_name=without_name
        )
        # Odoo also formats the address of no partner at all, for example the map
        # of a project without customer
        addition = self._get_name_addition() if self else ""
        if not addition:
            return address_format, args
        args["name_addition"] = addition
        if address_format.startswith(PARENT_LINE):
            # the name of the company first, the name addition right below it
            address_format = (
                PARENT_LINE + "%(name_addition)s\n" + address_format[len(PARENT_LINE) :]
            )
        else:
            address_format = "%(name_addition)s\n" + address_format
        return address_format, args

    @api.depends_context("skip_name_addition")
    def _compute_address(self):
        # the address fields are cached, with and without the name addition
        return super()._compute_address()

    @api.depends_context("skip_name_addition")
    def _compute_display_name(self):
        # the address in the display name (context show_address) depends on it
        return super()._compute_display_name()

    def _display_address_depends(self):
        return super()._display_address_depends() + [
            "name_addition",
            "commercial_partner_id.name_addition",
        ]
