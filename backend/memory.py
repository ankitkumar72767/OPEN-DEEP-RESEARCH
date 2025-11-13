
from typing import Dict, List
from collections import defaultdict
from datetime import datetime

class MemorySaver:
    def __init__(self):
        self.sessions: Dict[str, List[dict]] = defaultdict(list)

    def save(self, session_id: str, payload: dict):
        payload = dict(payload)
        payload["timestamp"] = datetime.utcnow().isoformat()
        self.sessions[session_id].append(payload)

    def load(self, session_id: str) -> List[dict]:
        return self.sessions.get(session_id, [])

    def all_sessions(self) -> Dict[str, List[dict]]:
        return self.sessions
