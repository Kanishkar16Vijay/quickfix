# Copyright (c) 2026, Kanishkar and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class SparePart(Document):
	def validate(self):
		if self.selling_price < self.unit_cost:
			frappe.throw(_("Selling Price should be greater than Unit Cost"))
