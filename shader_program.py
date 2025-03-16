class ShaderProgram:
    def __init__(self, ctx):
        self.ctx = ctx
        self.programs = {}
        self.programs['default'] = self.get_program('default')
        self.programs['advanced_skybox'] = self.get_program('skybox/advanced_skybox')

    def get_program(self, shader_program_name):
        """
        Load and compile vertex and fragment shaders from files.

        :param shader_name: The name of the shader files (without extension).
        :return: The compiled shader program.
        """
        # Load the vertex shader source code from file
        with open(f'shaders/{shader_program_name}.vert') as file:
            vertex_shader = file.read()

        # Load the fragment shader source code from file
        with open(f'shaders/{shader_program_name}.frag') as file:
            fragment_shader = file.read()

        # Compile the shaders and create the shader program
        program = self.ctx.program(
            vertex_shader=vertex_shader,
            fragment_shader=fragment_shader
        )
        return program

    def destroy(self):
        [program.release() for program in self.programs.values()]