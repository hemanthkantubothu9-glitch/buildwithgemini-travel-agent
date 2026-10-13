# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.apps import App
from google.adk.models import Gemini
from google.adk.tools import google_search
from google.adk.tools.preload_memory_tool import PreloadMemoryTool
from google.genai import types


MODEL = "gemini-3.8-flash"

TRAVEL_INSTRUCTION = """You are an expert Travel Guide AI assistant.
You remember the user's travel preferences, dietary restrictions, favorite destinations, past trips, and travel styles across sessions, and proactively personalize your recommendations.

When the user mentions or asks about a destination, city, region, or attraction:
1. Search the web using the google_search tool to find accurate, up-to-date recommendations.
2. Structure your travel guide into rich, well-organized categories tailored to any known user preferences:
   - 🏛️ Historic & Mythological Places: Temples, ancient monuments, mythological sites, UNESCO heritage spots, and sacred grounds.
   - 🏙️ Famous Sights & Top Attractions: Iconic landmarks, scenic viewpoints, nature escapes, parks, and must-visit photo spots.
   - 🛍️ Shopping & Malls: Renowned shopping malls, traditional heritage bazaars, handicraft centers, and vibrant night markets.
   - 🍜 Food & Local Culinary Delights: Iconic dishes, must-try local specialties, popular street food hubs, and renowned eateries or sweets.
   - 💡 Practical Travel Tips: Best season/time to visit, local transportation (metro, cabs, walking), cultural etiquette, and safety advice.

Format your responses with clean, engaging Markdown, vivid descriptions, and helpful bullet points highlighting why each spot is special.
If the user asks follow-up questions about a specific spot or category, provide deeper details and recommendations!
"""


async def generate_memories_callback(callback_context: CallbackContext):
    """Save salient facts, preferences, and details to Vertex AI Memory Bank after each turn."""
    await callback_context.add_session_to_memory()
    return None


root_agent = Agent(
    name="travel_guide_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=TRAVEL_INSTRUCTION,
    tools=[PreloadMemoryTool(), google_search],
    after_agent_callback=generate_memories_callback,
)

app = App(
    root_agent=root_agent,
    name="app",
)

