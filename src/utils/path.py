import os
import git

def get_repo_dir():
    # Get the git repo
    repo = git.Repo(os.path.dirname(os.path.abspath(__file__)), search_parent_directories=True)
    # Return the root path
    return repo.git.rev_parse("--show-toplevel")

def get_data_dir():
    repo_dir = get_repo_dir()
    return os.path.join(repo_dir, 'data')