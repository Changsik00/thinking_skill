import os
from typing import Dict, List, Optional

import yaml

from app.domain.entities.persona import Persona
from app.domain.repositories.persona_repository import PersonaRepository


class FilePersonaRepository(PersonaRepository):
    """
    Implementation of PersonaRepository that loads personas from a YAML file.
    """

    def __init__(self, config_path: str = "configs/personas.yaml"):
        self.config_path = config_path
        self._personas: Dict[str, Persona] = {}
        self._load_personas()

    def _load_personas(self):
        """
        Loads personas from the YAML configuration file.
        """
        if not os.path.exists(self.config_path):
            # Fallback or empty if file doesn't exist (though it should)
            print(f"Warning: Persona config not found at {self.config_path}")
            return

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)

            if not data or "personas" not in data:
                return

            for key, info in data["personas"].items():
                self._personas[key] = Persona(
                    key=key,
                    name=info.get("name", key),
                    display_name=info.get("display_name", key),
                    system_prompt=info.get("system_prompt", ""),
                )
        except Exception as e:
            print(f"Error loading personas: {e}")

    def get_persona(self, key: str) -> Optional[Persona]:
        return self._personas.get(key)

    def list_personas(self) -> List[Persona]:
        return list(self._personas.values())
