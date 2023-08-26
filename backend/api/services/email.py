#!/usr/bin/python3
"""Module to initialize routers and endpoints"""

from typing import Any, Dict, List

from api.config import settings
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from pydantic import BaseModel, EmailStr


class Mail(BaseModel):
    email: List[EmailStr]
    content: Dict[str, Any]


fm = FastMail(
    ConnectionConfig(
        MAIL_USERNAME=settings.MAIL_USERNAME,
        MAIL_PASSWORD=settings.MAIL_PASSWORD,
        MAIL_FROM=settings.MAIL_FROM,
        MAIL_PORT=settings.MAIL_PORT,
        MAIL_SERVER=settings.MAIL_SERVER,
        MAIL_TLS=settings.MAIL_TLS,
        MAIL_SSL=settings.MAIL_SSL
    )
)


async def simple_send(mail: Mail, template):
    message = MessageSchema(
        subject=mail.content.get(
            'subject') or 'AfriLegal API Password Reset',
        recipients=mail.email,
        body=template.format(**mail.content),
        subtype="html"
    )
    await fm.send_message(message)


async def send_in_background(background_tasks, mail: Mail, template: str):
    message = MessageSchema(
        subject=mail.content.get('subject') or 'AfriLegal API Password Reset',
        recipients=mail.email,
        body=template.format(**mail.content),
        subtype="html"
    )
    background_tasks.add_task(fm.send_message, message)
