from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
import enum

# ── Enums ──────────────────────────────────────────
class UserRole(str, enum.Enum):
    donor = "donor"
    orphanage = "orphanage"
    admin = "admin"

class RequestCategory(str, enum.Enum):
    food = "food"
    clothes = "clothes"
    education = "education"
    medical = "medical"
    others = "others"

class RequestPriority(str, enum.Enum):
    low = "low"
    medium = "medium"
    urgent = "urgent"

class RequestStatus(str, enum.Enum):
    active = "active"
    fulfilled = "fulfilled"

class DonationType(str, enum.Enum):
    item = "item"
    money = "money"

class DonationStatus(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"
    completed = "completed"

class DeliveryStatus(str, enum.Enum):
    pending = "pending"
    picked = "picked"
    delivered = "delivered"

# ── Users Table ────────────────────────────────────
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String)
    role = Column(Enum(UserRole), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    orphanage = relationship("Orphanage", back_populates="user", uselist=False)
    donations = relationship("Donation", back_populates="donor")
    notifications = relationship("Notification", back_populates="user")
    sent_messages = relationship("Message", back_populates="sender")

# ── Orphanages Table ───────────────────────────────
class Orphanage(Base):
    __tablename__ = "orphanages"

    orphanage_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    name = Column(String, nullable=False)
    address = Column(String)
    city = Column(String)
    contact = Column(String)
    description = Column(Text)
    document_proof = Column(String)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="orphanage")
    requests = relationship("Request", back_populates="orphanage")

# ── Requests Table ─────────────────────────────────
class Request(Base):
    __tablename__ = "requests"

    request_id = Column(Integer, primary_key=True, index=True)
    orphanage_id = Column(Integer, ForeignKey("orphanages.orphanage_id"))
    title = Column(String, nullable=False)
    category = Column(Enum(RequestCategory))
    description = Column(Text)
    image_path = Column(String)
    priority = Column(Enum(RequestPriority), default=RequestPriority.medium)
    status = Column(Enum(RequestStatus), default=RequestStatus.active)
    created_at = Column(DateTime, default=datetime.utcnow)

    orphanage = relationship("Orphanage", back_populates="requests")
    donations = relationship("Donation", back_populates="request")

# ── Donations Table ────────────────────────────────
class Donation(Base):
    __tablename__ = "donations"

    donation_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    request_id = Column(Integer, ForeignKey("requests.request_id"))
    donation_type = Column(Enum(DonationType))
    amount = Column(Float)
    items_description = Column(Text)
    quantity = Column(Integer)
    payment_method = Column(String)
    payment_proof = Column(String)
    pickup_address = Column(String)
    pickup_date = Column(DateTime)
    status = Column(Enum(DonationStatus), default=DonationStatus.pending)
    delivery_status = Column(Enum(DeliveryStatus), default=DeliveryStatus.pending)
    created_at = Column(DateTime, default=datetime.utcnow)

    donor = relationship("User", back_populates="donations")
    request = relationship("Request", back_populates="donations")
    payment = relationship("Payment", back_populates="donation", uselist=False)

# ── Payments Table ─────────────────────────────────
class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    donation_id = Column(Integer, ForeignKey("donations.donation_id"))
    payment_gateway = Column(String)
    transaction_id = Column(String)
    amount = Column(Float)
    payment_status = Column(String)
    payment_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    donation = relationship("Donation", back_populates="payment")

# ── Notifications Table ────────────────────────────
class Notification(Base):
    __tablename__ = "notifications"

    notification_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    message = Column(String, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="notifications")

# ── Messages Table ─────────────────────────────────
class Message(Base):
    __tablename__ = "messages"

    message_id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.user_id"))
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    sender = relationship("User", back_populates="sent_messages")