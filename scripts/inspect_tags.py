import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests


def inspect_tags(url: str) -> None:
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    data = response.json()

    items = data if isinstance(data, list) else next(
        (v for v in data.values() if isinstance(v, list)), []
    )

    all_tags: set[str] = set()
    for item in items:
        for tag in item.get("tags") or []:
            all_tags.add(tag.lower())

    sorted_tags = sorted(all_tags)

    print(f"URL:        {url}")
    print(f"Eventos:    {len(items)}")
    print(f"Tags únicos: {len(sorted_tags)}\n")
    for tag in sorted_tags:
        print(f"  {tag}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python inspect_tags.py <url>")
        sys.exit(1)

    inspect_tags(sys.argv[1])
