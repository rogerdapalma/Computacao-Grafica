import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import time

Window = None
Shader_programm = None
Vao = None
WIDTH = 800
HEIGHT = 800
angle = 0.0  # Ângulo de rotação inicial

def redimensionaCallback(window, w, h):
    global WIDTH, HEIGHT
    WIDTH = w
    HEIGHT = h

def inicializaOpenGL():
    global Window, WIDTH, HEIGHT

    # Inicializa GLFW
    glfw.init()

    # Criação de uma janela
    Window = glfw.create_window(WIDTH, HEIGHT, "Exemplo - renderização de um quadrado com transformações geométricas", None, None)
    if not Window:
        glfw.terminate()
        exit()

    glfw.set_window_size_callback(Window, redimensionaCallback)
    glfw.make_context_current(Window)

    print("Placa de vídeo: ",OpenGL.GL.glGetString(OpenGL.GL.GL_RENDERER))
    print("Versão do OpenGL: ",OpenGL.GL.glGetString(OpenGL.GL.GL_VERSION))

def inicializaObjetos():
    global Vao
    # Vao do quadrado
    Vao = glGenVertexArrays(1)
    glBindVertexArray(Vao)

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
        layout(location = 0) in vec3 vertex_posicao; //vem da modelagem de um objeto no python
        layout(location = 1) in vec3 vertex_cores; //vem da modelagem de um objeto no python
        uniform mat4 matriz; //matriz 4x4 vem do python, pois ela tem o modificador "uniform"
        out vec3 cores;
        void main () {
            cores = vertex_cores;
            //            MATRIZ DE TRANSFORMAÇÃO X     MODELO DO OBJETO
            gl_Position = matriz                  *     vec4 (vertex_posicao, 1.0);
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

def transformacaoGeometrica(tx, ty, tz, rx, ry, rz, sx, sy, sz):
    global angle
    # Matriz de translação
    translacao = np.array([
        [1.0, 0.0, 0.0, tx],
        [0.0, 1.0, 0.0, ty],
        [0.0, 0.0, 1.0, tz], 
        [0.0, 0.0, 0.0, 1.0]], np.float32)

    # Matriz de rotação em Z (eixo vertical)
    angulo = np.radians(angle)  # Usamos a variável angle para controlar a rotação
    cos = np.cos(angulo)
    sen = np.sin(angulo)
    rotacaoZ = np.array([
        [cos, -sen, 0.0, 0.0],
        [sen, cos, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    # Matriz de escala
    escala = np.array([
        [sx, 0.0, 0.0, 0.0],
        [0.0, sy, 0.0, 0.0],
        [0.0, 0.0, sz, 0.0], 
        [0.0, 0.0, 0.0, 1.0]], np.float32)

    # Combinação das transformações, multiplicando as matrizes
    transformacao = (escala.dot(rotacaoZ.dot(translacao)))

    # Passamos a matriz para o Vertex Shader
    transformLoc = glGetUniformLocation(Shader_programm, "matriz")
    glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transformacao)

def inicializaRenderizacao():
    global Window, Shader_programm, Vao, WIDTH, HEIGHT, angle

    while not glfw.window_should_close(Window):
        # Limpa a tela
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glViewport(0, 0, WIDTH, HEIGHT)

        # Ativa o shader
        glUseProgram(Shader_programm) 

        # Ativa o modelo de objeto a ser renderizado (quadrado)
        glBindVertexArray(Vao) 

        # Configura o valor da variável "matriz" do shader, que corresponde a transformações geométricas
        # Chamamos transformacaoGeometrica com um ângulo de rotação crescente para fazer o quadrado girar
        transformacaoGeometrica(0.0, 0.0, 0.0, 0.0, 0.0, angle, 0.25, 0.5, 1.0)
        glDrawArrays(GL_TRIANGLES, 0, 6)  # Renderiza o objeto (quadrado)

        angle += 1.0  # Aumenta o ângulo para fazer a rotação

        glfw.poll_events()

        glfw.swap_buffers(Window)
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_ESCAPE)):
            glfw.set_window_should_close(Window, True)
    
    glfw.terminate()

# Função principal
def main():
    inicializaOpenGL()
    inicializaObjetos()
    inicializaShaders()
    inicializaRenderizacao()

if __name__ == "__main__":
    main()
