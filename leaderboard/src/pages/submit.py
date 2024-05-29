from src.display.utils import EVAL_COLS, EVAL_TYPES, ModelType
from src.envs import EVAL_REQUESTS_PATH
from src.populate import get_evaluation_queue_df
from src.about import EVALUATION_QUEUE_TEXT
from src.submission.submit import add_new_eval
import gradio as gr

def show_submit_page():
    (
        finished_eval_queue_df,
        running_eval_queue_df,
        pending_eval_queue_df,
    ) = get_evaluation_queue_df(EVAL_REQUESTS_PATH, EVAL_COLS)
    with gr.TabItem("🚀 Submit here! ", elem_id="llm-benchmark-tab-table", id=3):
        with gr.Column():
            with gr.Row():
                gr.Markdown(EVALUATION_QUEUE_TEXT, elem_classes="markdown-text")

            with gr.Column():
                with gr.Accordion(
                    f"✅ Finished Evaluations ({len(finished_eval_queue_df)})",
                    open=False,
                ):
                    with gr.Row():
                        finished_eval_table = gr.components.Dataframe(
                            value=finished_eval_queue_df,
                            headers=EVAL_COLS,
                            datatype=EVAL_TYPES,
                            row_count=5,
                        )

                with gr.Accordion(
                    f"⏳ Pending Evaluation Queue ({len(pending_eval_queue_df)})",
                    open=False,
                ):
                    with gr.Row():
                        pending_eval_table = gr.components.Dataframe(
                            value=pending_eval_queue_df,
                            headers=EVAL_COLS,
                            datatype=EVAL_TYPES,
                            row_count=5,
                        )
        with gr.Row():
            gr.Markdown("# ✉️✨ Submit your model here!", elem_classes="markdown-text")

        with gr.Row():
            with gr.Column():
                model_name_textbox = gr.Textbox(label="Model name")

        submit_button = gr.Button("Submit Eval")
        submission_result = gr.Markdown()
        submit_button.click(
            add_new_eval,
            [
                model_name_textbox,
            ],
            submission_result,
        )