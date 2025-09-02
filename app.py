import asyncio
from mcp_use import MCPAgent, MCPClient
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory

async def main():
    # Initialize MCP client
    client = MCPClient.from_config_file("browser_mcp.json")

    # Initialize memory
    memory = ChatMessageHistory()

    # Initialize LLM
    llm = ChatOpenAI(model="gpt-4")

    # Initialize agent with memory
    agent = MCPAgent(
        llm=llm,
        client=client,
        disallowed_tools=["file_system", "network"]
    )

    # Function to run query with memory
    async def run_with_memory(query):
        # Prepend memory history to input
        past = "\n".join([f"{m.type}: {m.content}" for m in memory.messages])
        prompt = f"{past}\nUser: {query}" if past else f"User: {query}"
        result = await agent.run(prompt)
        # Save both user input and agent response
        memory.add_user_message(query)
        memory.add_ai_message(result)
        return result

    # Queries
    result1 = await run_with_memory("Find the best restaurant in San Francisco")
    print("Query 1 result:", result1)

    result2 = await run_with_memory("Based on my previous query, suggest a good Italian place nearby")
    print("Query 2 result (with memory):", result2)

    # Clean up
    await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(main())
