# %%
import pandas as pd
import os
import json


def convert_data_vh(input_csv: str, results_path: str):
    df = pd.read_csv(input_csv)
    result_columns = [
        "POPE COCO ↑",
        "CHAIR (s/i) ↓",
        "UniHD ↓",
        "SelfCheckGPT ↓",
        "CrossCheck-explicit ↓",
        "CrossCheck-implicit ↓",
        "Human ↓",
    ]
    keys = list(df.keys())
    results = {}
    for i, row in df.iterrows():
        model_name = row[keys[0]]
        config_results = {
            "model_name": model_name,
            "model_link": row["Model link (optional)"],
        }
        row_results = {}
        for k in result_columns:
            if k == "CHAIR (s/i) ↓":
                vs, vi = row[k].split(", ")
                row_results["CHAIR (s) ↓"] = {"CHAIR (s) ↓": vs}
                row_results["CHAIR (i) ↓"] = {"CHAIR (i) ↓": vi}
            else:
                row_results[k] = {k: row[k]}
        results[model_name] = {"config": config_results, "results": row_results}

    for model_name in results.keys():
        payload = results[model_name]
        dir_path = f"{results_path}/VH/{model_name}"
        os.makedirs(dir_path, exist_ok=True)
        with open(f"{dir_path}/results.json", "w") as w:
            json.dump(payload, w, ensure_ascii=False)


def convert_data_avh_v(input_csv: str, results_path: str):
    df = pd.read_csv(input_csv)
    result_columns = [
        "SelfCheckGPT ↓",
        "CrossCheck-explicit ↓",
        "RefCheck ↓",
    ]

    keys = list(df.keys())
    results = {}
    for i, row in df.iterrows():
        model_name = row[keys[0]]
        config_results = {
            "model_name": model_name,
            "model_link": row["Unnamed: 1"],
        }
        row_results = {}
        for k in result_columns:
            row_results[k] = {k: row[k]}
        results[model_name] = {"config": config_results, "results": row_results}

    for model_name in results.keys():
        payload = results[model_name]
        dir_path = f"{results_path}/AVH-visual/{model_name}"
        os.makedirs(dir_path, exist_ok=True)
        with open(f"{dir_path}/results.json", "w") as w:
            json.dump(payload, w, ensure_ascii=False)


def convert_data_avh_a(input_csv: str, results_path: str):
    df = pd.read_csv(input_csv)
    result_columns = [
        "SelfCheckGPT ↓",
        "CrossCheck-explicit ↓",
        "RefCheck ↓",
    ]

    keys = list(df.keys())
    results = {}
    for i, row in df.iterrows():
        model_name = row[keys[0]]
        config_results = {
            "model_name": model_name,
            "model_link": row["Model Link"],
        }
        row_results = {}
        for k in result_columns:
            row_results[k] = {k: row[k]}
        results[model_name] = {"config": config_results, "results": row_results}

    for model_name in results.keys():
        payload = results[model_name]
        dir_path = f"{results_path}/AVH-audio/{model_name}"
        os.makedirs(dir_path, exist_ok=True)
        with open(f"{dir_path}/results.json", "w") as w:
            json.dump(payload, w, ensure_ascii=False)


if __name__ == "__main__":
    convert_data_avh_v(
        input_csv="/Users/kunato/Desktop/crosscheck-leaderboard/avhallu-visual.csv",
        results_path="/Users/kunato/scb/leaderboard-template/results",
    )
    convert_data_avh_a(
        input_csv="/Users/kunato/Desktop/crosscheck-leaderboard/avhallu-audio.csv",
        results_path="/Users/kunato/scb/leaderboard-template/results",
    )
    convert_data_vh(
        "/Users/kunato/Desktop/crosscheck-leaderboard/img2img-hallucination.csv",
        results_path="/Users/kunato/scb/leaderboard-template/results",
    )
