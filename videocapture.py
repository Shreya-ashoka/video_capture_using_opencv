import cv2
cap=cv2.VideoCapture(0)
if(cap==False):
    print("couldn't open")
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))

video_cod=cv2.VideoWriter_fourcc(*'XVID')
video_output= cv2.VideoWriter('Capture_video.MP4',video_cod,30,(frame_width,frame_height))
while(True):
    ret , frame = cap.read()

    if ret==True:
      video_output.write(frame)
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF==ord('q'):
          break
    else:
     break
cap.release()   
video_output.release()
cv2.destroyAllWindows()
print("the video was saved successfully")
