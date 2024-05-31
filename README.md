#### Setup

1. Setup ssh-key in huggingface website
2. create new "results" and "requests" with dataset type repo on huggingface. (if name different, need to change on leaderboard envs.py) - make it public
3. Setup git repo on "results";
    - git init
    - git add .
    - git commit -m "init commit"
    - git remote add origin git@hf.co:datasets/????/results
    - git push origin main --force
4. create new "leaderboard" with spaces type repo on huggingface. With this config; Gradio; Blank; CPU basic - Free; Public.
5. Setup git repo on "leaderboard";
    - git init
    - git add .
    - git commit -m "init commit"
    - git remote add origin git@hf.co:spaces/????/leaderboard
    - git push origin main --force
6. Verified if the it's all worked.
7. Edit leaderboard/src/envs.py and another files to customized the leaderboard.
8. cd leaderboard && pip install -r requirements.txt
9. python app.py # to start server

#### Debug / Develop
```
cd leaderboard
gradio app.py # to auto reload
python app.py # to start app
```

#### Basic result file for each model

```
{
    "config": {
        "model_dtype": "torch.float16", # or torch.bfloat16 or 8bit or 4bit
        "model_name": "path of the model on the hub: org/model",
        "model_sha": "revision on the hub",
    },
    "results": {
        "task_name": {
            "metric_name": score,
        },
        "task_name2": {
            "metric_name": score,
        }
    }
}
```