from git import Repo
from tqdm import tqdm

repo = Repo('./')
repo.index.commit("Fix Footer");