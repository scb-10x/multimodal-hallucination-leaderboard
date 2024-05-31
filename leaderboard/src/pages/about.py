import gradio as gr

from src.about import LLM_BENCHMARKS_TEXT

def show_about_page(index: int):
    with gr.TabItem("📝 About", elem_id="llm-benchmark-tab-table", id=index):
        gr.Markdown(LLM_BENCHMARKS_TEXT, elem_classes="markdown-text")