from vbo import VBO
from shader_program import ShaderProgram

class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program = self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])

        # custom vaos
        self.vaos['cat'] = self.get_vao(
            program = self.program.programs['default'],
            vbo = self.vbo.vbos['cat'])

        self.vaos['cushiony_thingy'] = self.get_vao(
            program = self.program.programs['default'],
            vbo = self.vbo.vbos['cushiony_thingy'])

        self.vaos['tree'] = self.get_vao(
            program = self.program.programs['default'],
            vbo = self.vbo.vbos['tree'])

        # skybox vao
        self.vaos['advanced_skybox'] = self.get_vao(
            program = self.program.programs['advanced_skybox'],
            vbo = self.vbo.vbos['advanced_skybox'])
        # shadow vaos
        self.vaos['shadow_cube'] = self.get_vao(
            program = self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['cube'])

        self.vaos['shadow_cat'] = self.get_vao(
            program = self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['cat'])

        self.vaos['shadow_cushiony_thingy'] = self.get_vao(
            program = self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['cushiony_thingy'])

        self.vaos['shadow_tree'] = self.get_vao(
            program = self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['tree'])

        # Add plane VAO
        self.vaos['plane'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['plane']
        )
        self.vaos['shadow_plane'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['plane']
        )

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()