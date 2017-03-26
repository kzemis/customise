# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "customise"
app_title = "Customise"
app_publisher = "kaspars.zemiitis@gmail.com"
app_description = "Customise"
app_icon = "octicon octicon-file-directory"
app_color = "orange"
app_email = "kaspars.zemiitis@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/customise/css/customise.css"
# app_include_js = "/assets/customise/js/customise.js"

# include js, css files in header of web template
# web_include_css = "/assets/customise/css/customise.css"
# web_include_js = "/assets/customise/js/customise.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "customise.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "customise.install.before_install"
# after_install = "customise.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "customise.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"customise.tasks.all"
# 	],
# 	"daily": [
# 		"customise.tasks.daily"
# 	],
# 	"hourly": [
# 		"customise.tasks.hourly"
# 	],
# 	"weekly": [
# 		"customise.tasks.weekly"
# 	]
# 	"monthly": [
# 		"customise.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "customise.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "customise.event.get_events"
# }

