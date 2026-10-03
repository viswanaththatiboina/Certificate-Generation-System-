class GenAIService:
    """GenAI abstraction.

    Replace the demo implementation with an LLM provider call when an API
    key and model are configured.
    """

    def generate_message(self, recipient, achievement, event):
        return (
            f"This certificate is proudly presented to {recipient} "
            f"for {achievement} in recognition of outstanding participation "
            f"and achievement in {event}."
        )

    def choose_template(self, achievement):
        text = achievement.lower()
        if any(word in text for word in ("winner", "first", "champion", "gold")):
            return "achievement"
        return "classic"
