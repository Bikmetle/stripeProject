
stripe.com is a payment system with API and test mode for simulating and testing payments.

Using the python stripe library, you can create payment forms of various types, customer input data,
and implement other payment functions.

This is a single html page that talks to Stripe and creates payment forms for products.
The project uses Django and Stripe API

API with two methods:
GET /buy/{id}
to get the Stripe Session Id to pay for the selected product.
GET /item/{id}
to get a simple HTML page with information about the selected item and a Buy button.

There are 3 items, but you can add more in django admin.