import pandas as pd
from landmark_map import FACIAL_LANDMARKS
import matplotlib.pyplot as plt

df = pd.read_csv("face_landmarks.csv")

def eye_openness(df, eye="left"):
    top = FACIAL_LANDMARKS["eyes"][eye]["top"]
    bottom = FACIAL_LANDMARKS["eyes"][eye]["bottom"]

    eye_df = df[df["landmark_id"].isin([top, bottom])]
    pivot = eye_df.pivot(index="frame", columns="landmark_id", values="y")

    return abs(pivot[top] - pivot[bottom])

eye_open = eye_openness(df)

eye_open.plot(title="Eye Openness Over Time")


def region_activity(df, region_points):
    region_df = df[df["landmark_id"].isin(region_points)]
    return region_df.groupby("frame")[["x", "y"]].std().mean(axis=1)


def facial_heatmap(df, frame):
    frame_df = df[df["frame"] == frame]

    plt.scatter(
        frame_df["x"],
        frame_df["y"],
        c=frame_df["z"],
        cmap="coolwarm",
        s=5
    )

    plt.gca().invert_yaxis()
    plt.title(f"Facial Heatmap – Frame {frame}")
    plt.show()

facial_heatmap(df, frame=15)
