from datetime import date
from uuid import uuid4
from ai_service import GenAIService

class CertificateAgent:
    """Agentic workflow coordinating certificate-generation tasks."""

    def __init__(self):
        self.ai = GenAIService()

    def validate(self, data):
        required = ["recipient", "achievement", "event", "date"]
        missing = [field for field in required if not str(data.get(field, "")).strip()]
        if missing:
            return False, f"Missing fields: {', '.join(missing)}"
        return True, ""

    def run(self, data):
        valid, error = self.validate(data)
        if not valid:
            return {"success": False, "error": error}

        recipient = data["recipient"].strip()
        achievement = data["achievement"].strip()
        event = data["event"].strip()
        issued_date = data["date"].strip()

        certificate = {
            "certificate_id": "CERT-" + uuid4().hex[:10].upper(),
            "recipient": recipient,
            "achievement": achievement,
            "event": event,
            "date": issued_date or date.today().isoformat(),
            "message": self.ai.generate_message(recipient, achievement, event),
            "template": self.ai.choose_template(achievement)
        }
        return {"success": True, "certificate": certificate}
