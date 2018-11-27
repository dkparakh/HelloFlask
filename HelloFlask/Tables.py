from datetime import datetime
from run import db

class Customers(db.Model):
    __tablename__ = 'customers'

    customer_id = db.Column(db.Integer, primary_key=True)
    # True if Organisation, False for Individuals
    organisation = db.Column(db.Boolean)
    # Name of the organisation or First Name of the individual - Mandatory
    first_name = db.Column(db.String(100), nullable=False, index=True)
    # Middle Name of the individual - Optional
    middle_name = db.Column(db.String(100))
    # Last Name of the individual - Optional
    last_name = db.Column(db.String(100))
    # Gender of the individual - Optional
    gender = db.Column(db.Boolean)  # True for Male and False for Female
    # email address - mandatory
    email_address = db.Column(db.String(100), nullable=False, index=True)
    # password - mandatory
    login_password = db.Column(db.String(100), nullable=False, index=True)
    # phone number - mandatory
    phone_number = db.Column(db.String(15), nullable=False, index=True)
    # whatsapp number - Optional
    whatsapp_number = db.Column(db.String(15))

    customer_id, organisation, first_name, middle_name, last_name, gender, email_address, login_password, phone_number, whatsapp_number
    def __init__(self, customer_id, organisation=False, first_name, middle_name=None, last_name=None, gender=True, email_address, login_password, phone_number, whatsapp_number=None):
        self.customer_id = customer_id
        self.organisation = organisation
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.gender = gender
        self.email_address = email_address
        self.login_password = login_password
        self.phone_number = phone_number
        self.whatsapp_number = whatsapp_number

    def __repr__(self):
        return 'Customer id = {}' \
               'Organisation = {}' \
               'First Name = {}' \
               'Middle Name = {}' \
               'Last Name = {}' \
               'Gender = {}' \
               'email address = {}' \
               'Password = {}' \
               'Phone number = {}' \
               'Whatsapp number = {}' \
            .format(self.customer_id, self.organisation, self.first_name, self.middle_name, self.last_name, self.gender, self.email_address, self.login_password, self.phone_number, self.whatsapp_number)


class Orders(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    date_order_placed = db.Column(db.DateTime, default=datettime.utcnow())
    order_details = db.Column(db.String(500))

    # Relationship
    customer_id = db.Column(db.Integer, db.Foreignkey('customers.customer_id'))
    order_status_code = db.Column(db.Integer, db.Foreignkey('ref_order_status_codes.order_status_code'))


    order_id = order_id
    customer_id = customer_id

    order_status_code = order_status_code

    date_order_placed = date_order_placed

    order_details = order_details

    customer_id = db.Column(db.Integer, primary_key=True)
    # True if Organisation, False for Individuals
    organisation = db.Column(db.Boolean)
    # Name of the organisation or First Name of the individual - Mandatory
    first_name = db.Column(db.String(100), nullable=False, index=True)
    # Middle Name of the individual - Optional
    middle_name = db.Column(db.String(100))
    # Last Name of the individual - Optional
    last_name = db.Column(db.String(100))
    # Gender of the individual - Optional
    gender = db.Column(db.Boolean)  # True for Male and False for Female
    # email address - mandatory
    email_address = db.Column(db.String(100), nullable=False, index=True)
    # password - mandatory
    login_password = db.Column(db.String(100), nullable=False, index=True)
    # phone number - mandatory
    phone_number = db.Column(db.String(15), nullable=False, index=True)
    # whatsapp number - Optional
    whatsapp_number = db.Column(db.String(15))

    customer_id, organisation, first_name, middle_name, last_name, gender, email_address, login_password, phone_number, whatsapp_number
    def __init__(self, customer_id, organisation=False, first_name, middle_name=None, last_name=None, gender=True, email_address, login_password, phone_number, whatsapp_number=None):
        self.customer_id = customer_id
        self.organisation = organisation
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.gender = gender
        self.email_address = email_address
        self.login_password = login_password
        self.phone_number = phone_number
        self.whatsapp_number = whatsapp_number

    def __repr__(self):
        return 'Customer id = {}' \
               'Organisation = {}' \
               'First Name = {}' \
               'Middle Name = {}' \
               'Last Name = {}' \
               'Gender = {}' \
               'email address = {}' \
               'Password = {}' \
               'Phone number = {}' \
               'Whatsapp number = {}' \
            .format(self.customer_id, self.organisation, self.first_name, self.middle_name, self.last_name, self.gender, self.email_address, self.login_password, self.phone_number, self.whatsapp_number)





Ref_payment_methods

payment_method_code

payment_method_description


Customer_payment_methods

customer_payment_id

customer_id

payment_method_code

credit_card_number

payment_method_details


Ref_order_status_codes

order_status_code

order_status_description

Ref_product_types

product_type_code

parent_product_type_code

product_type_description


Products

product_id

product_type_code

return_merchandise_authorisation_number

product_name

product_price

product_colour

product_size

product_description

other_product_details



Invoices

invoice_number

order_id

invoice_status_code

invoice_date

invoice_details


Shipments

shipment_id

invoice_number

shipment_tracking_number

shipment_date

other_shipment_details



Order_items

order_item_id

product_id

order_id

order_item_status_code

order_item_quantity

order_item_price

RMA_number

RMA_issued_by

RMA_issued_date

othe_order_item_details


Ref_invoice_status_codes

invoice_status_code

invoice_status_description



Payments

payment_id

invoice_number

payment_date

payment_amount



Shipment_items

shipment_id

order_item_id



Ref_order_item_status_codes

order_item_status_code

order_item_status_description
