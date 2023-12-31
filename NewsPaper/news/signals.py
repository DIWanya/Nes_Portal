from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.template.loader import render_to_string
from NewsPaper import settings
from .models import PostCategory
from .tasks import send_notifications


# def send_notifications(pk, title, subscribers):
#     html_content = render_to_string(
#         'new_post.html',
#         {
#             'text': title,
#             'link': f'{settings.SITE_URL}/news/{pk}'
#         }
#     )
#     msg = EmailMultiAlternatives(
#         subject=title,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers,
#     )
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()


@receiver(m2m_changed, sender=PostCategory)
def news_created(sender, instance,  **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.postCategory.all()
        subscribers_emails = []
        for category in categories:
            subscribers = category.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        send_notifications.delay(instance.pk, instance.title, subscribers_emails)
