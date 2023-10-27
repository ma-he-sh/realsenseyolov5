import cv2
import numpy as np
import pyrealsense2 as rs
import torch

# git clone https://github.com/ultralytics/yolov5
model = torch.hub.load('./yolov5', 'custom', path='./trained_custom_model/exp15/weights/best.pt', source='local')

# connect to realsense camera
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)

# Main loop
try:
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        # convert the frame to np array
        frame = np.asanyarray(color_frame.get_data())

        # input the frame
        results = model(frame)
        for result in results.xyxy[0]:
            x1, y1, x2, y2, confidence, class_id = result

            if( confidence > 0.25 and class_id==0 ):
                # Draw a rectangle around the object
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 255), 4)
                cv2.putText(frame, 'Strawberry', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        cv2.imshow("Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    pipeline.stop()
    cv2.destroyAllWindows()
except Exception as e:
    print("Handled exceptions", e)