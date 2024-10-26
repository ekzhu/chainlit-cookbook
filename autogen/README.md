---
title: 'AutoGen with Chainlit'
tags: ['autogen', 'chainlit']
---

# AutoGen with Chainlit

This repository demonstrates the integration of [AutoGen](https://microsoft.github.io/autogen/) with Chainlit to create an interactive chat application that can execute code and perform tasks such as plotting a chart of stock price changes and saving it to disk.

## Quickstart

Follow these steps to get started with AutoGen and Chainlit:

### Setup

1. (Optional) Create and activate a Python virtual environment:

```shell
python3 -m venv venv
source venv/bin/activate
```

2. Install the required dependencies:

```shell
pip install chainlit autogen-agentchat==0.4.0.dev2 'autogen-ext[openai]==0.4.0.dev2'
```

3. Copy the `.env.sample` file to a new `.env` file and replace the `OPENAI_API_KEY` value with your own OpenAI API key.
4. Run the Chainlit app:

## Running the Application

To start the application, use the following command:

```shell
chainlit run app.py -w
```

This will initiate a chat session where the user can interact with the assistant agent to perform tasks such as generating a plot for NVDA stock price change YTD.
