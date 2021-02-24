import frappe
import json
from frappe import _

def create_lead(customer_signup, method):
    new_lead = frappe.get_doc({
        "doctype": "Lead",
        "lead_name" : customer_signup.full_name,
        "email_id" : str(customer_signup.email),
        "mobile_no" : str(customer_signup.phone_number),
        "how_did_you_find_us" : "Social Media",
        "source" : "Signup",
    })
    new_lead.flags.ignore_permission = True
    new_lead.insert()