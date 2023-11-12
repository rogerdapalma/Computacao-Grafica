// Autor: @patriciogv - 2015
// Título: Truchet - 10 print

// Verifica se estamos usando o GLSL ES (OpenGL ES), definindo a precisão para variáveis de ponto flutuante.
#ifdef GL_ES
precision mediump float;
#endif

// Definição da constante PI.
#define PI 3.14159265358979323846

// Declaração de variáveis uniformes, fornecidas pela aplicação (como a resolução da tela, posição do mouse e tempo).
uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

// Função para gerar números pseudoaleatórios a partir de uma posição (vec2 _st).
float random(in vec2 _st) {
    return fract(sin(dot(_st.xy, vec2(12.9898, 78.233))) * 43758.5453123);
}

// Função que implementa um padrão Truchet, onde _index determina a orientação do padrão.
vec2 truchetPattern(in vec2 _st, in float _index){
    _index = fract(((_index-0.5)*2.0));
    if (_index > 0.75) {
        _st = vec2(1.0) - _st;
    } else if (_index > 0.5) {
        _st = vec2(1.0-_st.x, _st.y);
    } else if (_index > 0.25) {
        _st = 1.0 - vec2(1.0-_st.x, _st.y);
    }
    return _st;
}

void main() {
    // Calcula as coordenadas normalizadas (0.0 a 1.0) do fragmento em relação à resolução da tela.
    vec2 st = gl_FragCoord.xy / u_resolution.xy;

    // Escala o sistema de coordenadas por 10.
    st *= 10.0;

    // Coordenadas inteiras (parte inteira) e fracionárias da posição escalada.
    vec2 ipos = floor(st);  // Coordenadas inteiras
    vec2 fpos = fract(st);  // Coordenadas fracionárias

    // Aplica o padrão Truchet à coordenada fracionária usando um valor aleatório com base nas coordenadas inteiras.
    vec2 tile = truchetPattern(fpos, random(ipos));

    float color = 0.0;

    // Maze
    // Define a cor com base em um padrão de labirinto.
    color = smoothstep(tile.x-0.3, tile.x, tile.y) -
            smoothstep(tile.x, tile.x+0.3, tile.y);

    // Circles
    // Define a cor com base em círculos concêntricos.
    // color = (step(length(tile),0.6) -
    //          step(length(tile),0.4) ) +
    //         (step(length(tile-vec2(1.)),0.6) -
    //          step(length(tile-vec2(1.)),0.4) );

    // Truchet (2 triângulos)
    // Define a cor usando o padrão Truchet (2 triângulos).
    // color = step(tile.x, tile.y);

    // Define a cor do fragmento.
    gl_FragColor = vec4(vec3(color), 1.0);
}
