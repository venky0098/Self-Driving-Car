
from sensors.lidar import get_lidar_data
from sensors.radar import get_radar_data
from sensors.camera import get_camera_frame
from models.object_detection import detect_objects
from models.path_planning import plan_path
from utils.visualizer import show_path

def main():
    lidar = get_lidar_data()
    radar = get_radar_data()
    camera = get_camera_frame()

    detected = detect_objects(camera)
    x, y = plan_path((lidar, radar, camera))

    show_path(x, y)

if __name__ == "__main__":
    main()
