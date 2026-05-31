import argparse
import json
from pathlib import Path


PROMPT_FILE = Path(__file__).parent / "prompts.json"


def load_prompts():
    with PROMPT_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def show_prompt(prompt):
    print("=" * 60)
    print(f"ID: {prompt['id']}")
    print(f"Category: {prompt['category']}")
    print(f"Title: {prompt['title']}")
    print("-" * 60)
    print(prompt["prompt"])
    print("=" * 60)
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Search Japanese AI prompts from prompts.json"
    )
    parser.add_argument(
        "--category",
        help="Filter prompts by category, for example: writing, summary, learning",
    )
    parser.add_argument(
        "--search",
        help="Search prompts by keyword",
    )

    args = parser.parse_args()
    prompts = load_prompts()

    if args.category:
        prompts = [
            prompt for prompt in prompts
            if prompt["category"] == args.category
        ]

    if args.search:
        keyword = args.search.lower()
        prompts = [
            prompt for prompt in prompts
            if keyword in prompt["title"].lower()
            or keyword in prompt["prompt"].lower()
            or keyword in prompt["category"].lower()
        ]

    if not prompts:
        print("No prompts found.")
        return

    for prompt in prompts:
        show_prompt(prompt)


if __name__ == "__main__":
    main()
