"""Configuration settings for the Ultimate Research Agent."""

# LLM Configuration
MODEL_NAME = "gemini-2.5-flash"
TEMPERATURE = 0.3

# --- Multi-model settings (used by llm.py) ---
GEMINI_MODEL = "gemini-2.5-flash"
GROQ_MODEL = "llama-3.3-70b-versatile"
MISTRAL_MODEL = "mistral-large-latest"
MODEL_TEMPERATURE = 0.3
# Allowed values: "gemini", "mistral", "groq"
DEFAULT_MODEL = "gemini"


class Config:
    """Central configuration for the research agent pipeline."""

    def __init__(self):
        # Model configuration
        self.model_name = MODEL_NAME
        self.temperature = TEMPERATURE
        self.max_tokens = 4096

        # Search configuration
        self.search_engine = "tavily"
        self.max_search_results = 10
        self.search_timeout = 30

        # Pipeline configuration
        self.max_planning_iterations = 3
        self.enable_analyst = True

        # Logging configuration
        self.log_level = "INFO"
        self.log_file = "research_agent.log"