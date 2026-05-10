# Toxic Comment Moderation — Trust & Safety Prototype

A quick prototype evaluating LLM prompt strategies for toxic content classification.

## What This Does

- Compares 4 approaches to detect toxic comments: keyword baseline, simple prompt, detailed prompt, and few-shot prompt
- Evaluates precision, recall, and F1 on balanced labeled data
- Identifies edge cases and iteratively improves prompt coverage

## Dataset

[Jigsaw Toxic Comment Classification Challenge](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge)
- 300 balanced samples (50% toxic, 50% non-toxic)
- Binary classification: toxic vs. safe

## Results

| Model | Accuracy | Precision | Recall | F1 |
|-------|----------|-----------|--------|-----|
| Keyword Baseline | 0.69 | 0.806 | 0.50 | 0.617 |
| LLM Simple Prompt | 0.86 | 0.891 | 0.82 | 0.854 |
| LLM Detailed Prompt | 0.88 | 0.880 | 0.88 | 0.880 |
| **LLM Few-Shot Prompt** | **0.87** | **0.814** | **0.96** | **0.881** |

**Key finding:** Few-shot prompting achieved **96% recall** on toxic content, significantly outperforming the keyword baseline. This matters for Trust & Safety because missing abusive content (false negatives) is more harmful than over-flagging safe content.

## Key Edge Cases Found

- **Sexual obscenity:** Initial few-shot examples lacked sexual content; model missed explicit sexual harassment. Fixed by adding targeted examples.
- **Sarcasm:** "You're so talented... NOT" — caught correctly by few-shot context.
- **Ambiguous innuendo:** Subtle sexual references remain challenging and may need human review.

## Setup

```bash
pip install -r requirements.txt

# Add your API key to .env
echo "GEMINI_API_KEY=your-key-here" &gt; .env

# Run the notebook
jupyter notebook notebooks/01_toxic_comment_prototype.ipynb