import httpx
from aiogram import types
from bot.utils import get_faq_context

MISTRAL_API_KEY = "QqkMxELY0YVGkCx17Vya04Sq9nGvCahu"
MISTRAL_ENDPOINT = "https://api.mistral.ai/v1/chat/completions"
FAQ_PATH = "UNIME FAQ SCRIPT.xlsx"

faq_context = get_faq_context(FAQ_PATH)

async def handle_faq(message: types.Message):
    user_question = message.text.strip()

    system_prompt = (
        "You are a helpful assistant for university admissions. "
        "Use the following FAQ to answer the user's question:\n\n"
        f"{faq_context}\n\n"
        f"User: {user_question}"
    )

    payload = {
        "model": "open-mistral-nemo",
        "temperature": 0.3,
        "top_p": 1,
        "max_tokens": 500,
        "messages": [
            {"role": "system", "content": system_prompt}
        ],
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                MISTRAL_ENDPOINT,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {MISTRAL_API_KEY}"
                },
                json=payload
            )
            response.raise_for_status()
            data = response.json()
            raw_answer = data["choices"][0]["message"]["content"]

            formatted_answer = (
                f"📌 *Your Question:*\n"
                f"`{user_question}`\n\n"
                f"💬 *Answer:*\n"
                f"{raw_answer.strip()}\n\n"
                f"_🤖 Answered by AI based on official FAQ data_"
            )

            await message.answer(formatted_answer, parse_mode="Markdown")
    except Exception as e:
        await message.answer("❌ Sorry, there was an error fetching the answer.")
        print(f"Mistral error: {e}")
