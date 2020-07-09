import signal
import time
import argparse


exit_flag = False


def dirwatcher():
    """Long running program to watch a directory and log any files added, deleted, or changed"""
    pass

def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT. Other signals can be mapped here as well (SIGHUP?)
    Basically, it just sets a global flag, and main() will exit its loop if the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    # log the associated signal name
    logger.warn('Received ' + signal.Signals(sig_num).name)

def create_parser():
    parser = argparse.ArgumentParser(
        description="Transform and dislay a message.")
    # positional arguments maintain their position
    parser.add_argument('msg', help="message to display")
    parser.add_argument('-b', help="border character around message")
    parser.add_argument(
        '-n', type=int, help="number of times to display the message")
    parser.add_argument('-u', action='store_true',
                        help="transform message to uppercase")
    parser.add_argument('-l', action='store_true',
                        help="transform message to lowercase")
    parser.add_argument('-t', action='store_true',
                        help="transform message to titlecase")
    return parser


def main():
    # Hook into these two signals from the OS
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if OS sends
    # either of these to my process.

    while not exit_flag:
        try:
            # call my directory watching function
            pass
        except Exception as e:
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            pass

        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        time.sleep(polling_interval)

    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start






if __name__() == '__main__':
    main()