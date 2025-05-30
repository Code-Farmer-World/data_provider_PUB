import math
from typing import List

EARTH_RADIUS = 6378137.0  # 地球半徑 (公尺)

def degrees(rad: float) -> float:
    """弧度轉角度"""
    return rad * (180 / math.pi)

def radians(deg: float) -> float:
    """角度轉弧度"""
    return deg * math.pi / 180

class Degree:
    """經緯度座標"""
    def __init__(self, x: float, y: float):
        self.X = x  # 緯度
        self.Y = y  # 經度

    def __repr__(self):
        return f"Degree(Lat={self.X}, Lng={self.Y})"

def get_degree_coordinates(center: Degree, distance: float) -> List[Degree]:
    """以中心點計算正方形四個角落（距離為半邊長）"""
    dlat = degrees(distance / EARTH_RADIUS)
    dlng = degrees(2 * math.asin(math.sin(distance / (2 * EARTH_RADIUS)) / math.cos(radians(center.X))))

    return [
        Degree(round(center.X + dlat, 6), round(center.Y - dlng, 6)),  # 左上
        Degree(round(center.X - dlat, 6), round(center.Y - dlng, 6)),  # 左下
        Degree(round(center.X - dlat, 6), round(center.Y + dlng, 6)),   # 右下
        Degree(round(center.X + dlat, 6), round(center.Y + dlng, 6))  # 右上
       
    ]

def get_distance(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """計算兩點間距離（單位：公尺）"""
    x1, y1, x2, y2 = map(radians, [lat1, lng1, lat2, lng2])
    dot = math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)
    dot = max(min(dot, 1), -1)
    return EARTH_RADIUS * math.acos(dot)
