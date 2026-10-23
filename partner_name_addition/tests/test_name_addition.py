# Copyright 2026 Baumgärtner Marketing GmbH
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestNameAddition(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        country = cls.env.ref("base.de")
        cls.company = cls.env["res.partner"].create(
            {
                "name": "Anna Beispiel",
                "is_company": True,
                "name_addition": "Praxis am Markt - Physiotherapie",
                "street": "Musterweg 1",
                "zip": "12345",
                "city": "Musterstadt",
                "country_id": country.id,
            }
        )
        cls.person = cls.env["res.partner"].create(
            {"name": "Anna Beispiel", "parent_id": cls.company.id, "type": "contact"}
        )
        cls.plain = cls.env["res.partner"].create(
            {
                "name": "Muster GmbH",
                "is_company": True,
                "street": "Hauptstraße 2",
                "zip": "54321",
                "city": "Beispielstadt",
                "country_id": country.id,
            }
        )

    def _lines(self, partner, **kwargs):
        return partner._display_address(**kwargs).split("\n")

    def test_company_line_then_addition(self):
        lines = self._lines(self.company)
        self.assertEqual(lines[0], "Anna Beispiel")
        self.assertEqual(lines[1], "Praxis am Markt - Physiotherapie")
        self.assertEqual(lines[2], "Musterweg 1")

    def test_child_contact_uses_company_addition(self):
        lines = self._lines(self.person)
        self.assertEqual(lines[0], "Anna Beispiel")
        self.assertEqual(lines[1], "Praxis am Markt - Physiotherapie")
        self.assertEqual(lines[2], "Musterweg 1")

    def test_without_company(self):
        lines = self._lines(self.person, without_company=True)
        self.assertEqual(lines[0], "Praxis am Markt - Physiotherapie")
        self.assertEqual(lines[1], "Musterweg 1")

    def test_own_addition_wins(self):
        self.person.name_addition = "Abteilung Training"
        lines = self._lines(self.person, without_company=True)
        self.assertEqual(lines[0], "Abteilung Training")

    def test_no_addition_unchanged(self):
        self.assertEqual(
            self.plain._display_address(),
            self.plain.with_context(skip_name_addition=True)._display_address(),
        )
        self.assertEqual(self._lines(self.plain)[1], "Hauptstraße 2")

    def test_blank_addition_ignored(self):
        self.plain.name_addition = "   "
        self.assertEqual(self._lines(self.plain)[1], "Hauptstraße 2")

    def test_context_skips_addition(self):
        lines = self._lines(self.company.with_context(skip_name_addition=True))
        self.assertEqual(lines[1], "Musterweg 1")

    def test_contact_address_recomputed(self):
        self.plain.name_addition = "Werk Nord"
        self.assertIn("Werk Nord\nHauptstraße 2", self.plain.contact_address)

    def test_contact_widget(self):
        converter = self.env["ir.qweb.field.contact"]
        html = converter.value_to_html(
            self.company, {"fields": ["name", "address"], "no_marker": True}
        )
        self.assertIn("Praxis am Markt - Physiotherapie", html)
        html = converter.value_to_html(
            self.company,
            {
                "fields": ["name", "address"],
                "no_marker": True,
                "no_name_addition": True,
            },
        )
        self.assertNotIn("Praxis am Markt", html)
        self.assertIn("Musterweg 1", html)
        self.assertEqual(converter.value_to_html(False, {}), "")
        self.assertIn("no_name_addition", converter.get_available_options())
