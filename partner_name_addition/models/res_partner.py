# Copyright 2026 Baumgärtner Marketing GmbH
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models

COMPANY_LINE = "%(company_name)s\n"


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

    def _prepare_display_address(self, without_company=False):
        address_format, args = super()._prepare_display_address(
            without_company=without_company
        )
        addition = self._get_name_addition()
        if not addition:
            return address_format, args
        args["name_addition"] = addition
        if address_format.startswith(COMPANY_LINE):
            # company line first, the name addition right below it
            address_format = (
                COMPANY_LINE
                + "%(name_addition)s\n"
                + address_format[len(COMPANY_LINE) :]
            )
        else:
            address_format = "%(name_addition)s\n" + address_format
        return address_format, args

    @api.depends_context("skip_name_addition")
    def _compute_display_name(self):
        # the address in the display name (context show_address) depends on it
        return super()._compute_display_name()

    def _display_address_depends(self):
        return super()._display_address_depends() + [
            "name_addition",
            "commercial_partner_id.name_addition",
        ]
