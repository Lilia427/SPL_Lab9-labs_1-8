class Transformations:
    @staticmethod
    def scale(points, factor):
        return [(x * factor, y * factor, z * factor) for x, y, z in points]

    @staticmethod
    def translate(points, dx, dy, dz):
        return [(x + dx, y + dy, z + dz) for x, y, z in points]

    @staticmethod
    def rotate_z(points, angle):
        import math
        angle_rad = math.radians(angle)
        cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)
        return [
            (x * cos_a - y * sin_a, x * sin_a + y * cos_a, z)
            for x, y, z in points
        ]