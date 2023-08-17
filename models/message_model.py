from typing import Dict, Any, Optional
from dataclasses import dataclass, field

@dataclass
class Log():
    user_id : str
    chat_id : str
    message : str
    
@dataclass
class Request():
    request: Dict[Any,Any] = field(default_factory=dict)
    response: Dict[Any,Any] = field(default_factory=dict)
    resolved: bool = False