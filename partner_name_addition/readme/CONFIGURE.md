Nothing to configure. Report layouts that print the name lines on their own can
show the name addition where they want it
(`partner.commercial_partner_id.name_addition`) and print the remaining address
with the option `no_name_addition` of the contact widget, so it does not appear
twice:

    <div t-field="o.partner_id"
         t-options="{'widget': 'contact', 'fields': ['address'], 'no_name_addition': True}"/>

In Python, the context key `skip_name_addition` has the same effect on
`_display_address()`.
