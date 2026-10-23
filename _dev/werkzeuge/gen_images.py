# Copyright 2026 Baumgärtner Marketing GmbH
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
"""Banner and icon of the module (static/description).

In English, as the Odoo Apps Store requires, and in the style of the other BM1
modules. Runs inside the Odoo container, which has Pillow and the DejaVu
fonts::

    docker compose run --rm --no-deps -T --entrypoint python3 odoo - \
        < _dev/werkzeuge/gen_images.py
"""

# pylint: disable=print-used

from PIL import Image, ImageDraw, ImageFont

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DARK, LIGHT, ACCENT, WHITE = (
    (31, 58, 96),
    (233, 239, 247),
    (52, 120, 184),
    (255, 255, 255),
)


def fitted(draw, text, path, size, width):
    """Font of at most ``size`` points whose ``text`` fits into ``width``."""
    while size > 10:
        font = ImageFont.truetype(path, size)
        if draw.textlength(text, font=font) <= width:
            return font
        size -= 1
    return ImageFont.truetype(path, size)


def label(draw, text, box, color):
    """``text`` centred in the horizontal range of ``box`` at its top."""
    left, top, right = box
    font = fitted(draw, text, BOLD, 44, right - left)
    width = draw.textlength(text, font=font)
    draw.text((left + (right - left - width) / 2, top), text, font=font, fill=color)


def save_icon(img, out):
    img.resize((128, 128), Image.LANCZOS).save(out + "icon.png", optimize=True)


def banner(out, rows):
    width, height = 1120, 560
    margin = 80
    img = Image.new("RGB", (width, height), DARK)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, height - 120, width, height), fill=ACCENT)
    title, first, second, footer = rows
    for text, path, size, color, top in (
        (title, BOLD, 84, WHITE, 100),
        (first, REGULAR, 38, LIGHT, 240),
        (second, REGULAR, 38, LIGHT, 300),
        (footer, REGULAR, 30, WHITE, height - 82),
    ):
        font = fitted(draw, text, path, size, width - 2 * margin)
        draw.text((margin, top), text, font=font, fill=color)
    img.save(out + "banner.png", optimize=True)


def icon(out):
    size = 256
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((0, 0, size - 1, size - 1), radius=40, fill=DARK)
    # an address card: name, the name addition highlighted, street, city
    draw.rounded_rectangle((36, 44, 220, 212), radius=10, fill=WHITE)
    draw.rounded_rectangle((56, 70, 184, 86), radius=6, fill=DARK)
    draw.rounded_rectangle((52, 100, 204, 128), radius=8, fill=ACCENT)
    draw.rounded_rectangle((56, 146, 168, 158), radius=5, fill=(160, 172, 190))
    draw.rounded_rectangle((56, 176, 152, 188), radius=5, fill=(160, 172, 190))
    save_icon(img, out)


OUT = "/mnt/extra-addons/partner_name_addition/static/description/"
icon(OUT)
banner(
    OUT,
    (
        "Partner Name Addition",
        "A second name line such as a trade name or department,",
        "printed in every address between the name and the street",
        "Odoo 19 · quotations, invoices, delivery slips, portal",
    ),
)
print("ok")
