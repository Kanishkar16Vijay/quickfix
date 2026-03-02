import frappe
from frappe.utils import add_to_date, now


def get_overdue_jobs():
	jobcard = frappe.qb.DocType("Job Card")

	over_due_jobs = (
		frappe.qb.from_(jobcard)
		.select(jobcard.name, jobcard.customer_name, jobcard.assigned_technician, jobcard.creation)
		.where(
			jobcard.workflow_state.isin(["Pending Diagnosis", "In Repair"]) & jobcard.creation
			< add_to_date(now(), days=7)
		)
		.orderby(jobcard.creation)
		.run(as_dict=True)
	)

	return over_due_jobs


def transfer_job(from_tech, to_tech):
	try:
		frappe.db.sql(
			"""
			UPDATE `tabJob Card`
			SET assigned_technician = %s
			WHERE assigned_technician = %s
			AND workflow_state IN (
				"Pending Diagnosis",
				"Awaiting Customer Approval",
				"In Repair"
			)
			""",
			(from_tech, to_tech),
		)
		frappe.db.commit()

	except Exception:
		frappe.db.rollback()
		frappe.log_error("Tranfer Job Failed", frappe.get_traceback(with_context=True))
