# Este exemplo apresenta uma aplicação completa de OpenGL, que renderiza um quadrado e um triângulo na tela.
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

Window = None
Shader_programm = None
Vao_quadrado = None
Vao_triangulo = None
WIDTH = 800
HEIGHT = 600

def redimensionaCallback(window, w, h):
    global WIDTH, HEIGHT
    WIDTH = w
    HEIGHT = h

def inicializaOpenGL():
    global Window, WIDTH, HEIGHT

    # Inicializa GLFW
    glfw.init()

    # Criação de uma janela
    Window = glfw.create_window(WIDTH, HEIGHT, "Exemplo - renderização de um triângulo", None, None)
    if not Window:
        glfw.terminate()
        exit()

    glfw.set_window_size_callback(Window, redimensionaCallback)
    glfw.make_context_current(Window)

    print("Placa de vídeo: ",OpenGL.GL.glGetString(OpenGL.GL.GL_RENDERER))
    print("Versão do OpenGL: ",OpenGL.GL.glGetString(OpenGL.GL.GL_VERSION))

def inicializaTriangulo():
    global Vao_triangulo

    # VAO do triângulo
    Vao_triangulo = glGenVertexArrays(1)
    glBindVertexArray(Vao_triangulo)

    # VBO dos vértices
    points = [
        0.0, -0.5, 0.0,  # canto inferior direito
        0.5, -1.0, 0.0,  # canto inferior esquerdo
        -0.5, -1.0, 0.0   # canto superior central
    ]

    points = np.array(points, dtype=np.float32)

    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    # VBO das cores
    cores = [
        1.0, 0.0, 0.0,  # vermelho
        0.0, 1.0, 0.0,  # verde
        0.0, 0.0, 1.0  # azul
    ]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaQuadrado():
    global Vao_quadrado
    # Vao do quadrado
    Vao_quadrado = glGenVertexArrays(1)
    glBindVertexArray(Vao_quadrado)

    # VBO dos vértices do quadrado
    points = [
        # triângulo 1
        0.5, 0.5, 0.0,  # vertice superior direito
        0.5, -0.5, 0.0,  # vertice inferior direito
        -0.5, -0.5, 0.0,  # vertice inferior esquerdo
        # triângulo 2
        -0.5, 0.5, 0.0,  # vertice superior esquerdo
        0.5, 0.5, 0.0,  # vertice superior direito
        -0.5, -0.5, 0.0  # vertice inferior esquerdo
    ]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    # VBO das cores
    cores = [
        # triângulo 1
        1.0, 1.0, 0.0,  # amarelo
        0.0, 1.0, 1.0,  # ciano
        1.0, 0.0, 1.0,  # magenta
        # triângulo 2
        0.0, 1.0, 1.0,  # ciano
        1.0, 1.0, 0.0,  # amarelo
        1.0, 0.0, 1.0,  # magenta
    ]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaShaders():
    global Shader_programm
    # Especificação do Vertex Shader:
    vertex_shader = """
        #version 400
        layout(location = 0) in vec3 vertex_posicao;
        layout(location = 1) in vec3 vertex_cores;
        out vec3 cores;
        void main () {
            cores = vertex_cores;
            gl_Position = vec4 (vertex_posicao.y, vertex_posicao.x, vertex_posicao.z, 1.0);
        }
    """
    vs = OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER)
    if not glGetShaderiv(vs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(vs, 512, None)
        print("Erro no vertex shader:\n", infoLog)

    # Especificação do Fragment Shader:
    fragment_shader = """
        #version 400
        in vec3 cores;
        out vec4 frag_colour;
        void main () {
            frag_colour = vec4 (cores, 1.0);
        }
    """
    fs = OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    if not glGetShaderiv(fs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(fs, 512, None)
        print("Erro no fragment shader:\n", infoLog)

    # Especificação do Shader Programm:
    Shader_programm = OpenGL.GL.shaders.compileProgram(vs, fs)
    if not glGetProgramiv(Shader_programm, GL_LINK_STATUS):
        infoLog = glGetProgramInfoLog(Shader_programm, 512, None)
        print("Erro na linkagem do shader:\n", infoLog)

    glDeleteShader(vs)
    glDeleteShader(fs)

def inicializaRenderizacao():
    global Window, Shader_programm, Vao, WIDTH, HEIGHT

    while not glfw.window_should_close(Window):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glViewport(0, 0, WIDTH, HEIGHT)

        glUseProgram(Shader_programm) # ativa o shader

        # desenha o quadrado
        glBindVertexArray(Vao_quadrado)
        glDrawArrays(GL_TRIANGLES, 0, 6)

        # desenha o triângulo
        glBindVertexArray(Vao_triangulo)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.poll_events() # recebe eventos de mouse e teclado

        glfw.swap_buffers(Window) # realiza a troca de buffers para renderizar o que foi desenhado acima

        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_ESCAPE)): # trata os eventos de mouse e teclado
            glfw.set_window_should_close(Window, True)

    glfw.terminate()

# Função principal
def main():
    inicializaOpenGL()
    inicializaQuadrado() # modelagem do quadrado
    inicializaTriangulo() # modelagem do triângulo
    inicializaShaders()
    inicializaRenderizacao()

if __name__ == "__main__":
    main()
