from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.template.loader import render_to_string
from NewsPaper import settings
from .models import Post


def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'new_post.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@receiver(m2m_changed, sender=Post)
def news_created(sender, instance,  **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.PostCategory.all()
        subscribers_emails = []
        for categoryThrough in categories:
            subscribers = categoryThrough.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk(), instance.title(), subscribers_emails)
