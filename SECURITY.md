# Security Policy

## Supported versions

Security fixes are made on the branch `19.0` and released as a new version `19.0.x.y.z`
of the affected modules. Older versions are not maintained.

| Branch | Supported |
| ------ | --------- |
| 19.0   | yes       |

## Reporting a vulnerability

Please do not report security problems in public issues, pull requests or discussions.

- Preferably use the private vulnerability reporting of GitHub: tab _Security_, _Report
  a vulnerability_ in
  [BM1-de/odoo-partner-name-addition](https://github.com/BM1-de/odoo-partner-name-addition/security).
- Or write an e-mail to the maintainer, Phillip Baumgärtner <baumgaertner@bm1.de>, with
  the subject "Security odoo-partner-name-addition".

Describe the problem, the affected module and version, how to reproduce it and its
possible impact. Do not send real tax or personal data; use synthetic data for the
example.

We confirm the receipt, examine the report, keep you informed and publish a fix together
with a security notice in the changelog (`HISTORY.md` of the module). We credit you
unless you prefer not to be named.

## Scope

In scope are the modules of this repository, in particular:

- injection through the name addition of a contact into addresses, reports or the portal
  (the name addition is escaped like any other field of the address);
- name additions of other contacts or companies shown to users or portal users who may
  not see these contacts.

Out of scope are vulnerabilities of Odoo itself or of other modules (please report them
to their maintainers) and wrong results without a security impact (please open a normal
issue, without real data).

## Note

The modules send no data anywhere. They are provided free of charge and without warranty
under the GNU AGPL-3.0 (see `LICENSE`).
