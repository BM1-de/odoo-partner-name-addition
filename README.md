

# Namenszusatz für Odoo
<!-- /!\ Non OCA Context : Set here the badge of your runbot / runboat instance. -->
[![Pre-commit Status](https://github.com/BM1-de/odoo-partner-name-addition/actions/workflows/pre-commit.yml/badge.svg?branch=19.0)](https://github.com/BM1-de/odoo-partner-name-addition/actions/workflows/pre-commit.yml?query=branch%3A19.0)
[![Build Status](https://github.com/BM1-de/odoo-partner-name-addition/actions/workflows/test.yml/badge.svg?branch=19.0)](https://github.com/BM1-de/odoo-partner-name-addition/actions/workflows/test.yml?query=branch%3A19.0)
[![codecov](https://codecov.io/gh/BM1-de/odoo-partner-name-addition/branch/19.0/graph/badge.svg)](https://codecov.io/gh/BM1-de/odoo-partner-name-addition)
<!-- /!\ Non OCA Context : Set here the badge of your translation instance. -->

<!-- /!\ do not modify above this line -->

Ein Feld *Namenszusatz* am Kontakt: eine zweite Namenszeile wie ein Geschäftsname, eine
Abteilung oder der Name einer Praxis. Odoo druckt sie in jeder Anschrift unter dem Namen
und über der Straße – in Angeboten, Aufträgen, Rechnungen, Lieferscheinen und im Portal:

```text
Anna Beispiel
Praxis am Markt – Physiotherapie
Musterweg 1
12345 Musterstadt
```

> **Alpha:** Das Modul ist neu. Die Software wird ohne Gewährleistung bereitgestellt
> (AGPL-3.0, Abschnitte 15 und 16).

## Was das Modul tut

- Odoo hat für die zweite Namenszeile kein Feld. Die üblichen Behelfe schreiben den Zusatz
  in den Firmennamen (dann steht er überall in einer Zeile) oder in die zweite
  Straßenzeile (die Odoo nach der Straße druckt und E-Rechnungen als Teil der Straße
  ausgeben).
- Ansprechpartner und Adressen einer Firma übernehmen den Namenszusatz der Firma, solange
  sie keinen eigenen haben.
- Kontakte ohne Namenszusatz bleiben unverändert.

## Einrichtung

- Den Namenszusatz am Kontakt unter dem Namen eintragen.
- Eigene Berichtslayouts, die die Namenszeilen selbst drucken, können den Zusatz an ihre
  Stelle setzen (`partner.commercial_partner_id.name_addition`) und die übrige Anschrift
  mit der Option `no_name_addition` des Kontakt-Widgets drucken, damit er nicht doppelt
  erscheint.

## Grenzen

- Der Namenszusatz gehört nicht zum Anzeigenamen; in Listen und Auswahlfeldern erscheint
  er nicht.
- E-Rechnungen (Factur-X, XRechnung) enthalten ihn nicht; sie haben kein Feld für eine
  zweite Namenszeile des Käufers.

## Mehr Dokumentation

Die Beschreibung des Moduls (englisch) steht in
[partner_name_addition/README.rst](partner_name_addition/README.rst).

*English: A second name line on the contact (trade name, department), printed in every
address between the name and the street. Alpha, no warranty.*

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[partner_name_addition](partner_name_addition/) | 19.0.1.0.0 | <a href='https://github.com/bm1-phillip'><img src='https://github.com/bm1-phillip.png' width='32' height='32' style='border-radius:50%;' alt='bm1-phillip'/></a> | Second name line on the contact (trade name, department) between the name and the street of the address

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Baumgärtner Marketing GmbH
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
<!-- /!\ Non OCA Context : Set here the full description of your organization. -->
