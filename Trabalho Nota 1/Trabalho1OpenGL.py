import glfw
from OpenGL.GL import *
from OpenGL.GL import shaders
import numpy as np



# Defina as coordenadas e cores para o quadrado e o triângulo
quadrado_vertices = np.array([
    # Posições       Cores
    -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,  # Inferior esquerdo (vermelho)
     0.5, -0.5, 0.0, 0.0, 1.0, 0.0,  # Inferior direito (verde)
     0.5,  0.5, 0.0, 0.0, 0.0, 1.0,  # Superior direito (azul)
    -0.5,  0.5, 0.0, 1.0, 1.0, 0.0   # Superior esquerdo (amarelo)
], dtype=np.float32)

triangulo_vertices = np.array([
    # Posições       Cores
     0.0,  0.5, 0.0, 1.0, 0.0, 0.0,  # Superior (vermelho)
    -0.5, -0.5, 0.0, 0.0, 1.0, 0.0,  # Inferior esquerdo (verde)
     0.5, -0.5, 0.0, 0.0, 0.0, 1.0   # Inferior direito (azul)
], dtype=np.float32)

# Defina os shaders (vertex e fragment shaders)
vertex_shader = """
# version 330 core
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_color;
out vec3 color;
void main()
{
    gl_Position = vec4(a_position, 1.0);
    color = a_color;
}
"""

fragment_shader = """
# version 330 core
in vec3 color;
out vec4 fragColor;
void main()
{
    fragColor = vec4(color, 1.0);
}
"""

# Função para inicializar o OpenGL
def inicializaOpenGL():
    if not glfw.init():
        return
    # Configuração das janelas
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    # Criação da janela
    window = glfw.create_window(800, 600, "Quadrado e Triângulo", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    return window

# Função para inicializar os shaders
def inicializaShaders():
    shader = OpenGL.GL.shaders.compileProgram(
        OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
        OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    )
    glUseProgram(shader)
    return shader

# Função para criar um VAO e VBO para um objeto (quadrado ou triângulo)
def criaVAO(vertices):
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
    # Posições
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)
    # Cores
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(1)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)
    return VAO

# Função para renderizar um objeto
def renderizaObjeto(VAO):
    glBindVertexArray(VAO)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray(0)

# Função principal
def main():
    window = inicializaOpenGL()
    if not window:
        return
    shader = inicializaShaders()
    
    VAO_quadrado = criaVAO(quadrado_vertices)
    VAO_triangulo = criaVAO(triangulo_vertices)
    
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Renderiza o quadrado
        glBindVertexArray(VAO_quadrado)
        glDrawArrays(GL_TRIANGLE_FAN, 0, 4)
        
        # Renderiza o triângulo
        glBindVertexArray(VAO_triangulo)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        
        glBindVertexArray(0)
        glfw.swap_buffers(window)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
