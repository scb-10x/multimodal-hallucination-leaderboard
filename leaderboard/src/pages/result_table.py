import gradio as gr
import pandas as pd
from src.envs import EVAL_RESULTS_PATH
from src.populate import get_leaderboard_df
from src.display.utils import (
    AutoEvalColumn,
)

def update_table(
    hidden_df: pd.DataFrame,
    query: str,
):
    filtered_df = filter_queries(query, hidden_df)
    return filtered_df


def search_table(df: pd.DataFrame, query: str) -> pd.DataFrame:
    return df[(df[AutoEvalColumn.model.name].str.contains(query, case=False))]


def filter_queries(query: str, filtered_df: pd.DataFrame) -> pd.DataFrame:
    final_df = []
    if query != "":
        queries = [q.strip() for q in query.split(";")]
        for _q in queries:
            _q = _q.strip()
            if _q != "":
                temp_filtered_df = search_table(filtered_df, _q)
                if len(temp_filtered_df) > 0:
                    final_df.append(temp_filtered_df)
        if len(final_df) > 0:
            filtered_df = pd.concat(final_df)
            filtered_df = filtered_df.drop_duplicates(
                subset=[AutoEvalColumn.model.name, ]
            )

    return filtered_df



def show_result_page(root_path: str, title: str, index: int):
    raw_data, original_df = get_leaderboard_df(EVAL_RESULTS_PATH + f'/{root_path}')
    leaderboard_df = original_df.copy()
    number_of_field = list(leaderboard_df.keys())
    with gr.TabItem(title, elem_id="llm-benchmark-tab-table", id=index):
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    search_bar = gr.Textbox(
                        placeholder=" 🔍 Search for your model (separate multiple queries with `;`) and press ENTER...",
                        show_label=False,
                        elem_id="search-bar",
                    )

        
        leaderboard_table = gr.components.Dataframe(
            value=leaderboard_df,
            headers=list(leaderboard_df.keys()),
            datatype=['markdown'],
            elem_id="leaderboard-table",
            column_widths=(['20%'] if len(number_of_field) > 6 else [str((1.5 / (len(number_of_field))) * 100) + '%']) * len(number_of_field),
            min_width=180,
            interactive=False,
            visible=True,
            wrap=True
        )
        

        # Dummy leaderboard for handling the case when the user uses backspace key
        hidden_leaderboard_table = gr.components.Dataframe(
            value=original_df,
            headers=list(original_df.keys()),
            interactive=False,
            visible=False,
        )

        search_bar.submit(
            update_table,
            [
                hidden_leaderboard_table,
                search_bar,
            ],
            leaderboard_table,
        )