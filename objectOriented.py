#This will be a object oriented version of the virtual3d game.
import cv2 

class faceFinder:
    """Uses Haar Cascade filter to detect largest face from a frame."""
    def init(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        print("Face Finder initialize")


    def find_face(self, frame):
        """Returns face center (x,y), Draws rect on a frame"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, minNeighbors=9)

        if faces is None:
            return None

        bx=by=bw=bh=0

        # x = top left corner, y = bottom left
        for (x, y, w, h) in faces:
            if w > bw:
                bx,by,bw,bh = x,y,w,h
        
        cv2.rectangle(frame, (bx, by), (bx+bw, by+bh), (0, 255, 255), 3)
        return ((bx+bw)/2, (by+bh)/2)

#---------------------------------------------------------------------
#Main
#-----------------------------------------------------------------------

print("Starting O.O Virtual3d")


ff = faceFinder()
print("Virtual3d complete.")


