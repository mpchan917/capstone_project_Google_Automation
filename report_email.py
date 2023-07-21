#!/usr/bin/env python3

import reports
import os
import datetime
import run
import emails
import getpass

username = getpass.getuser()
txt_dir = os.path.join(os.getcwd()+ "/supplier-data/descriptions/")
photos_dir = os.path.join(os.getcwd()+ "/supplier-data/images/")
report_content = "<br/> <br/>"
def data_process(report_content):
    """Get needed items details from run modules"""
    items_list = run.get_items(txt_dir)
    for item in items_list:
        report_content += f"<br/>name: {item['name']}<br/>"
        report_content += f"<br/>weight: {item['weight']} lbs<br/>"
        report_content += "<br/> <br/>"
    return report_content

if __name__ == "__main__":
    #Generate daily report
    attachment = "/tmp/processed.pdf"
    today = datetime.date.today()
    title = f"Processed Update on {today.strftime ('%B %d, %Y')}"
    paragraph = data_process(report_content)
    reports.generate_report(attachment, title, paragraph)
    #Send email with daily report
    sender = "automation@example.com"
    receiver = username+"@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate(sender, receiver, subject, body, attachment)
    emails.send(message)


