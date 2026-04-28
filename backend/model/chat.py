from dotenv import load_dotenv
from openai import OpenAI
from fastmcp import Client
import json
import os
import asyncio


load_dotenv('../.env')
APIKEY = os.environ.get('OPENAI_API_KEY')
llm = OpenAI(api_key=APIKEY)

async def call_mcp(tool_name, args):
    async with Client('http://127.0.0.1:9000/mcp') as client:
        return await client.call_tool(tool_name, args)
# mcp_client = Client('http://127.0.0.1:9000')

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_info_products",
            "description": "Get info product name, harga end user, and stock. Bila stock 0 tetap cantumkan namun beri keterangan (Habis)",
            "parameters": {
                "type": "object",
                "properties": {
                    "products": {
                        "type": "array", 
                        "items":{
                            "type":"string"
                        }
                    }
                },
                "required": ["products"]
            }
        }
    }
]



def chat_with_tools(msg):

    first = llm.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": msg}],
        tools=TOOLS,
        tool_choice="auto"
    )

    
    message = first.choices[0].message

    print("ini output awal: ", message)

    if message.tool_calls:
        tool_messages = []

        for tool in message.tool_calls:
            args = json.loads(tool.function.arguments)

            result = asyncio.run(
                call_mcp(tool.function.name, args)
            )

            print("ini result:", result.content[0].text)

            tool_messages.append({
                "role": "tool",
                "tool_call_id": tool.id,
                "content": result.content[0].text
            })
        
        # print(result.content[0].text)
        print("ini result: ", result.content[0].text)

        final = llm.chat.completions.create(
            model="gpt-4o-mini",
            messages = [
                {"role": "user", "content": msg},
                {
                    "role": "assistant",
                    "content": message.content,
                    "tool_calls": message.tool_calls
                },
                *tool_messages
            ]
        )

        return {
            "answer": final.choices[0].message.content
        }

    return {
        "answer": message.content
    }
