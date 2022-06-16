from maths.vector3d import Vector3D
from multiprocessing import Manager, Process
from rendering.lights import AmbientLight, DirectionalLight, PointLight
from rendering.objects import Plane, Sphere
from rendering.ray import Ray
from threading import Thread
from rendering.color import Color


class Engine:
    """An Engine has a camera, a scene, a resulting image, a maximem allowed depth as well as a number of threads."""

    BIAS = 0.0000001

    def __init__(self, camera, scene, image, max_depth, num_thread):
        self.camera = camera
        self.scene = scene
        self.image = image
        self.max_depth = max_depth
        self.num_thread = num_thread

    def render(self):
        """Renders the image using multiple threads."""
        step = self.image.height / self.num_thread

        ranges = []
        for i in range(self.num_thread - 1):
            ranges.append((int(i * step), int(i * step + step)))
        ranges.append((int((self.num_thread - 1) * step), int(self.image.height)))

        m = Manager()
        rows = {i: m.list() for i in range(self.num_thread)}
        threads = []
        for i in range(len(ranges)):
            threads.append(
                Process(
                    target=self._sub_render,
                    args=(ranges[i][0], ranges[i][1], rows[i]),
                )
            )
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        del self.image.data[:]

        for i in range(len(rows)):
            self.image.data.extend(rows[i])

    def _sub_render(self, start, end, rows):
        """Threaded rendering method."""
        for h in range(start, end):
            row = []
            for w in range(self.image.width):
                row.append(
                    self._trace_ray(
                        self.camera.corresponding_ray(
                            (self.image.width, self.image.height), (w, h)
                        ),
                        0,
                    )
                )
            rows.append(row)

    def _nearest_obj(self, ray):
        """Returns the nearest object intersected by the ray and None otherwise."""
        nearest_obj = None
        nearest_obj_dist = None
        for obj in self.scene.objects:
            obj_dist = obj.intersect(ray)
            if obj_dist:
                if not nearest_obj_dist or obj_dist < nearest_obj_dist:
                    nearest_obj_dist = obj_dist
                    nearest_obj = obj

        return (nearest_obj, nearest_obj_dist)

    def _trace_ray(self, ray, depth, from_inside=False):
        """Returns the color evaluated by a given ray."""
        color = Color(0, 0, 0)

        if depth > self.max_depth:
            return color
        (nearest_obj, nearest_obj_dist) = self._nearest_obj(ray)
        if not nearest_obj:
            return color

        pos = ray.origin + ray.direction * nearest_obj_dist
        col = nearest_obj.color_at(pos)
        norm = nearest_obj.normal_at(pos)
        norm = -norm if from_inside else norm
        pos += norm * Engine.BIAS

        for light in self.scene.lights:
            color = light.affect(
                color, col, pos, norm, ray, nearest_obj, self.scene.objects
            )

        if nearest_obj.material.reflection_rate:
            color += (
                col
                * self._trace_ray(Ray(pos, norm.reflect(-ray.direction)), depth + 1)
                * nearest_obj.material.reflection_rate
            )

        return color
