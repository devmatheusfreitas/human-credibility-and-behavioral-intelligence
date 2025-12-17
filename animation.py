import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

df = pd.read_csv("face_landmarks.csv")

frames = sorted(df["frame"].unique())

fig, ax = plt.subplots()
scat = ax.scatter([], [], s=5)

ax.set_xlim(0, 1)
ax.set_ylim(1, 0)  # inverte Y pra ficar igual webcam
ax.set_title("Facial Landmarks Movement")

def update(frame_number):
    frame_df = df[df["frame"] == frame_number]
    scat.set_offsets(frame_df[["x", "y"]].values)
    ax.set_title(f"Frame {frame_number}")
    return scat,

ani = FuncAnimation(
    fig,
    update,
    frames=frames,
    interval=0  # ms
)

plt.show()