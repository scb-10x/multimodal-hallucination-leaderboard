import os
from dotenv import load_dotenv
load_dotenv()
from huggingface_hub import HfApi

# Info to change for your repository
# ----------------------------------
TOKEN = os.environ.get("TOKEN") # A read/write token for your org

OWNER = "scb10x" # Change to your org - don't forget to create a results and request dataset, with the correct format!
# ----------------------------------

REPO_ID = f"{OWNER}/multimodal-hallucination-leaderboard"
QUEUE_REPO = f"{OWNER}/multimodal_hallucination_requests"
RESULTS_REPO = f"{OWNER}/multimodal_hallucination_results"

# If you setup a cache later, just change HF_HOME
CACHE_PATH=os.getenv("HF_HOME", ".")

# Local caches
EVAL_REQUESTS_PATH = os.path.join(CACHE_PATH, "eval-queue")
EVAL_RESULTS_PATH = os.path.join(CACHE_PATH, "eval-results")
EVAL_REQUESTS_PATH_BACKEND = os.path.join(CACHE_PATH, "eval-queue-bk")
EVAL_RESULTS_PATH_BACKEND = os.path.join(CACHE_PATH, "eval-results-bk")

API = HfApi(token=TOKEN)
