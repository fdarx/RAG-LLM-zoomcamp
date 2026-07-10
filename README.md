# LLM Zoomcamp — My Journey
 
This is my public, in-progress build-along of [DataTalks.Club's LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) — a free 10-week course on building production LLM applications (RAG, vector search, agents, evaluation, monitoring).

## How My Differs From The Official Course Repo

This repository follows the same course structure as the official [DataTalksClub/llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) materials, but I made a few intentional changes to match my own setup and the stack I wanted to practice with.

- Gemini instead of OpenAI: I use Google's Gemini models and the `google-genai` client in my notebooks and helpers. This keeps the whole project on one provider, matches the API access I already have, and lets me focus on the course concepts instead of switching between vendors.
- Local WSL2 Ubuntu instead of GitHub Codespaces: I run the project on my own machine inside WSL2 Ubuntu. That gives me more control over Python, Docker, databases, and system packages, and it makes the environment easier for me to reproduce and debug locally.
In short, the course content is the reference point, but the implementation here is adapted to my tools, my environment, and the way I prefer to learn.
