# AI Operations Assistant

## Overview

This project is an **AI Operations Assistant** developed for the GenAI Intern assignment at TrulyMadly.  
The system accepts a natural-language task, plans the required steps, executes real API calls, verifies the results, and returns a clean, user-focused response.

The implementation focuses on **agent-based reasoning**, **tool orchestration**, and **reliability**, while remaining simple to run and easy to evaluate locally.

---

## Core Capabilities

- Multi-agent architecture (Planner, Executor, Verifier)
- Structured task planning (no monolithic prompts)
- Integration with real third-party APIs
- Global weather support (any city in the world)
- Dynamic, topic-based news retrieval
- End-to-end execution with a clean UI
- No hard-coded responses

---

## Architecture

The system is divided into three agents, each with a clear responsibility:

### Planner Agent
- Interprets the user’s natural-language task
- Extracts intent (weather, news, context)
- Produces a **structured plan** describing which tools to call and with what inputs

### Executor Agent
- Executes the planner’s steps sequentially
- Calls external APIs through dedicated tools
- Collects raw results from each API

### Verifier Agent
- Validates execution results
- Handles missing or partial data gracefully
- Formats the final output so that only user-relevant information is returned

This separation ensures clarity, testability, and easy extensibility.

---

## Integrated APIs

This project integrates **three real third-party APIs**, all free to use and requiring no API keys:

1. **Open-Meteo API**
   - Global geocoding (city → latitude/longitude)
   - Current weather data for any city worldwide

2. **Hacker News Algolia API**
   - Dynamic, topic-based news retrieval
   - Topics such as AI, technology, startups

3. **Wikipedia REST API**
   - Short contextual summaries for cities or topics
   - Used when available, with graceful fallback

---

## Project Structure
```
ai_ops_assistant/
├── agents/
│   ├── planner.py
│   ├── executor.py
│   └── verifier.py
├── tools/
│   ├── weather_tool.py
│   ├── news_tool.py
│   └── wiki_tool.py
├── llm/
│   └── llm_client.py
├── templates/
│   └── index.html
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

## Setup Instructions (Local)
### Prerequisites

- Python 3.9+
- pip

 ### Install Dependencies
```
pip install -r requirements.txt
```
### Run the Project
```
uvicorn main:app --reload
```


### Open in browser:

```
http://127.0.0.1:8000/
```

The application runs locally using a single command, as required.

### Environment Variables

No environment variables are required.

A .env.example file is included for completeness and future extensibility:
```

# No API keys required
```

### Example Prompts

Use the following prompts to test the system:

- Get weather in Paris and AI news

- Get weather in Hyderabad and startup news

- Get weather in New York

- Get weather in Tokyo and tech news

- Get weather in Assam

## Output Behavior

- Weather is returned for the requested city (global support)

- News results vary based on the topic specified in the task

- Wikipedia summaries are shown when available

- Internal plans, debug data, and raw JSON are not exposed in the UI

## Known Limitations / Tradeoffs

- News results may appear similar when the same topic (e.g., AI) is requested repeatedly

- Wikipedia summaries depend on availability and may not always be returned

- Planner uses lightweight rule-based intent extraction instead of a paid LLM to keep the project free and easy to run locally

- Tool execution is sequential and not parallelized

- These tradeoffs were chosen to prioritize clarity, reliability, and ease of evaluation.

## Running the Project
```
uvicorn main:app --reload
```
## Notes

- This submission satisfies all mandatory requirements:

- Multi-agent design

- Structured planning and tool usage

- Integration with real third-party APIs

- Complete end-to-end execution

- No hard-coded responses

**Thank you for reviewing this submission.**