from ollama import chat


def ask_jarvis(text):
    response = chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are JARVIS, a personal AI assistant running locally "
                    "on the user's computer. Your name is JARVIS. "
                    "Do not say that you are Qwen or that you are not JARVIS. "
                    "Respond naturally as JARVIS. "
                    "Be helpful, concise, and conversational."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response["message"]["content"]