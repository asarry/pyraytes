from maths.vector3d import Vector3D
from rendering.ray import Ray


class Light:
    """A Light has a color and defines an affect method allowing the let the light affect a given color."""

    def __init__(self, color):
        self.color = color

    def affect(self, initial_color, color, position, normal, ray, nearest_obj, objects):
        """Returns the color after affecting it."""
        pass


class AmbientLight(Light):
    """A Light has a color and defines an affect method allowing the let the light affect a given color."""

    def __init__(self, color):
        super().__init__(color)

    def affect(self, initial_color, color, position, normal, ray, nearest_obj, objects):
        """Returns the color after affecting it."""
        return initial_color + self.color * color


class DirectionalLight(Light):
    """A DirectionalLight has a color, a direction and an intensity."""

    def __init__(self, color, direction, intensity):
        super().__init__(color)
        self.direction = direction
        self.intensity = intensity

    def affect(self, initial_color, color, position, normal, ray, nearest_obj, objects):
        """Returns the color after affecting it."""
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
    """A PointLight has a color, a position, an intensity and xyz attenuations factors."""

    def __init__(
        self, color, position, intensity, attenuation_factors=(1.0, 0.1, 0.01)
    ):
        super().__init__(color)
        self.position = position
        self.intensity = intensity
        self.attenuation_factors = attenuation_factors

    def affect(self, initial_color, color, position, normal, ray, nearest_obj, objects):
        """Returns the color after affecting it."""
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
                self.attenuation_factors[0]
                + self.attenuation_factors[1] * dist
                + self.attenuation_factors[2] * dist * dist
            )

            initial_color += self.color * self.intensity * color * factor * atten
        return initial_color


def _is_in_shadow(ray, objects, target):
    """Returns if the target is in the shadow in a given scene."""

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
