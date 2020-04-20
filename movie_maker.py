import cv2

videoName = 'trim.mov'
savePath = 'trim.mp4'

#読み出し用の変数を用意
cap = cv2.VideoCapture(videoName)

# 書き出し用の変数を用意
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter(savePath, fourcc, fps, (width, height))

# 読み込んだ動画を一枚ずつ読み込んで、動画を生成する
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        out.write(frame)
    else:
        break

# お片付け
cap.release()
