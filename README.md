# helpdesk_tricks_task_TopGaz_company_V17_18
# Helpdesk Customization Module

## Overview
This Odoo module extends the **Helpdesk Ticket** model (`helpdesk.ticket`) by adding custom fields that allow storing additional customer and case information.

## Added Fields
The following fields have been added to `helpdesk.ticket`:

- **x_customer_name** (`Char`) – User Name
- **x_customer_phone** (`Char`) – Phone
- **street** (`Char`) – Street
- **street2** (`Char`) – Street 2
- **city** (`Char`) – City
- **state_id** (`Many2one → res.country.state`) – State
- **country_id** (`Many2one → res.country`) – Country
- **cost** (`Char`) – Cost
- **technician_name** (`Char`) – Technician name
- **x_case_number** (`Char`) – Case Number
- **x_issue_description** (`Text`) – Problem
- **x_purchase_date** (`Date`) – Purchase Date
- **x_case_date** (`Date`) – Case Date

## Installation
1. Copy the module folder into your Odoo `addons` directory.
2. Restart your Odoo server.
3. Update the app list from Odoo.
4. Install the module **Helpdesk Customization**.

## Usage
After installing this module, you will find the new fields inside the **Helpdesk Tickets** form view.  
These fields allow you to capture customer details, technical information, and case-related data.

## Compatibility
- Odoo Version: **17.0** (Community/Enterprise)

## Author
- **Developer:** محمد النايض  
- **Company:** *Custom Development*  

---
