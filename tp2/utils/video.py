import cv2
import ipywidgets as widgets
from IPython.display import display, clear_output
from threading import Thread

class VideoPlayer:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.frame_rate = self.cap.get(cv2.CAP_PROP_FPS)
        self.current_frame = 0
        self.playing = False
        self.show_info = False

        # Controles
        self.play_pause_button = widgets.Button(description="Play")
        self.next_button = widgets.Button(description="Next Frame")
        self.info_checkbox = widgets.Checkbox(value=False, description='Show Info')
        self.controls = widgets.HBox([self.play_pause_button, self.next_button, self.info_checkbox])

        # Conectar eventos
        self.play_pause_button.on_click(self.toggle_play_pause)
        self.next_button.on_click(self.next_frame)
        self.info_checkbox.observe(self.toggle_info, names='value')

    def display_controls(self):
        display(self.controls)
        self.show_frame()

    def toggle_play_pause(self, b):
        if self.playing:
            self.playing = False
            self.play_pause_button.description = "Play"
        else:
            self.playing = True
            self.play_pause_button.description = "Pause"
            Thread(target=self.play).start()

    def next_frame(self, b):
        self.playing = False
        self.play_pause_button.description = "Play"
        self.current_frame += 1
        if self.current_frame >= self.frame_count:
            self.current_frame = 0
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)
        self.show_frame()

    def toggle_info(self, change):
        self.show_info = change['new']
        self.show_frame()

    def play(self):
        while self.playing:
            ret, frame = self.cap.read()
            if not ret:
                self.playing = False
                self.play_pause_button.description = "Play"
                break

            self.current_frame += 1
            if self.show_info:
                cv2.putText(frame, f'Frame: {self.current_frame}/{self.frame_count}', (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                elapsed_time = self.current_frame / self.frame_rate
                cv2.putText(frame, f'Time: {elapsed_time:.2f}s', (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            _, buffer = cv2.imencode('.jpg', frame)
            display_img = widgets.Image(value=buffer.tobytes(), format='jpg', width=640, height=480)
            clear_output(wait=True)
            display(self.controls)
            display(display_img)

            if cv2.waitKey(int(1000 / self.frame_rate)) & 0xFF == ord('q'):
                break

    def show_frame(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)
        ret, frame = self.cap.read()
        if ret:
            if self.show_info:
                cv2.putText(frame, f'Frame: {self.current_frame}/{self.frame_count}', (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                elapsed_time = self.current_frame / self.frame_rate
                cv2.putText(frame, f'Time: {elapsed_time:.2f}s', (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            _, buffer = cv2.imencode('.jpg', frame)
            display_img = widgets.Image(value=buffer.tobytes(), format='jpg', width=640, height=480)
            clear_output(wait=True)
            display(self.controls)
            display(display_img)
