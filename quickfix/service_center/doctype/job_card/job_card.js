// Copyright (c) 2026, Kanishkar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Job Card", {
	refresh(frm) {
		frm.doc.labour_charge = frappe.get_single_value(
			"QuickFix Setting",
			"default_labour_charge"
		);
	},
});
