# publish_review.py
#
# Reads a list of review file paths from stdin (one per line) and publishes
# each one to the corresponding student-facing course repo.
#
# Input path format:  comp<NNN>su26/week<NN>-review.md
#   e.g.  comp271su26/week03-review.md
#
# Target repo format: comp-<NNN>-su26
#   e.g.  comp-271-su26
#
# What "publish" means:
#   1. Clone the target repo using the PUBLISH_TOKEN and REPO_OWNER env vars.
#   2. Create (or reuse) a week<NN>/ subdirectory inside it.
#   3. Copy the review .md file into that subdirectory.
#   4. Copy any locally-linked files referenced in the review (e.g. .py code
#      files) into the same subdirectory, so relative links remain valid.
#   5. Commit and push if anything changed; skip silently if not.
#
# Environment variables (set by the GitHub Actions workflow):
#   GH_TOKEN   — personal access token with write access to the target repo
#   REPO_OWNER — GitHub username or org that owns the target repo

import os
import re
import shutil
import subprocess
import sys


def local_links(md_path):
    """Return relative file paths linked in the markdown, skipping external URLs."""
    with open(md_path) as f:
        content = f.read()
    links = re.findall(r'\[.*?\]\(([^)]+)\)', content)
    return [l for l in links if not l.startswith('http')]


def publish(review_path, owner, token):
    folder, filename = review_path.split('/', 1)

    # Derive course number and week from the path components.
    code = re.match(r'comp(\d+)su26', folder).group(1)
    week = re.match(r'(week\d+)-review\.md', filename).group(1)
    target_repo = f"comp-{code}-su26"

    repo_url = f"https://x-access-token:{token}@github.com/{owner}/{target_repo}.git"
    subprocess.run(['git', 'clone', repo_url, 'target_repo'], check=True)

    # Place the review file and any linked assets in a per-week subdirectory.
    week_dir = os.path.join('target_repo', week)
    os.makedirs(week_dir, exist_ok=True)

    shutil.copy(review_path, os.path.join(week_dir, filename))

    # Copy locally-linked files (e.g. code examples) so relative links in the
    # review remain valid when students view it in the target repo.
    for link in local_links(review_path):
        src = os.path.join(folder, link)
        if os.path.isfile(src):
            shutil.copy(src, os.path.join(week_dir, os.path.basename(link)))

    subprocess.run(['git', '-C', 'target_repo', 'config',
                    'user.name', 'github-actions[bot]'], check=True)
    subprocess.run(['git', '-C', 'target_repo', 'config',
                    'user.email', 'github-actions[bot]@users.noreply.github.com'], check=True)
    subprocess.run(['git', '-C', 'target_repo', 'add', '.'], check=True)

    # Only commit and push when there are actual changes; a re-push of an
    # unchanged review should be a no-op in the target repo.
    changed = subprocess.run(
        ['git', '-C', 'target_repo', 'diff', '--staged', '--quiet']
    )
    if changed.returncode != 0:
        subprocess.run(['git', '-C', 'target_repo', 'commit',
                        '-m', f'publish {week} review'], check=True)
        subprocess.run(['git', '-C', 'target_repo', 'push'], check=True)

    shutil.rmtree('target_repo')


def main():
    token = os.environ['GH_TOKEN']
    owner = os.environ['REPO_OWNER']
    for line in sys.stdin:
        path = line.strip()
        if path:
            print(f"Publishing {path} ...")
            publish(path, owner, token)


if __name__ == '__main__':
    # Leo I.
    main()
