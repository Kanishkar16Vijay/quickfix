import frappe


def permission_for_techs(user=None):
	if not user:
		user = frappe.session.user

	if "QF Manager" in frappe.get_roles(user) or "QF Service Staff" in frappe.get_roles(user):
		return ""
	else:
		return f"(tabTechnician.user = '{user}')"


def permission_for_assign_jc(user=None):
	if not user:
		user = frappe.session.user

	if "QF Manager" in frappe.get_roles(user) or "QF Service Staff" in frappe.get_roles(user):
		return ""
	else:
		return f"(tabJob Card.assigned_technician IN (SELECT name FROM `tabTechnician` WHERE user = {user}))"


def service_invoice_permission_for_paid(doc, user=None):
	if not user:
		user = frappe.sesion.user

	if "QF Manager" in frappe.get_roles(user):
		return True

	payment_status = frappe.db.get_value("Job Card", doc.job_card, "payment_status")
	if payment_status != "Paid":
		return False

	return True
