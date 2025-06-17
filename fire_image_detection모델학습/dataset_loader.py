from roboflow import Roboflow
rf = Roboflow(api_key="zAkmnLnZgDoFFfBnKvKR")
project = rf.workspace("smopensourcefiredetection").project("firedetection-9toil")
version = project.version(6)
dataset = version.download("yolov8")
                                