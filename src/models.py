from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Event:
    club_id: int
    club_name: str  # solo para logs, no se persiste en BD
    title: str
    date: str  # yyyy-MM-dd
    external_id: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    ticket_url: Optional[str] = None
    tags: list[str] = field(default_factory=list)
    categories: list[int] = field(default_factory=list)
