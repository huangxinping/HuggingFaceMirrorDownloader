import subprocess
import argparse
import os
from utils import install_library, is_library_installed, str2bool

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=str, default=None)
    parser.add_argument("--local-dir", type=str, default=None)
    parser.add_argument("--num-retries", type=int, default=10)
    parser.add_argument("--use_model_scope", type=str2bool, default=True)
    args = parser.parse_args()
    assert args.repo is not None, "Please specify the repo name"

    for _ in range(args.num_retries):
        if args.use_model_scope:
            if not is_library_installed("modelscope"):
                install_library("modelscope")
            from modelscope import snapshot_download

            if args.local_dir is None:
                args.local_dir = f"{os.getcwd()}"
            snapshot_download(args.repo, cache_dir=args.local_dir, repo_type="dataset")
        else:
            if args.local_dir is None:
                args.local_dir = args.repo
            else:
                args.local_dir = f"{args.local_dir}/{args.repo}"
            subprocess.run(
                [
                    "huggingface-cli",
                    "download",
                    "--repo-type=dataset",
                    args.repo,
                    f"--local-dir={args.local_dir}",
                ]
            )
