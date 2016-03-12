#!/usr/bin/env python
# Note: Some Python best-practices have been sacrificed below for simplicity's sake.
import pdfplumber
import sys, os

COLUMNS = [ "state", "permit", "handgun", "long_gun", "other", "multiple", "admin", "prepawn_handgun", "prepawn_long_gun", "prepawn_other", "redemption_handgun", "redemption_long_gun", "redemption_other", "returned_handgun", "returned_long_gun", "returned_other", "rentals_handgun", "rentals_long_gun", "private_sale_handgun", "private_sale_long_gun", "private_sale_other", "return_to_seller_handgun", "return_to_seller_long_gun", "return_to_seller_other", "totals" ]

pdf_path = os.path.join(sys.argv[1])

pdf = pdfplumber.open(pdf_path)

first_page = pdf.pages[0]

cropped = first_page.crop((0, 80, first_page.width, 485))

table = cropped.extract_table(
    v="lines",
    h="gutters",
    x_tolerance=5,
    y_tolerance=5
)

print("\t".join(COLUMNS))
for row in table:
    cols = [ (row[i] or "") for i in range(len(COLUMNS)) ]
    print("\t".join(cols).replace(",", ""))
