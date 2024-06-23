import glm


class Light:
    def __init__(self, app, toUse, pos):
        self.app = app
        if toUse:
            self.light((50, 50, 0))
        else:
            self.light(pos)

    def light(self, position):
        self.color = glm.vec3(self.app.color[0]) if self.app.is_day else glm.vec3(self.app.color[1])
        self.position = glm.vec3(position)
        self.direction = glm.vec3(0, 0, 0)
        # intensities
        self.Ia = 0.2 * self.color if self.app.is_day else 0.2 * self.color
        self.Id = 0.6 * self.color if self.app.is_day else 0.6 * self.color
        self.Is = 1.2 * self.color if self.app.is_day else 1.2 * self.color
        # view matrix
        self.m_view_light = self.get_view_matrix()
        
    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))
