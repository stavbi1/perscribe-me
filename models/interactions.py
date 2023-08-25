from pydantic import BaseModel
from typing import Dict, List


class Interactions(BaseModel):
    interaction_pairs: Dict[str, List[str]] = {}
