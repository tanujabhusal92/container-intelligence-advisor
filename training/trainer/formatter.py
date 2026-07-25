"""
Dataset Formatter

Converts dataset records into instruction format
for supervised fine-tuning.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""


def format_dataset(dataset):

    print("=" * 60)
    print("Formatting Dataset")
    print("=" * 60)


    def formatting(example):

        text = f"""
### Instruction:
{example["instruction"]}

### Input:
{example["input"]}

### Response:
{example["output"]}
"""

        return {
            "text": text.strip()
        }


    formatted_dataset = dataset.map(
        formatting
    )


    print("✓ Dataset Formatting Completed")

    return formatted_dataset
