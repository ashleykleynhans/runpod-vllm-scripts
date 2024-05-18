# OpenAI Compatible API scripts for RunPod vLLM Worker

## Installation

### Create your RunPod Endpoint

You can click on `Serverless vLLM` at the top of the
[Explore Templates](https://www.runpod.io/console/explore)
page on [RunPod](https://runpod.io?ref=2xxro4sy).

Be sure to specify your model name and maximum model
length.  (Refer to the [docs](https://github.com/runpod-workers/worker-vllm)).

### Install these scripts

```bash
git clone https://github.com/ashleykleynhans/runpod-vllm-scripts.git
cd runpod-vllm-scripts
python3 -m venv venv
source venv/bin/activate
```

### Set your RunPod API key, RunPod Endpoint ID and Model

> [!NOTE]
> The `MODEL` is the path to the model on Hugging Face Hub
> and not the full URL.  For example,
> https://huggingface.co/cognitivecomputations/dolphin-2.9.1-llama-3-8b
> would be `cognitivecomputations/dolphin-2.9.1-llama-3-8b`.

1. Copy the file `.env.example` to a new file called `.env`.
2. Edit the `.env` file and set your RunPod API key,
   RunPod Endpoint ID, and model path to the model on
   Hugging Face Hub.
3. Save the file.

## Scripts

| Script Name                   | Description                        |
|-------------------------------|------------------------------------|
| chat_completions.py           | Chat completions WITHOUT streaming |
| chat_completions_streaming.py | Chat completions WITH streaming    |
| completions.py                | Completions WITHOUT streaming      |
| completions_streaming.py      | Completions WITH streaming         |
| list_models.py                | List Available models              |

Once you have installed the scripts and activated the env, you
can run any of the above scripts, for example:

```bash
python3 chat_completions_streaming.py
```

You obviously need to edit the scripts to set your prompt, message,
model, etc.

## Appreciate my work?

<a href="https://www.buymeacoffee.com/ashleyk" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

