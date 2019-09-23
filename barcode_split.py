import numpy as np
import cv2 as cv
import time
import os
from datetime import datetime

width = 3000
height = 2000
every_x_frame = 1
dir = 'movies'


def main():
    for name in range(0, 6):
        print(datetime.now())
        start = time.time()

        cap = cv.VideoCapture(os.path.join(dir, f'{name}.mp4'))

        num_rows = get_num_rows(cap)
        frame_width, frame_height = get_frame_size(cap)
        total_frames = cap.get(cv.CAP_PROP_FRAME_COUNT)

        slices, fc = [], 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if fc % 1000 == 0:
                print_eta(total_frames, start, fc)
            if fc % every_x_frame == 0:
                frame = cv.resize(frame, (frame_width, frame_height))
                slice = np.mean(frame, axis=1).astype(np.uint8)
                slices.append(np.expand_dims(slice, 1))
            fc = fc + 1
        cap.release()

        threshold = len(slices) // num_rows
        rows, rows_sc = [], []
        for i in range(0, len(slices) - threshold + 1, threshold):
            row = slices[i:i + threshold]
            rows.append(np.concatenate(row, axis=1))
            rows_sc.append(row_to_single_color(row))

        img = np.concatenate(rows, axis=0)
        np.save(os.path.join('raw', f'{str(name)}_raw_split'), img)
        cv.imwrite(os.path.join('images', f'{name}_split.jpg'), img)
        img = np.concatenate(rows_sc, axis=0)
        cv.imwrite(os.path.join('images', f'{name}s_split.jpg'), img)

        dur = time.time() - start
        print(f'slice shape: {slices[0].shape}')
        print(f'number of slices: {len(slices)}')
        print(f'img shape: {img.shape}')
        print(f'total duration: {int(dur // 60)}:{int(dur % 60)}')
        print(f'frames processed: {int(total_frames)}')
        print(f'fps: {int(total_frames // dur)}')


def get_num_rows(cap):
    total_frames = cap.get(cv.CAP_PROP_FRAME_COUNT)
    return int(total_frames / every_x_frame / width)


def get_frame_size(cap):
    num_rows = get_num_rows(cap)
    frame_height = height / num_rows
    ratio = cap.get(cv.CAP_PROP_FRAME_WIDTH) / cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    frame_width = int(frame_height * ratio)
    return frame_width, int(frame_height)


def row_to_single_color(row):
    slices = []
    for slice in row:
        color = np.mean(slice, axis=0).astype(np.uint8)
        slice = np.empty((slice.shape[0], 1, 3), dtype=np.uint8)
        slice[:, :] = color
        slices.append(slice)
    return np.concatenate(slices, axis=1)


def print_eta(total_frames, start, fc):
    eta = (time.time() - start) / (fc + 1) * (total_frames - fc)
    print(f'{round(fc / total_frames * 100 * 100) / 100}% {int(eta / 3600)}:{int((eta % 3600) / 60)}:{int(eta % 60)}')


if __name__ == "__main__":
    main()
