from pathlib import Path


BOARD_SIZE = 8
NODES = 0
COPY_TIME = 0
LEAF_NODES = 0

PROJ_DIR = Path().cwd()
leaf_nodes_path = PROJ_DIR / "build"
leaf_nodes_path.mkdir(parents=True, exist_ok=True)
