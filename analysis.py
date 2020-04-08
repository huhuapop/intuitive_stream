import cv2
import os


class Analysis:
    """
    Analysis Class
    """

    def analyse(self, savedir, queue):
        """
          analyse the frame at playing
          Parameters:
            savedir - the directory for saving frame
            queue - a queue which shared the data between the player and analysis
          """
        i = 0
        path = savedir+"/data_"
        test = os.listdir(savedir)

        # Remove the image files for previous recording
        for item in test:
            os.remove(os.path.join(savedir, item))
        while (True):
            try:
                frame_org = queue.get()
                # Resize the image(this is an example)
                resize = cv2.resize(frame_org, (352, 240), interpolation=cv2.INTER_LINEAR)
                if i % 10 == 0:
                    # Save the first frame in each ten frames as jpg file
                    cv2.imwrite(path + str(i) + '.jpg', frame_org)
                i += 1
            except Exception as e:
                print(e)
