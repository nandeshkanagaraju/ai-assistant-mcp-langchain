# AI Assistant MCP

An interactive AI chat assistant built using **MCPAgent** with **LangChain**, **OpenAI GPT-4**, and **conversation memory**.  
This assistant can answer queries, remember previous messages, and provide structured responses, including formatted outputs with colored terminal messages.

---

## Features

- **Interactive Chat**: Chat with the assistant in a terminal session.
- **Memory-Enabled**: Remembers previous queries and responses for contextual conversations.
- **Formatted Output**: Clean, readable terminal outputs with separators and numbering.
- **Colored Output**: Uses `colorama` to distinguish user messages, assistant messages, and system info.
- **Tool Restrictions**: Disables potentially unsafe tools (`file_system`, `network`) for safe execution.
- **Search & Recommendation Tools**: Can use MCP-enabled tools like search to find restaurants, hotels, etc.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/nandeshkanagaraju/ai-assistant-mcp.git
cd ai-assistant-mcp
```

2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
# Install colorama if not included
pip install colorama
```

4. Ensure you have your `browser_mcp.json` configuration file ready for MCPClient.

---

## Usage

Run the assistant using:

```bash
python3 app.py
```

### Chat Commands

- Type your query and press Enter.
- The assistant remembers previous messages.
- Type `exit` or `quit` to end the session.

### Example Interaction

```
🟢 Chat started! Type 'exit' to quit.
============================================================
[1] You: hi
------------------------------------------------------------
[1] Assistant: Hi! How can I assist you today?
------------------------------------------------------------
[2] You: Suggest hotels near Hosur Bus Stand
------------------------------------------------------------
[2] Assistant: Here are some options for hotels near the Hosur bus stand:
1. [Makemytrip Hotels](https://www.makemytrip.com/hotels/hosur-hotels.html) – with restaurant, 24-hour room service.
2. [Yatra Hotels](https://www.yatra.com/hotels/hotels-near-hosur-bus-stand-with-parking-in-hosur) – with parking and discounts.
...
------------------------------------------------------------
```

---

## File Structure

```
ai-assistant-mcp/
├── app.py                  # Main chat script
├── browser_mcp.json        # MCP client configuration
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── venv/                   # Virtual environment (optional)
```

---

## Notes

- Uses **langchain-community** `ChatMessageHistory` for conversation memory.
- MCPAgent can integrate with multiple tools for search, booking, and browsing.
- To avoid internal MCP logs cluttering the chat, logs can be disabled or redirected.

---

## License

MIT License © Nandesh Kanagaraju

