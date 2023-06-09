import frappe

# this will auto set custom fields value, and it will be useful when doing multiple variants item, as they are created through backend
def update_conversion_factor(doc,event):
	if doc.attributes and doc.variant_of:
		for row in doc.attributes:
			if row.get('attribute') == 'Height':
				doc.height = int(row.get('attribute_value'))
			if row.get('attribute') == 'Width':
				doc.width = int(row.get('attribute_value'))
			if row.get('attribute') == 'Yield':
				doc.yield_ = float(row.get('attribute_value'))
	if not doc.has_variants:
		update_uoms_conversion(doc)

# Update UOM Conversion table
def update_uoms_conversion(doc):
	for row in doc.uoms:
		if row.formula:
			row.conversion_factor = eval(str(row.formula))
