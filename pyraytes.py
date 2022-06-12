#!/usr/bin/python3

from maths.vector3d import Vector3D
from rendering.camera import Camera
from rendering.engine import Engine
from rendering.image import Image
from rendering.light import AmbientLight, DirectionalLight
from rendering.objects import CheckerboardUpPlane, Material, Sphere
from rendering.scene import Scene
from rendering.color import Color

BLACK = Color(0, 0, 0)
WHITE = Color(1, 1, 1)
RED = Color(1, 0, 0)
GREEN = Color(0, 1, 0)
BLUE = Color(0, 0, 1)
YELLOW = Color(1, 1, 0)
MAGENTA = Color(1, 0, 1)
CYAN = Color(0, 1, 1)

if __name__ == "__main__":
    f = Image(2000, 2000, BLACK)
    scene = Scene()

    scene.objects.append(
        CheckerboardUpPlane(Material(WHITE, 1, 0.1, 1, 0.3), 200, 200, BLACK)
    )
    scene.objects.append(
        Sphere(Material(RED, 1, 1, 8, 0.5), Vector3D(140, -100, 0), 100)
    )
    scene.objects.append(
        Sphere(Material(YELLOW, 1, 1, 8, 0.5), Vector3D(0, 0, 450), 200)
    )
    scene.objects.append(
        Sphere(Material(GREEN, 1, 1, 8, 0.5), Vector3D(-140, -90, 0), 110)
    )

    scene.lights.append(AmbientLight(Color(0.05, 0.05, 0.05)))
    scene.lights.append(
        DirectionalLight(Color(0.1, 0.1, 0.1), Vector3D(1, -1, 1).normalize(), 6)
    )

    cam = Camera.create_lookat(
        Vector3D(0, 324, -532),
        Vector3D(0, 0, 80),
        Vector3D(0, 1, 0),
        f.width / f.height,
    )

    eng = Engine(cam, scene, f, 4, 8)

    print("Rendering...")
    eng.render()
    print("Done! Saving...")

    f.save_ppm("result.ppm", f)
