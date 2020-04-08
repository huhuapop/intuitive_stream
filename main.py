from multiprocessing import Queue, Process, Event
from videoplayer import Videoplayer
from analysis import Analysis
import sys


if __name__ == '__main__':
    filename = "data/Robotic_Surgical_System_720.mp4"  # video path
    frametime = 10  # frame interval(ms)
    queue = Queue()  # shared the data between the player and analysis
    savedir = "data/capture"  # Save the capture frame
    playerevent = Event()    # Check the status of the Play thread
    # Init video player object and start a process to control the video playing
    player = Videoplayer(filename, frametime)
    process_video = Process(target=player.play_video, args=(queue, playerevent, ))
    process_video.start()

    # Init analysis object and start a process to control the analysis
    m_analysis = Analysis()
    process_analysis = Process(target=m_analysis.analyse, args=(savedir, queue, ))
    process_analysis.start()
    while True:
        # if the video has finished to play and queue is empty, closed these two threads
        if playerevent.is_set() and queue.empty():
            process_video.terminate()
            process_analysis.terminate()
            sys.exit(1)





