from maths.vector3d import Vector3D
from rendering.ray import Ray


class Light:
    def __init__(self, color):
        self.color = color

    def affect(self, initial_color, color, position, normal, ray, nearest_obj, objects):
        pass


class AmbientLight(Light):
    def __init__(self, color):
        super().__init__(color)

    def affect(self, initial_color, color, position, normal, ray, nearest_obj, objects):
        return initial_color + self.color * color


class DirectionalLight(Light):
    def __init__(self, color, direction, intensity):
        super().__init__(color)
        self.direction = direction
        self.intensity = intensity

    def affect(self, initial_color, color, position, normal, ray, nearest_obj, objects):
        light_ray_dir = -self.direction
        if not _is_in_shadow(Ray(position, light_ray_dir), objects, None):

            specular_factor = (
                max(Vector3D.dot(normal.reflect(light_ray_dir), -ray.direction), 0)
                ** nearest_obj.material.specular_exponent
                * nearest_obj.material.specular_rate
            )

            diffuse_factor = (
                max(Vector3D.dot(light_ray_dir, normal), 0)
                * nearest_obj.material.diffuse_rate
            )

            factor = diffuse_factor + specular_factor

            initial_color += initial_color * self.intensity * color * factor
        return initial_color


class PointLight(Light):
    def __init__(
        self, color, position, intensity, attenuation_factors=(1.0, 0.1, 0.01)
    ):
        super().__init__(color)
        self.position = position
        self.intensity = intensity
        self.attenuation_factors = attenuation_factors

    def affect(self, initial_color, color, position, normal, ray, nearest_obj, objects):
        light_ray_dir = (self.position - position).normalize()
        if not _is_in_shadow(Ray(position, light_ray_dir), objects, self.position):
            specular_factor = (
                max(Vector3D.dot(normal.reflect(light_ray_dir), -ray.direction), 0)
                ** nearest_obj.material.specular_exponent
                * nearest_obj.material.specular_rate
            )

            diffuse_factor = (
                max(Vector3D.dot(light_ray_dir, normal), 0)
                * nearest_obj.material.diffuse_rate
            )

            factor = diffuse_factor + specular_factor
            dist = (self.position - position).length()
            atten = 1.0 / (
                self.atten_factors[0]
                + self.atten_factors[1] * dist
                + self.atten_factors[2] * dist * dist
            )

            initial_color += self.color * self.intensity * color * factor * atten
        return initial_color


def _is_in_shadow(ray, objects, target):
    for obj in objects:
        obj_dist = obj.intersect(ray)
        if obj_dist:
            if target:
                target_dist = (target - ray.origin).length()
                if target_dist < obj_dist:
                    return False
                else:
                    return True
            return True
    return False
