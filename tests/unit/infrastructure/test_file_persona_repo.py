import os
import tempfile

import pytest
import yaml

from app.infrastructure.storage.file_persona_repository import FilePersonaRepository


@pytest.fixture
def temp_config_file():
    # Create a temporary config file
    data = {
        "personas": {
            "test_persona": {
                "name": "tester",
                "display_name": "TeSter",
                "system_prompt": "You are a test agent.",
            }
        }
    }

    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".yaml") as f:
        yaml.dump(data, f)
        path = f.name

    yield path

    # Cleanup
    if os.path.exists(path):
        os.remove(path)


def test_load_personas(temp_config_file):
    repo = FilePersonaRepository(config_path=temp_config_file)
    personas = repo.list_personas()

    assert len(personas) == 1
    assert personas[0].key == "test_persona"
    assert personas[0].name == "tester"
    assert personas[0].display_name == "TeSter"
    assert personas[0].system_prompt == "You are a test agent."


def test_get_persona(temp_config_file):
    repo = FilePersonaRepository(config_path=temp_config_file)

    persona = repo.get_persona("test_persona")
    assert persona is not None
    assert persona.system_prompt == "You are a test agent."

    missing = repo.get_persona("non_existent")
    assert missing is None


def test_missing_file_handled_gracefully():
    repo = FilePersonaRepository(config_path="non_existent.yaml")
    assert repo.list_personas() == []
