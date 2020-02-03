from reader import feed
from my_timer import Timer
import time


@Timer()
def main():
    """Download and print the latest tutorial from RP"""
    feed.get_article(0)

    # with Timer():
    #     for tutorial_num in range(10):
    #         tutorial = feed.get_article(tutorial_num)
    #     # print(tutorial)
    #
    # # download_time = Timer.timers["download"]
    # # print(f"Downloaded 10 tutorials in {download_time:0.2f} seconds")


if __name__ == "__main__":
    main()
