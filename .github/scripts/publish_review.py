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

    code = re.match(r'comp(\d+)su26', folder).group(1)
    week = re.match(r'(week\d+)-review\.md', filename).group(1)
    target_repo = f"comp-{code}-su26"

    repo_url = f"https://x-access-token:{token}@github.com/{owner}/{target_repo}.git"
    subprocess.run(['git', 'clone', repo_url, 'target_repo'], check=True)

    week_dir = os.path.join('target_repo', week)
    os.makedirs(week_dir, exist_ok=True)

    shutil.copy(review_path, os.path.join(week_dir, filename))

    for link in local_links(review_path):
        src = os.path.join(folder, link)
        if os.path.isfile(src):
            shutil.copy(src, os.path.join(week_dir, os.path.basename(link)))

    subprocess.run(['git', '-C', 'target_repo', 'config',
                    'user.name', 'github-actions[bot]'], check=True)
    subprocess.run(['git', '-C', 'target_repo', 'config',
                    'user.email', 'github-actions[bot]@users.noreply.github.com'], check=True)
    subprocess.run(['git', '-C', 'target_repo', 'add', '.'], check=True)

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
