from src.config import BackendConfig
from src.services.command_history import save_command, update_command_status
from src.mqtt.mqtt_publisher import publish_payload
from src.services.tag_service import get_tag


def publish_command(payload: dict) -> int | None:
    config = BackendConfig()

    tag = get_tag(payload["tagId"])

    if tag is None:
        print(
            f"Unknown tagId: {payload['tagId']}. "
            "Payload was not published."
        )
        return None

    if tag["status"] != "available":
        print(
            f"Unavailable tagId: {payload['tagId']}. "
            "payload was not published."
        )
        return None

    command_id = save_command(payload)
    payload["commandId"] = command_id

    publish_payload(config, payload)
    update_command_status(command_id, "published")

    return command_id
