#!/usr/bin/env python3
from util import *
from openai import OpenAI


MODEL = 'cognitivecomputations/dolphin-2.9.1-llama-3-8b'


if __name__ == '__main__':
    client = OpenAI(
        api_key=RUNPOD_API_KEY,
        base_url=f'https://api.runpod.ai/v2/{RUNPOD_ENDPOINT_ID}/openai/v1',
    )

    # Create a chat completion
    timer = Timer()
    response_stream = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": "Who was president of the US in 1998?"
            }
        ],
        temperature=0,
        max_tokens=100,
        stream=True
    )

    # Stream the response
    for chunk in response_stream:
        print(chunk.choices[0].delta.content or "", end="", flush=True)

    total_time = timer.get_elapsed_time()

    print()
    print('-----')
    print(f'Time taken: {total_time} seconds')
