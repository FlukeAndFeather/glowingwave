#!/usr/bin/env python
"""
Generate HTML from Jupyter notebooks for GitHub Pages

This script converts all notebooks in the notebooks/ directory to HTML
and saves them to the docs/ directory for GitHub Pages.

Usage:
    python scripts/generate_html.py
"""

import subprocess
from pathlib import Path


def convert_notebook_to_html(notebook_path, output_dir):
    """
    Convert a Jupyter notebook to HTML.

    Parameters
    ----------
    notebook_path : Path
        Path to the notebook file
    output_dir : Path
        Directory to save the HTML output
    """
    print(f"Converting {notebook_path.name}...")

    cmd = [
        'jupyter', 'nbconvert',
        '--to', 'html',
        str(notebook_path),
        '--output-dir', str(output_dir)
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"  ✓ Successfully converted to {output_dir / notebook_path.stem}.html")
    else:
        print(f"  ✗ Error converting {notebook_path.name}")
        print(result.stderr)

    return result.returncode == 0


def main():
    """Convert all notebooks to HTML for GitHub Pages."""
    # Set up paths
    project_root = Path(__file__).parent.parent
    notebooks_dir = project_root / 'notebooks'
    docs_dir = project_root / 'docs'

    # Ensure docs directory exists
    docs_dir.mkdir(exist_ok=True)

    print("=" * 60)
    print("GENERATING HTML FOR GITHUB PAGES")
    print("=" * 60)

    # Find all notebook files
    notebooks = sorted(notebooks_dir.glob('*.ipynb'))

    if not notebooks:
        print("No notebooks found in notebooks/")
        return

    print(f"\nFound {len(notebooks)} notebook(s)")
    print("-" * 60)

    # Convert each notebook
    success_count = 0
    for notebook in notebooks:
        if convert_notebook_to_html(notebook, docs_dir):
            success_count += 1

    print("\n" + "=" * 60)
    print(f"COMPLETE: {success_count}/{len(notebooks)} notebooks converted")
    print("=" * 60)
    print(f"\nHTML files saved to: {docs_dir}")
    print("\nTo enable GitHub Pages:")
    print("  1. Go to your repo Settings > Pages")
    print("  2. Set source to 'Deploy from a branch'")
    print("  3. Select 'main' branch and '/docs' folder")
    print("  4. Save and wait for deployment")


if __name__ == '__main__':
    main()
