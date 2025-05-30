from geo_utils import Degree, get_degree_coordinates

# 經緯度集合中心
center = Degree(25.049698872203532, 121.512095472458228)

# 半徑 一棟房的點大概10公尺
half_side = 10.0

# 計算正方形四個角落的經緯度
corners = get_degree_coordinates(center, half_side)

# 輸出結果- 左上-左下-右下-右上
print("Corner coordinates of 10m square:")
for i, corner in enumerate(corners, 1):
    print(f"{i}: Lng = {corner.Y}, Lat = {corner.X}")
