from dataclasses import dataclass


@dataclass
class Persona:
    """
    Defines the personality and behavior instructions for an Agent.
    """

    key: str  # Unique key (e.g., 'creative', 'critical')
    name: str  # Internal name (e.g., 'creative_diverger')
    display_name: str  # User-friendly name (e.g., '창의적 발산가')
    system_prompt: str  # The actual system prompt for the LLM
