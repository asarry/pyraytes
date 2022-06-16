#!/usr/bin/python3

from maths.vector3d import Vector3D
from rendering.camera import Camera
from rendering.color import Color
from rendering.engine import Engine
from rendering.image import Image
from rendering.lights import AmbientLight, DirectionalLight, PointLight
from rendering.material import CheckeredMaterial, Material
from rendering.objects import Plane, Sphere
from rendering.scene import Scene

BLACK = Color(0, 0, 0)
WHITE = Color(1, 1, 1)
RED = Color(1, 0, 0)
GREEN = Color(0, 1, 0)
BLUE = Color(0, 0, 1)
YELLOW = Color(1, 1, 0)
MAGENTA = Color(1, 0, 1)
CYAN = Color(0, 1, 1)

if __name__ == "__main__":
    image = Image(2000, 2000, BLACK)
    scene = Scene()

    scene.objects.append(
        Plane(
            CheckeredMaterial(WHITE, BLACK, 1, 0.1, 1, 0.3, 200), Vector3D(0, 1, 0), 0
        )
    )
    scene.objects.append(
        Sphere(Material(MAGENTA, 1, 1, 8, 0.5), Vector3D(0, 250, 750), 250)
    )
    scene.objects.append(
        Sphere(Material(YELLOW, 1, 1, 8, 0.5), Vector3D(200, 150, 0), 100)
    )
    scene.objects.append(
        Sphere(Material(CYAN, 1, 1, 8, 0.5), Vector3D(-150, 150, 50), 50)
    )

    scene.lights.append(AmbientLight(Color(0.0001, 0.0001, 0.0001)))
    scene.lights.append(
        DirectionalLight(Color(0.1, 0.1, 0.1), Vector3D(1, -1, 1).normalize(), 750)
    )
    scene.lights.append(
        PointLight(
            Color(0.1, 0.1, 0.1),
            Vector3D(0, 300, 0).normalize(),
            100,
            (0.0001, 0.0001, 0.0001),
        )
    )

    camera = Camera.create_lookat(
        Vector3D(0, 250, -750),
        Vector3D(0, 150, 100),
        Vector3D(0, 1, 0),
        image.width / image.height,
    )

    engine = Engine(camera, scene, image, 4, 8)
    engine.render()
    image.save_as_ppm("image.ppm")
