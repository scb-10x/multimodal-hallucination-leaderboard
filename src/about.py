from dataclasses import dataclass
from enum import Enum



NUM_FEWSHOT = 0 # Change with your few shot
# ---------------------------------------------------

TITLE = """<h1 align="center" id="space-title">🎭 Multimodal Hallucination Leaderboard</h1>"""


# <a href="url"></a>

INTRODUCTION_TEXT = """
<p>The Multimodal Hallucination Leaderboard ranks multimodal large language models based on hallucination levels in various tasks. System rankings for three different input modalities are displayed, covering the audio, image, and video domains. For each task, hallucination levels are measured using various existing hallucination ranking metrics. The leaderboard currently consists of the following benchmarks:</p>
<ul>
      <li><b><a href="https://arxiv.org/abs/2305.10355">POPE</a> / <a href="https://huggingface.co/datasets/openkg/MHaluBench">MHaluBench</a></b>: Both are image-captioning datasets where the task is to generate text given an input image. System Hallucination scores are measured using existing visual hallucination metrics as follows (i) the <a href="https://arxiv.org/abs/2305.10355">POPE</a> method is evaluated on the POPE dataset, and (ii) <a href="https://arxiv.org/abs/1809.02156">CHAIR</a>, <a href="https://arxiv.org/abs/2402.03190">UniHD</a>, <a href="https://arxiv.org/abs/2303.08896">SelfCheckGPT</a>, <a href="https://arxiv.org/abs/2405.13684">CrossCheckGPT</a>, and human evaluation scores (for systems investigated in the CrossCheckGPT paper) are evaluated on the image-captioning subset of MHaluBench dataset.</li>
      <li><b><a href="https://huggingface.co/datasets/potsawee/avhallubench">AVHalluBench</a></b> (Visual and Audio): This is a video-captioning dataset where the task is to generate text descriptions given an input video. This dataset can be used for two different tasks; either generating <b>visual descriptions</b> or <b>audio descriptions</b>. Existing audio-visual hallucination metrics include <a href="https://arxiv.org/abs/2303.08896">SelfCheckGPT</a>, <a href="https://arxiv.org/abs/2405.13684">CrossCheckGPT</a>, and <a href="https://arxiv.org/abs/2405.13684">RefCheck</a>.</li>
</ul>
"""

LLM_BENCHMARKS_TEXT = f"""
This leaderboard presents hallucination benchmarks for multimodal LLMs on tasks of different input modalities, including image-captioning and video-captioning. For each task, we measure hallucination levels of the text output of various multimodal LLMs using existing hallucination metrics.

Some metrics such as POPE*, CHAIR, UniHD are designed specifically for image-to-text tasks, and thus are not directly applicable to video-to-text tasks. For the image-to-text benchmark, we also provide the ranking based human rating where annotators were asked to rate the outputs of the multimodal LLMs on MHaluBench. *Note that the POPE paper proposed both a dataset and a method. 

More information about each existing metric can be found in their relevant paper, and CrossCheckGPT is proposed in https://arxiv.org/pdf/2405.13684.

Currently, the leaderboard hasn't yet supported automatic evaluation of new models, but you are welcome to request an evaluation of a new model by creating a new discussion, or emailing us at potsawee@scb10x.com.
"""

EVALUATION_QUEUE_TEXT = """
Currently, the leaderboard hasn't yet supported automatic evaluation of new models, but you are welcome to request an evaluation of a new model by creating a new discussion, or emailing us at potsawee@scb10x.com.
"""

CITATION_BUTTON_LABEL = "Copy the following snippet to cite these results"
CITATION_BUTTON_TEXT = r"""@misc{sun2024crosscheckgpt,
      title={CrossCheckGPT: Universal Hallucination Ranking for Multimodal Foundation Models}, 
      author={Guangzhi Sun and Potsawee Manakul and Adian Liusie and Kunat Pipatanakul and Chao Zhang and Phil Woodland and Mark Gales},
      year={2024},
      eprint={2405.13684},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}"""
