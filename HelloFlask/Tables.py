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
    date_order_placed = db.Column(db.DateTime, default=datetime.utcnow())
    order_details = db.Column(db.String(500))

    # Relationship
    customer_id = db.Column(db.Integer, db.Foreignkey('customers.customer_id'))
    order_status_code = db.Column(db.Integer, db.Foreignkey('ref_order_status_codes.order_status_code'))



    def __init__(self, order_id, customer_id, order_status_code, date_order_placed, order_details):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_status_code = order_status_code
        self.date_order_placed = date_order_placed
        self.order_details = order_details

    def __repr__(self):
        return 'Order ID = {}' \
               'Customer ID = {}' \
               'Order Status Code = {}' \
               'Date Order Placed = {}' \
               'Order Details = {}' \
            .format(self.order_id, self.customer_id, self.order_status_code, self.date_order_placed, self.order_details)

class Ref_Payment_Methods(db.Model):
    __tablename__ = 'ref_payment_methods'

    payment_method_code = db.Column(db.Integer, primary_key=True)
    payment_method_description = db.Column(db.String(100), nullable=False, index=True)

    def __init__(self, payment_method_code, payment_method_description):
        self.payment_method_code = payment_method_code
        self.payment_method_description = payment_method_description

    def __repr__(self):
        return 'Payment Method Code = {} ' \
               'Payment Method Description = {}'\
            .format(self.payment_method_code, self.payment_method_description)

class Customer_Payment_Methods(db.Model):

    __tablename__ = 'customer_payment_methods'

    customer_payment_id = db.Column(db.Integer, primary_key=True)
    credit_card_number = db.Column(db.String(15))
    payment_method_details = db.Column(db.String(500))

    # Relationship
    customer_id = db.Column(db.Integer, db.Foreignkey('customers.customer_id'))
    payment_method_code = db.Column(db.Integer, db.Foreignkey('ref_payment_methods.payment_method_code'))



    def __init__(self, customer_payment_id, customer_id, payment_method_code, credit_card_number, payment_method_details):
        self.customer_payment_id = customer_payment_id
        self.customer_id = customer_id
        self.payment_method_code = payment_method_code
        self.credit_card_number = credit_card_number
        self.payment_method_details = payment_method_details

    def __repr__(self):
        return 'Customer Payment ID = {}' \
               'Customer ID = {}' \
               'Payment Method Code = {}' \
               'Credit Card Number = {}' \
               'Payment Method Details = {}' \
            .format(self.customer_payment_id, self.customer_id, self.payment_method_code, self.credit_card_number, self.payment_method_details)

class Ref_order_status_codes(db.Model):
    __tablename__ = 'ref_order_status_codes'

    order_status_code = db.Column(db.Integer, primary_key=True)
    order_status_description = db.Column(db.String(100), nullable=False, index=True)

    def __init__(self, order_status_code, order_status_description):
        self.order_status_code = order_status_code
        self.order_status_description = order_status_description

    def __repr__(self):
        return 'Order Status Code = {}' \
               'Order Status Description = {}' \
            .format(self.order_status_code, self.order_status_description)

class Ref_product_types(db.Model):

    __tablename__ = 'ref_product_types'

    product_type_code = db.Column(db.Integer, primary_key=True)
    parent_product_type_code = db.Column(db.Integer, db.Foreignkey('ref_product_types.product_type_code'))
    product_type_description = db.Column(db.String(500))

    def __init__(self, product_type_code, parent_product_type_code, product_type_description):
        self.product_type_code = product_type_code
        self.parent_product_type_code = parent_product_type_code
        self.product_type_description = product_type_description

    def __repr__(self):
        return 'Product Type Code = {}' \
               'Parent Product Type Code = {}' \
               'Product Type Description = {}' \
            .format(self.product_type_code, self.parent_product_type_code, self.product_type_description)

class Products(db.Model):

    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    product_type_code = db.Column(db.Integer, db.Foreignkey('ref_product_types.product_type_code'))
    return_merchandise_authorisation_number = db.Column(db.Integer)
    product_name = db.Column(db.String(100))
    product_price = db.Column(db.Float)
    product_colour = db.Column(db.String(50))
    product_size = db.Column(db.Integer, nullable=False)
    product_description = db.Column(db.String(100), nullable=False, index=True)
    other_product_details = db.Column(db.String(100))

    def __init__(self, product_id, product_type_code, return_merchandise_authorisation_number, product_name, product_price, product_colour, product_size, product_description, other_product_details):
        self.product_id = product_id
        self.product_type_code = product_type_code
        self.return_merchandise_authorisation_number = return_merchandise_authorisation_number
        self.product_name = product_name
        self.product_price = product_price
        self.product_colour = product_colour
        self.product_size = product_size
        self.product_description = product_description
        self.other_product_details = other_product_details

    def __repr__(self):
        return 'Product ID = {}' \
               'Organisation = {}' \
               'Return Merchandise Authorisation Number = {}' \
               'Product Name = {}' \
               'Product Price = {}' \
               'Product Colour = {}' \
               'Product Size = {}' \
               'Product Description = {}' \
               'Other Product Details = {}' \
            .format(self.product_id, self.organisation, self.return_merchandise_authorisation_number, self.product_name,
                    self.product_price, self.product_colour, self.product_size, self.product_description, self.other_product_details)

class Ref_invoice_status_codes(db.Model):

    __tablename__ = 'ref_invoice_status_codes'

    invoice_status_code = db.Column(db.Integer, primary_key=True)
    invoice_status_description = db.Column(db.String(100), nullable=False, index=True)

    def __init__(self, invoice_status_code, invoice_status_description):
        self.invoice_status_code = invoice_status_code
        self.invoice_status_description = invoice_status_description

    def __repr__(self):
        return 'invoice_status_code = {}' \
               'invoice_status_description = {}' \
            .format(self.invoice_status_code, self.invoice_status_description)

class Ref_order_item_status_codes(db.Model):

    __tablename__ = 'ref_order_item_status_codes'

    order_item_status_code = db.Column(db.Integer, primary_key=True)
    order_item_status_description = db.Column(db.String(100), nullable=False, index=True)

    def __init__(self, order_item_status_code, order_item_status_description):
        self.order_item_status_code = order_item_status_code
        self.order_item_status_description = order_item_status_description

    def __repr__(self):
        return 'order_item_status_code = {}' \
               'order_item_status_description = {}' \
            .format(self.order_item_status_code, self.order_item_status_description)

class Invoices(db.Model):

    __tablename__ = 'invoices'

    invoice_number = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.Foreignkey('orders.order_id'))
    invoice_status_code = db.Column(db.Integer, db.Foreignkey('Ref_invoice_status_codes.invoice_status_code'))
    invoice_date = db.Column(db.DateTime, default=datetime.utcnow())
    invoice_details = db.Column(db.String(50))



    def __init__(self, invoice_number, order_id, invoice_status_code, invoice_date, invoice_details):
        self.invoice_number = invoice_number
        self.order_id = order_id
        self.invoice_status_code = invoice_status_code
        self.invoice_date = invoice_date
        self.invoice_details = invoice_details

    def __repr__(self):
        return 'Invoice Number = {}' \
               'Order ID = {}' \
               'Invoice Status Code = {}' \
               'Invoice Date = {}' \
               'Invoice Details = {}' \
            .format(self.invoice_number, self.order_id, self.invoice_status_code, self.invoice_date, self.invoice_details)

class Shipments(db.Model):

    __tablename__ = 'shipments'

    shipment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.Foreignkey('orders.order_id'))
    invoice_number = db.Column(db.Integer, db.Foreignkey('invoices.invoice_number'))
    shipment_tracking_number = db.Column(db.String(100), nullable=False, index=True)
    shipment_date = db.Column(db.DateTime, default=datetime.utcnow())
    other_shipment_details = db.Column(db.String(100))

    def __init__(self, shipment_id, order_id, invoice_number, shipment_tracking_number, shipment_date, other_shipment_details):
        self.shipment_id = shipment_id
        self.order_id = order_id
        self.invoice_number = invoice_number
        self.shipment_tracking_number = shipment_tracking_number
        self.shipment_date = shipment_date
        self.other_shipment_details = other_shipment_details

    def __repr__(self):
        return 'Shipment ID = {}' \
               'Order ID = {}' \
               'Invoice Number = {}' \
               'Shipment Tracking Number = {}' \
               'Shipment Date = {}' \
               'Other Shipment Details = {}' \
            .format(self.shipment_id, self.order_id, self.invoice_number, self.shipment_tracking_number, self.shipment_date, self.other_shipment_details)

class Order_items(db.Model):

    __tablename__ = 'order_items'

    order_item_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.Foreignkey('products.product_id'))
    order_id = db.Column(db.Integer, db.Foreignkey('orders.order_id'))
    order_item_status_code = db.Column(db.Integer, db.Foreignkey('Ref_order_item_status_codes.order_item_status_code'))
    order_item_quantity = db.Column(db.Integer)
    order_item_price = db.Column(db.Float)
    RMA_number = db.Column(db.Integer)
    RMA_issued_by = db.Column(db.String(100))
    RMA_issued_date = db.Column(db.DateTime)
    other_order_item_details = db.Column(db.String(50))

    def __init__(self, order_item_id, product_id=False, order_id, order_item_status_code=None, order_item_quantity=None, order_item_price=True, RMA_number, RMA_issued_by, RMA_issued_date, other_order_item_details=None):
        self.order_item_id = order_item_id
        self.product_id = product_id
        self.order_id = order_id
        self.order_item_status_code = order_item_status_code
        self.order_item_quantity = order_item_quantity
        self.order_item_price = order_item_price
        self.RMA_number = RMA_number
        self.RMA_issued_by = RMA_issued_by
        self.RMA_issued_date = RMA_issued_date
        self.other_order_item_details = other_order_item_details

    def __repr__(self):
        return 'Order Item ID = {}' \
               'Product ID = {}' \
               'Order ID = {}' \
               'Order Item Status Code = {}' \
               'Order Item Quantity = {}' \
               'Order Item Price = {}' \
               'RMA Number = {}' \
               'RMA Issued By = {}' \
               'RMA Issued Date = {}' \
               'Other Order Item Details = {}' \
            .format(self.order_item_id, self.product_id, self.order_id, self.order_item_status_code, self.order_item_quantity, self.order_item_price, self.RMA_number, self.RMA_issued_by, self.RMA_issued_date, self.other_order_item_details)

class Payments(db.Model):

    __tablename__ = 'payments'

    payment_id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.Integer, db.Foreignkey('invoices.invoice_number'))
    payment_date = db.Column(db.DateTime, default=datetime.utcnow())
    payment_amount = db.Column(db.Float)

    def __init__(self, payment_id, invoice_number, payment_date, payment_amount):
        self.payment_id = payment_id
        self.invoice_number = invoice_number
        self.payment_date = payment_date
        self.payment_amount = payment_amount

    def __repr__(self):
        return 'Payment ID = {}' \
               'invoice_number = {}' \
               'payment_date = {}' \
               'payment_amount = {}' \
            .format(self.payment_id, self.invoice_number, self.payment_date, self.payment_amount)

class Shipment_items(db.Model):
    __tablename__ = 'shipment_items'

    shipment_id = db.Column(db.Integer, db.Foreignkey('shipments.shipment_id'))
    order_item_id = db.Column(db.Integer, db.Foreignkey('order_items.order_item_id'))

    def __init__(self, shipment_id, order_item_id):
        self.shipment_id = shipment_id
        self.order_item_id = order_item_id

    def __repr__(self):
        return 'Shipment ID = {}' \
               'Order Item ID = {}' \
            .format(self.shipment_id, self.order_item_id)
