import glob
import json
import os
from dataclasses import dataclass

import dateutil

from src.display.formatting import model_hyperlink
from src.display.utils import AutoEvalColumn


@dataclass
class EvalResult:
    """Represents one full evaluation. Built from a combination of the result and request file for a given run.
    """
    eval_name: str # org_model (uid) 
    full_model: str # org/model (path on hub)
    org: str 
    model: str
    results: dict
    model_link: str = ""
    date: str = "" # submission date of request file

    @classmethod
    def init_from_json_file(self, json_filepath):
        """Inits the result from the specific model result file"""
        with open(json_filepath) as fp:
            data = json.load(fp)

        config = data.get("config")


        # Get model and org
        org_and_model = config.get("model_name", config.get("model_args", None))
        org_and_model = org_and_model.split("/", 1)

        if len(org_and_model) == 1:
            org = None
            model = org_and_model[0]
            result_key = f"{model}"
        else:
            org = org_and_model[0]
            model = org_and_model[1]
            result_key = f"{org}_{model}"
        full_model = "/".join(org_and_model)
        model_link = config.get('model_link', '')

        # Extract results available in this file (some results are split in several files)
        results = {}

        for k, v in data["results"].items():
            results[k] = v[k]
        print('results', results)
        return self(
            eval_name=result_key,
            full_model=full_model,
            model_link=model_link,
            org=org,
            model=model,
            results=results,
        )

    def update_with_request_file(self, requests_path):
        """Finds the relevant request file for the current model and updates info with it"""
        request_file = get_request_file_for_model(requests_path, self.full_model)

        try:
            with open(request_file, "r") as f:
                request = json.load(f)
            self.date = request.get("submitted_time", "")
        except Exception:
            print(f"Could not find request file for {self.org}/{self.model}")

    def to_dict(self):
        """Converts the Eval Result to a dict compatible with our dataframe display"""
        data_dict = {
            AutoEvalColumn.model.name: model_hyperlink(self.model_link, self.full_model),
        }

        for key in self.results.keys():
            data_dict[key] = self.results[key]

        return data_dict


def get_request_file_for_model(requests_path, model_name):
    """Selects the correct request file for a given model. Only keeps runs tagged as FINISHED"""
    request_files = os.path.join(
        requests_path,
        f"{model_name}_eval_request_*.json",
    )
    request_files = glob.glob(request_files)

    request_file = ""
    request_files = sorted(request_files, reverse=True)
    for tmp_request_file in request_files:
        with open(tmp_request_file, "r") as f:
            req_content = json.load(f)
            if (
                req_content["status"] in ["FINISHED"]
            ):
                request_file = tmp_request_file
    return request_file


def get_raw_eval_results(results_path: str) -> list[EvalResult]:
    """From the path of the results folder root, extract all needed info for results"""
    model_result_filepaths = []

    for root, _, files in os.walk(results_path):
        # We should only have json files in model results
        if len(files) == 0 or any([not f.endswith(".json") for f in files]):
            continue

        # Sort the files by date
        try:
            files.sort(key=lambda x: x.removesuffix(".json").removeprefix("results_")[:-7])
        except dateutil.parser._parser.ParserError:
            files = [files[-1]]

        for file in files:
            model_result_filepaths.append(os.path.join(root, file))

    eval_results = {}
    for model_result_filepath in model_result_filepaths:
        # Creation of result
        eval_result = EvalResult.init_from_json_file(model_result_filepath)

        # Store results of same eval together
        eval_name = eval_result.eval_name
        if eval_name in eval_results.keys():
            eval_results[eval_name].results.update({k: v for k, v in eval_result.results.items() if v is not None})
        else:
            eval_results[eval_name] = eval_result

    results = []
    for v in eval_results.values():
        try:
            v.to_dict() # we test if the dict version is complete
            results.append(v)
        except KeyError:  # not all eval values present
            continue
    return results
