import cv2


class Videoplayer:
    """
    Video Player Class(Using Factory Design Pattern)
    """

    def __init__(self, path, frame_time):
        """
         Init the Player
         Parameters:
           path - video path
           frame_time - the interval between each frame
        """
        self.path = path
        self.frame_time = frame_time

    def play(self, frame_org):
        """
         Player the frame
         Parameters:
           frame_org - a frame will play by OpenCV
        """
        cv2.imshow('frame', frame_org)
        return

    def pause(self):
        """
        Pause the Player
       """
        cv2.waitKey(0)
        return

    def play_video(self, queue, player_event, *args, **kwargs):
        """
          Player the video
          Parameters:
            queue - a queue which shared the data between the player and analysis
            player_event - the status of the thread
          """
        if self.path:
            try:
                vidcap = cv2.VideoCapture(self.path)  #
                while (vidcap.isOpened()):
                    try:
                        success, frame_org = vidcap.read()  # Capture frame-by-frame
                        if success:
                            self.play(frame_org)
                            queue.put(frame_org)
                            key = cv2.waitKey(self.frame_time)
                            if key & 0xFF == ord('q'):
                                player_event.set()
                                break
                            elif key == ord('p'):
                                self.pause()  # wait until any key is pressed
                        else:
                            player_event.set()  # set event and the video player has finished playing
                            break
                    except Exception as e:
                        print(e)
                        break
                player_event.set()
                # Release the resource for video playing
                vidcap.release()
                cv2.destroyAllWindows()
            except Exception as e:
                print(e)
                return
        else:
            print("please check the video path")
        return
