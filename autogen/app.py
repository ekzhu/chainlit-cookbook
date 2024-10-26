from typing import cast
import chainlit as cl
from autogen_ext.models import OpenAIChatCompletionClient
from autogen_agentchat.agents import CodingAssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat, MaxMessageTermination

@cl.on_chat_start
async def start_chat():
    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    agent = CodingAssistantAgent(name="coding_assistant", model_client=model_client)
    team = RoundRobinGroupChat([agent])
    cl.user_session.set("team", team)

@cl.on_message
async def on_user_message(message: cl.Message):
    team = cast(RoundRobinGroupChat, cl.user_session.get("team")) # type: RoundRobinGroupChat

    result = await team.run(message.content, termination_condition=MaxMessageTermination(1))

    response = "\n".join([str(msg.content) for msg in result.messages[1:]])

    # Send a response back to the user
    await cl.Message(
        content=response,
    ).send()
