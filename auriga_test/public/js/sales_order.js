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
                                    columns:2
                                },
                                {
                                    label: 'Actual Qty',
                                    fieldname: 'actual_qty',
                                    fieldtype: 'Float',
                                    in_list_view:1,
                                    read_only:1,
                                    columns:2
                                },
                                {
                                    label: 'Reserved',
                                    fieldname: 'reserved',
                                    fieldtype: 'Float',
                                    in_list_view:1,
                                    read_only:1,
                                    // reqd:1,
                                    columns:2
                                },
                                {
                                    label: 'Free for Reserve',
                                    fieldname: 'a_reserve',
                                    fieldtype: 'Float',
                                    in_list_view:1,
                                    read_only:1,
                                    columns:2
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
                            method: "auriga_test.auriga_test.custom.sales_order.sales_reservation",
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
                        var free_for_reserve = 0;
                        var t_reserved = 0;
                        frappe.call({
                            method: "auriga_test.auriga_test.custom.sales_order.get_actual_reserved_qty",
                            args: {
                                item:q.item_code,
                                warehouse:q.warehouse,
                            },
                            async:false,
                            callback: function(r) {
                                console.log("hhhhhhh",r.message)
                                t_reserved = r.message
                                free_for_reserve = q.actual_qty - t_reserved
                            }
                        });
                        d.fields_dict.reserved_qty_details.df.data.push({
                            'item_code': q.item_code,
                            'reserved_qty': q.qty,
                            'actual_qty': q.actual_qty,
                            'reserved':t_reserved,
                            'a_reserve':free_for_reserve,
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
                d.$wrapper.find('.modal-dialog').css("max-width", "50%").css("width", "50%");
            });
        }
	}
})
