from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.persona import Persona

class PersonaRepository(ABC):
    """
    Interface for retrieving Agent Personas.
    """

    @abstractmethod
    def get_persona(self, key: str) -> Optional[Persona]:
        """
        Retrieve a specific persona by its key (e.g., 'creative', 'critical').
        """
        pass

    @abstractmethod
    def list_personas(self) -> List[Persona]:
        """
        List all available personas.
        """
        pass
