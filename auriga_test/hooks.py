from . import __version__ as app_version

app_name = "auriga_test"
app_title = "Auriga Test"
app_publisher = "auriga"
app_description = "test app for ui"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "guruprasad.kondiba@aurigait.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/auriga_test/css/auriga_test.css"
# app_include_js = "/assets/auriga_test/js/auriga_test.js"

# include js, css files in header of web template
# web_include_css = "/assets/auriga_test/css/auriga_test.css"
# web_include_js = "/assets/auriga_test/js/auriga_test.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "auriga_test/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {"Item" : "public/js/item.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "auriga_test.install.before_install"
# after_install = "auriga_test.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "auriga_test.uninstall.before_uninstall"
# after_uninstall = "auriga_test.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "auriga_test.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
# 	}
# }

doc_events = {
	"Item": {
		"before_save": "auriga_test.auriga_test.docevents.item.update_conversion_factor"
	}
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"auriga_test.tasks.all"
#	],
#	"daily": [
#		"auriga_test.tasks.daily"
#	],
#	"hourly": [
#		"auriga_test.tasks.hourly"
#	],
#	"weekly": [
#		"auriga_test.tasks.weekly"
#	]
#	"monthly": [
#		"auriga_test.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "auriga_test.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "auriga_test.event.get_events"
# }
# 
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "auriga_test.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["auriga_test.utils.before_request"]
# after_request = ["auriga_test.utils.after_request"]

# Job Events
# ----------
# before_job = ["auriga_test.utils.before_job"]
# after_job = ["auriga_test.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"auriga_test.auth.validate"
# ]

