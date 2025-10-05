# utils/validator.py
def validate_alert_data(data: dict) -> bool:
    """
    Minimal validation for the Suricata eve.json alert structure we use.
    Returns True if payload likely contains the expected fields.
    """
    if not isinstance(data, dict):
        return False

    # basic required top-level keys
    required_top = ["timestamp", "src_ip", "dest_ip", "alert"]
    for k in required_top:
        if k not in data:
            return False

    # alert object must contain signature and severity
    alert = data.get("alert", {})
    if not isinstance(alert, dict):
        return False

    if "signature" not in alert or "severity" not in alert:
        return False

    return True