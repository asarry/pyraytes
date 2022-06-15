class Scene:
    """A Scene contains multiple objects as well as multiple lights."""

    def __init__(self, objects=[], lights=[]):
        self.objects = objects
        self.lights = lights
