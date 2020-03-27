import base64
from django.template import loader
from django.conf import settings
from sendgrid import SendGridAPIClient, Content
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
from backend.apps.utils.print_colors import _green, _red


def send(**kwargs):
    print('sending message')
    print(_green(kwargs))
    result = True
    body = Content("text/html", loader.render_to_string(
        kwargs.get('email_template'),
        kwargs.get('context')
    ))
    try:
        message = Mail(
            from_email=settings.SENGRID_SENDER_EMAIL,
            to_emails=kwargs.get('to_email'),
            subject=kwargs.get('subject'),
            html_content=body
        )
        file_path = kwargs.get('file_path')
        with open(file_path, 'rb') as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        attachment = Attachment()
        attachment.file_content = FileContent(encoded)
        attachment.file_type = FileType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        attachment.file_name = FileName(file_path.split('/')[1])
        attachment.disposition = Disposition("attachment")
        attachment.content_id = ContentId("Excel Document file")
        message.add_attachment(attachment)

        sengrid_email = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        email_request = sengrid_email.send(message)
        print(_green('----------- sendgrid email response -----------'))
        print(email_request.status_code)
        print(email_request.body)
        print(email_request.headers)
        print(_green('----------- sendgrid email response -----------'))
    except Exception as e:
        result = False
        print(_red('Error sending email caused by : {}'.format(str(e))))
    return result