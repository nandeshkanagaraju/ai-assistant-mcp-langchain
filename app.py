import asyncio
from mcp_use import MCPAgent, MCPClient
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

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
        past = "\n".join([f"{m.type}: {m.content}" for m in memory.messages])
        prompt = f"{past}\nUser: {query}" if past else f"User: {query}"
        result = await agent.run(prompt)
        memory.add_user_message(query)
        memory.add_ai_message(result)
        return result

    print(Fore.GREEN + "🟢 Chat started! Type 'exit' to quit.\n")
    print(Fore.GREEN + "="*60)

    # Message counter
    msg_count = 1

    # Interactive chat loop
    while True:
        user_input = input(Fore.CYAN + f"[{msg_count}] You: " + Style.RESET_ALL).strip()
        if user_input.lower() in ("exit", "quit"):
            print(Fore.GREEN + "\nExiting chat. Goodbye!")
            break

        response = await run_with_memory(user_input)

        # Formatted output
        print(Fore.YELLOW + "-"*60)
        print(Fore.YELLOW + f"[{msg_count}] Assistant: " + Style.RESET_ALL + response)
        print(Fore.YELLOW + "-"*60 + "\n")

        msg_count += 1

    # Clean up
    await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(main())
