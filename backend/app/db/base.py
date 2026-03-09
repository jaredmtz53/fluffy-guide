from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

from backend.app.models import (
    Category,
    EmailVerificationToken,
    Favorite,
    Listing,
    ListingImage,
    ListingOffer,
    Message,
    MessageThread,
    Notification,
    PhoneVerificationCode,
    Report,
    Review,
    User,
    VerificationRequest,
)