#!/usr/bin/env python3
from util import *
from openai import OpenAI


if __name__ == '__main__':
    client = OpenAI(
        api_key=RUNPOD_API_KEY,
        base_url=f'https://api.runpod.ai/v2/{RUNPOD_ENDPOINT_ID}/openai/v1',
    )

    # Create a chat completion
    timer = Timer()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": "How do I make bread?"
            }
        ],
        temperature=0,
        max_tokens=2000
    )
    total_time = timer.get_elapsed_time()

    # Print the response
    print(response.choices[0].message.content)
    print('-----')
    print(f'Time taken: {total_time} seconds')
    print(f'Completion tokens: {response.usage.completion_tokens}')
    print(f'Prompt tokens: {response.usage.prompt_tokens}')
    print(f'Total tokens: {response.usage.total_tokens}')
