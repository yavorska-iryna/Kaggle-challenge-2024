import os
import git

def get_repo_dir():
    """
    Get the path to the root of the repo dir

    Args:
        None
    
    Returns:
        str
    """
    # Get the git repo
    repo = git.Repo(os.path.dirname(os.path.abspath(__file__)), search_parent_directories=True)
    # Return the root path
    return repo.git.rev_parse("--show-toplevel")

def get_data_dir(): 
    """
    Get the path to the data directory

    Args:
        None
    
    Returns:
        str
    """
    repo_dir = get_repo_dir()
    return os.path.join(repo_dir, 'data')