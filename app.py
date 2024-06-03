import subprocess
import gradio as gr
from apscheduler.schedulers.background import BackgroundScheduler
from huggingface_hub import snapshot_download

from src.pages.about import show_about_page
from src.pages.submit import show_submit_page
from src.pages.result_table import show_result_page
from src.about import (
    CITATION_BUTTON_LABEL,
    CITATION_BUTTON_TEXT,
    INTRODUCTION_TEXT,
    TITLE,
)
from src.display.css_html_js import custom_css
from src.envs import API, EVAL_REQUESTS_PATH, EVAL_RESULTS_PATH, QUEUE_REPO, REPO_ID, RESULTS_REPO, TOKEN



def restart_space():
    API.restart_space(repo_id=REPO_ID)

try:
    print(EVAL_REQUESTS_PATH)
    snapshot_download(
        repo_id=QUEUE_REPO, local_dir=EVAL_REQUESTS_PATH, repo_type="dataset", tqdm_class=None, etag_timeout=30, token=TOKEN
    )
except Exception:
    restart_space()
try:
    print(EVAL_RESULTS_PATH)
    snapshot_download(
        repo_id=RESULTS_REPO, local_dir=EVAL_RESULTS_PATH, repo_type="dataset", tqdm_class=None, etag_timeout=30, token=TOKEN
    )
except Exception:
    restart_space()


demo = gr.Blocks(css=custom_css)
with demo:
    gr.HTML(TITLE)
    gr.Markdown(INTRODUCTION_TEXT, elem_classes="markdown-text")

    with gr.Tabs(elem_classes="tab-buttons") as tabs:
        show_result_page(root_path='VH', title='🎆 Visual Hallucination Benchmark', index=0)
        show_result_page(root_path='AVH-visual', title='📺 AVHalluBench Visual', index=1)
        show_result_page(root_path='AVH-audio', title='🔈 AVHalluBench Audio', index=2)
        show_about_page(index=3)
        show_submit_page(index=4)

    with gr.Row():
        with gr.Accordion("📙 Citation", open=False):
            citation_button = gr.Textbox(
                value=CITATION_BUTTON_TEXT,
                label=CITATION_BUTTON_LABEL,
                lines=8,
                elem_id="citation-button",
                show_copy_button=True,
            )

scheduler = BackgroundScheduler()
scheduler.add_job(restart_space, "interval", seconds=1800)
scheduler.start()
demo.queue(default_concurrency_limit=40).launch()