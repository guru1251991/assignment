frappe.ui.form.on('Sales Order', {
	refresh(frm) {
        if (frm.doc.docstatus == 1){
            frm.add_custom_button('Reserve Qty', () => {
                let data = [];
                let d = new frappe.ui.Dialog({
                    title: 'Items Qty Reservation',
                    fields: [
                        {
                            label: 'Reserve required qty for each item',
                            fieldname: 'reserved_qty_details',
                            fieldtype: 'Table',
                            cannot_add_rows: true,
                            data: data,
                            get_data: () => {
                                return data;
                            },
                            fields:[
                                {
                                    label: 'Item Code',
                                    fieldname: 'item_code',
                                    fieldtype: 'Link',
                                    options: 'Item',
                                    in_list_view:1,
                                    read_only :1,
                                    columns:2
                                },
                                {
                                    label: 'Qty to be Reserved',
                                    fieldname: 'reserved_qty',
                                    fieldtype: 'Float',
                                    in_list_view:1,
                                    reqd:1,
                                    columns:3
                                },
                                {
                                    label: 'Actual Qty',
                                    fieldname: 'actual_qty',
                                    fieldtype: 'Float',
                                    // in_list_view:1,
                                    columns:1,
                                    hidden:1
                                },
                                {
                                    label: 'Name',
                                    fieldname: 'items_name',
                                    fieldtype: 'Data',
                                    // in_list_view:1,
                                    hidden:1,
                                    columns:1
                                },
                                {
                                    label:'Item Name',
                                    fieldname: 'item_name',
                                    fieldtype: 'Data',
                                    // in_list_view:1,
                                    hidden:1,
                                    columns:1
                                },
                                {
                                    label:'Warehouse',
                                    fieldname: 'warehouse',
                                    fieldtype: 'Link',
                                    option: 'Warehousee',
                                    hidden:1,
                                    columns:1
                                },
                                {
                                    label:'Sales Order',
                                    fieldname: 'sales_order',
                                    fieldtype: 'Link',
                                    option: 'Sales Order',
                                    hidden:1,
                                    columns:1
                                },
                            ]
                        },
                    ],

                });
                d.set_primary_action(__('Add'), function() {
                    var dialog_data = d.get_values()
                        frappe.call({
                            method: "custom_app.custom_app.custom.sales_order.sales_reservation",
                            args: {
                                data:dialog_data.reserved_qty_details,
                            },
                            callback: function(r) {
                            }
                        });
                    d.hide();
                });
                if (! cur_frm.doc.__islocal){
                    cur_frm.doc.items.forEach(q => {
                        d.fields_dict.reserved_qty_details.df.data.push({
                            'item_code': q.item_code,
                            'reserved_qty': q.qty,
                            'actual_qty': q.actual_qty,
                            'items_name': q.name,
                            'item_name': q.item_name,
                            'warehouse': q.warehouse,
                            'sales_order': cur_frm.doc.name,
                        });
                    });
                    data = d.fields_dict.reserved_qty_details.df.data;
                    d.fields_dict.reserved_qty_details.grid.refresh();
                }
                d.show();
            });
        }
	}
})
