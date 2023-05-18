import frappe
import json
from frappe.utils import now

@frappe.whitelist()
def sales_reservation(data):
	data = json.loads(data)
	cnt =0
	msg = f'''
				<table border ='1'>
					<tr>
						<td colspan = 4><b>For the below items you can't reserve qty</b></td>
					</tr>
					<tr>
						<td> Item </td>
						<td> Total Available Qty </td>
						<td> Available Qty for reservation </td>
						<td> Total Reserved Qty </td>
					</tr> 
			'''
	for row in data:
		item = row.get("item_code")
		warehouse = row.get("warehouse")
		qty_to_be_reserved = row.get("reserved_qty")
		reserved_qty = get_actual_reserved_qty(item,warehouse)


		# this actual_qty qty means qty which is available for sale i.e stock qty in warehouse
		total_available_qty = row.get("actual_qty")

		free_for_reserve = total_available_qty - reserved_qty
		if qty_to_be_reserved > free_for_reserve:
			free_for_reserve = 0 if free_for_reserve < 0 else free_for_reserve
			cnt += 1
			msg += f'''
						<tr>
							<td>{item}</td>
							<td>{total_available_qty}</td>
							<td>{free_for_reserve}</td>
							<td>{reserved_qty}</td>
						<tr>
					'''
		else:
			make_reservation(item,warehouse,row)
	if cnt:
		msg += '''</table> '''
		frappe.throw(msg)

def get_actual_reserved_qty(item,warehouse):
	query = """ 
		SELECT 
			SUM(quantity_reserved) as qty
		FROM 
			`tabTest Sales Reservation` 
		WHERE 
			reservation_status = 'Reserved' AND item_no = %(item)s AND warehouse = %(warehouse)s
	"""
	reserved_qty = frappe.db.sql(query,{'item':item,'warehouse':warehouse},as_dict=1,debug=1)
	return reserved_qty[0].get('qty') if reserved_qty[0].get('qty') else 0

def make_reservation(item,warehouse,row):
	srt_doc = frappe.new_doc("Test Sales Reservation")
	srt_doc.item_record_id = row.get("items_name")
	srt_doc.item_no = item
	srt_doc.item_name = warehouse
	srt_doc.quantity_reserved = row.get("reserved_qty")
	srt_doc.reserved_by = frappe.session.user
	srt_doc.reservation_date_and_time = now()
	srt_doc.so_no = row.get("sales_order")
	srt_doc.reservation_status = "Reserved"
	srt_doc.warehouse = row.get("warehouse")
	
	srt_doc.save(ignore_permissions=True)
	frappe.db.commit()