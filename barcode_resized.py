import numpy as np
import cv2 as cv
import time
import os
from datetime import datetime

width = 3000
height = 500
every_x_frame = 1
dir = 'movies'


def main():
    for i in range(99, 100):
        print(datetime.now())
        start = time.time()

        cap = cv.VideoCapture(os.path.join(dir, f'{i}.mp4'))

        frame_width, frame_height = get_frame_size(cap)
        total_frames = cap.get(cv.CAP_PROP_FRAME_COUNT)

        img, fc = [], 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if fc % 1000 == 0:
                print_eta(total_frames, start, fc)
            if fc % every_x_frame == 0:
                frame = cv.resize(frame, (frame_width, frame_height))
                slice = np.mean(frame, axis=1).astype(np.uint8)
                img.append(np.expand_dims(slice, 1))
            fc = fc + 1
        cap.release()

        img = np.concatenate(img, axis=1)
        np.save(os.path.join('raw', f'{str(i)}_raw'), img)
        img = cv.resize(img, (width, height))
        cv.imwrite(os.path.join('images', f'{i}.jpg'), img)
        img = to_single_color(img)
        cv.imwrite(os.path.join('images', f'{i}s.jpg'), img)

        dur = time.time() - start
        print(f'img shape: {img.shape}')
        print(f'total duration: {int(dur // 60)}:{int(dur % 60)}')
        print(f'frames processed: {int(total_frames)}')
        print(f'fps: {int(total_frames // dur)}')


def get_frame_size(cap):
    ratio = cap.get(cv.CAP_PROP_FRAME_WIDTH) / cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    frame_width = int(height * ratio)
    return frame_width, height


def to_single_color(img):
    img = np.mean(img, axis=0).astype(np.uint8)
    img = np.expand_dims(img, axis=0)
    return cv.resize(img, (width, height))


def print_eta(total_frames, start, fc):
    eta = (time.time() - start) / (fc + 1) * (total_frames - fc)
    print(f'{round(fc / total_frames * 100 * 100) / 100}% {int(eta / 3600)}:{int((eta % 3600) / 60)}:{int(eta % 60)}')


if __name__ == "__main__":
    main()
