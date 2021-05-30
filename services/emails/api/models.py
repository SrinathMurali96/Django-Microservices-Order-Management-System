from django.db import models 


class Email(models.Model):
	sender = models.EmailField()
	receiver = models.EmailField()
	subject = models.CharField(max_length=300)
	body = models.TextField()
	
	class Meta:
        db_table = 'REF_EMAIL'