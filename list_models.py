#!/usr/bin/env python3
from util import *
from openai import OpenAI


if __name__ == '__main__':
    client = OpenAI(
        api_key=RUNPOD_API_KEY,
        base_url=f'https://api.runpod.ai/v2/{RUNPOD_ENDPOINT_ID}/openai/v1',
    )

    timer = Timer()
    response = client.models.list()
    total_time = timer.get_elapsed_time()

    for model in response:
        print(model.id)

    print('-----')
    print(f'Time taken: {total_time} seconds')
