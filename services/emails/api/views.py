from rest_framework.views import APIView
from django.conf import settings
from django.core.mail import send_mail
from .models import Email
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
LOGGER = logging.getLogger(__name__)


@api_view(http_method_names=["POST"])
def email_send(request):
	"""
	This function is created to trigger Email to the Customer for Order confirmation
	created on: 24-May-2020
	Updated on: 24-May-2020
	"""
	sender = settings.EMAIL_HOST_USER
	LOGGER.info('Trigger Emails Method - Starts')
	try:
		# Fetching the email data to be sent
		receiver = request.data["receiver"]
		subject = request.data["subject"]
		body = request.data["body"]

		new_mail = Email.objects.create(
			sender=sender,
			receiver=receiver,
			subject=subject,
			body=body
		)
		
		# Triggering the Email
		send_mail(subject, body, sender, [receiver], fail_silently=False)
		return Response({"message": "Email sent successfully"}, status=200)
		LOGGER.info('Trigger Emails Method - Ends')
	except:
		return Response({"message": "Email sending error"}, status=500)






