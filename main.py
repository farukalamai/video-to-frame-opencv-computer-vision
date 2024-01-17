import cv2


video_path = 'video.mp4'

video = cv2.VideoCapture(video_path)
success,frame = video.read()
count = 0


while True:
  


  if success == True:
    name = 'Frames/'+str(count)+'.jpg'
    cv2.imwrite(name,frame)
    # video.set(cv2.CAP_PROP_POS_MSEC, (count**100))
    success,frame = video.read()
    
    count += 1

    key = cv2.waitKey(50)

    if key == 80 or key ==113:
      break
      cv2.destroyAllWindows()