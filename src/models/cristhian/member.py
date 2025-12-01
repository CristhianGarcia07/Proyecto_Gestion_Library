from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class Member(BaseModel):
    member_id: int = Field(..., description="Unique identifier for each library member")
    first_name: str = Field(..., min_length=1, max_length=50, description="Member's first name")
    last_name: str = Field(..., min_length=1, max_length=50, description="Member's last name")
    email: str = Field(..., description="Member's email address")
    phone: Optional[str] = Field(None, description="Member's phone number")
    membership_date: date = Field(..., description="Date the member joined the library")
    is_active: bool = Field(default=True, description="Member activity status (active or inactive)")

