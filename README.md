# LLM Zoomcamp: My Build-Along

This is my public, in-progress build-along of [DataTalks.Club's LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp), a free 10-week course on building production LLM applications (RAG, vector search, agents, evaluation, monitoring).

## What's inside

| Folder | Contents |
|---|---|
| `setup/` | Requirements and a Gemini connection test |
| `01-agentic-rag/` | RAG and agent notebooks, helper code, ingestion |
| `02-vector-search/` | Vector search notebooks, including a pgvector version |
| `03-orchestration/` | Docker setup and six Kestra flows (chat, RAG, RAG with web search, simple agent, web research agent, multi-agent research) |
| `04-Evaluation/` | Ground-truth generation, retrieval evaluation, RAG evaluation, LLM-as-judge |

## Results (evaluation module)

**Retrieval.** 590 LLM-generated test questions over 118 FAQ documents. Top-5 keyword search, scored by hit rate (right document in the top 5) and MRR (how high it ranks).

| Search setting | Hit rate | MRR |
|---|---|---|
| Baseline (question boost 3.0, section boost 0.5) | 0.641 | 0.489 |
| Best single boost value (0.5) | 0.768 | 0.609 |
| Best grid-search weights (36 combinations) | about 0.827 | about 0.663 |

My numbers are lower than the course's reference notebook (hit rate about 0.975, MRR about 0.885) even with identical code. Likely causes:

1. **A larger index:** 118 documents vs 79, so more near-matches compete for the 5 returned slots.
2. **A different model wrote the test questions.** I used `gemini-3.1-flash-lite`, a lightweight Gemini model; the course reference used `gpt-5.4-mini`. Since the search is keyword-based, how closely a generated question's wording overlaps the FAQ text affects hit rate and MRR, and different models paraphrase differently.

I haven't tested either explanation by re-running on the reference data, and I can't say the Gemini model is weaker, only that it is different. Details are in `04-Evaluation/code/02-search-eval.ipynb`.

**Generation.** The RAG prompt tells the model to answer only from the retrieved context and otherwise reply "I don't know based on the provided context." An LLM judge (structured output, good/bad with reasoning) scored 150 of the answers: **105 good, 45 bad**. Failures I reviewed included over-refusals (answering "I don't know" when the context had the answer) and answers that added details the source did not state. I used `gemini-3.1-flash-lite` for answering and judging (the reference used `gpt-5.4-mini`), so these generation results shouldn't be compared directly with the course's numbers either.

**Limitations.** I tuned the search weights on the same questions I scored them on, so the tuned numbers are probably optimistic. The test questions are LLM paraphrases of the FAQ, which may not match how real users ask. The same model family generated the answers and judged them, which can bias the scores. A held-out set would be the next step.

## How it differs from the official course repo

- **Gemini instead of OpenAI.** I use Google's Gemini models and the `google-genai` client. This keeps the whole project on one provider and matches the API access I already have.
- **Local WSL2 Ubuntu instead of GitHub Codespaces.** Running on my own machine gives me more control over Python, Docker, databases and system packages, and makes the environment easier to reproduce and debug.

The course content is the reference point, but the implementation is adapted to my tools and the way I prefer to learn.
