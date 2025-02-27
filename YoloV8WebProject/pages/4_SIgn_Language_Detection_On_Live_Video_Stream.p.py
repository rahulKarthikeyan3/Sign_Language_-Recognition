import streamlit as st 
from streamlit_webrtc import webrtc_streamer
import av
from ultralytics import YOLO


# load yolo model

yolo =  YOLO('C:\\Users\\rahul\\OneDrive\\Desktop\\Multi-Purpose-Object-Detection-with-YOLOV8-Pose-Detection-and-Sign-Language-Recognition-main\\YoloV8WebProject\\Model_Data\\yolo8n-signlanguagedetection.pt')


def video_frame_callback(frame):
    # img = frame.to_ndarray(format="bgr24")
    # # any operation 
    # #flipped = img[::-1,:,:]
    # pred_img = yolo.predictions(img)

    # return av.VideoFrame.from_ndarray(pred_img, format="bgr24")
    img = frame.to_image()
    res = yolo(img)
    res_plotted = res[0].plot().astype('uint8')
    return av.VideoFrame.from_ndarray(res_plotted, format="bgr24")

webrtc_streamer(key="example", 
                video_frame_callback=video_frame_callback,
                media_stream_constraints={"video":True,"audio":False})