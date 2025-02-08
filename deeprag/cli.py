import argparse
import logging
from deeprag.configuration import Configuration, init_config
from deeprag.online_query import query
from deeprag.offline_loading import load_from_local_files, load_from_website

httpx_logger = logging.getLogger("httpx")  # disable openai's logger output
httpx_logger.setLevel(logging.WARNING)

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)  # disable warning output

def main():
    config = Configuration()  #Customize your config here
    init_config(config = config)

    parser = argparse.ArgumentParser(
        prog="deeprag", description="Deep RAG Agent."
    )
    ## Arguments of query
    parser.add_argument(
        "--query", type=str, default="", help="query question or search topic."
    )
    parser.add_argument(
        "--max_iter",
        type=int,
        default=8,
        help="Max iterations of reflection. Default is 8.",
    )

    ## Arguments of loading
    parser.add_argument(
        "--load",
        type=str,
        help="Load knowledge from a local files or from urls.",
    )
    parser.add_argument(
        "--collection_name",
        type=str,
        default=None,
        help="Destination collection name of loaded knowledge.",
    )


    args = parser.parse_args()
    if args.query:
        query(args.query, max_iter=args.max_iter)
    else:
        if args.load:
            if args.load.startswith("http"):
                load_from_website(args.load)
            else:
                load_from_local_files(args.load)
        else:
            print("Please provide a query or a load argument.")


if __name__ == "__main__":
    main()
