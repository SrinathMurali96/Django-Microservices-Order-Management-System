from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import Order
import logging
LOGGER = logging.getLogger(__name__)


@api_view(http_method_names=["POST"])
def add_order(request):
	"""
	This function is created to place the order and save in Database
	created on: 24-May-2020
	Updated on: 29-May-2020
	"""
	LOGGER.info('Order confirmation Method Starts')
	try:
		total_price = 0
		
		# Storing the Order Data in the Database
		order = Order()
		order.customer_name = request.data["customer_name"]
		order.customer_email = request.data["customer_email"]
		order.items = []

		LOGGER.info(request.data)
		
		# Fetching each product details by sending the request to Product Microservice
		for product in request.data["products_id"]:
			response = requests.get("http://127.0.0.1:8002/products/fetch/?prod_id=%s" % product).json()
			print(response)
			total_price += float(response[0]["price"])

			order.items.append({
				"item_name": response[0]["name"],
				"item_description": response[0]["description"],
				"item_price": response[0]["price"],
			})
		order.total = total_price
		order.save()
		
		# Sending Order Confirmation mail to Customer by triggering request to Email Microservice
		send_email(order)
		LOGGER.info('Order confirmation Method Ends')
		return Response({"message": "Order successfully created!"})
	except Exception:
        LOGGER.error(traceback.format_exc())
		return Response({"message": "Order creation Failed!"})
		
def send_email(order):
	"""
	This function is created to trigger request to Email Microservice
	created on: 24-May-2020
	Updated on: 24-May-2020
	"""
	LOGGER.info('Email Service Request Method - Starts')
	try:
		# Triggering request to Email Microservice with request data
		requests.post("http://127.0.0.1:8003/emails/send/", data={
			"receiver": order.customer_email,
			"subject": "Order Created",
			"body": "Hello %s, your order has been created. Total of: %s. Thanks" % (order.customer_name, order.total)
		})
		LOGGER.info('Email Service Request Method - Ends')
	except Exception:
        LOGGER.error(traceback.format_exc())
		return Response({"message": "Email service request Failed!"})