// Verifica se estamos usando o GLSL ES (OpenGL ES), definindo a precisão para variáveis de ponto flutuante.
#ifdef GL_ES
precision mediump float;
#endif

// Declaração de variáveis uniformes, fornecidas pela aplicação (como a resolução da tela, posição do mouse e tempo).
uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

// Função para gerar números pseudoaleatórios a partir de uma posição (vec2 st).
float random(vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898, 78.233))) * 43758.5453123);
}

void main() {
    // Calcula as coordenadas normalizadas (0.0 a 1.0) do fragmento em relação à resolução da tela.
    vec2 st = gl_FragCoord.xy / u_resolution.xy;

    // Escala o sistema de coordenadas por 10.
    st *= 10.0;

    // Obtém as coordenadas inteiras (parte inteira) e fracionárias da posição escalada.
    vec2 ipos = floor(st);  // Coordenadas inteiras
    vec2 fpos = fract(st);  // Coordenadas fracionárias

    // Atribui um valor aleatório com base nas coordenadas inteiras à cor.
    vec3 color = vec3(random(ipos));

    // Descomente para ver a grade subdividida (coordenadas fracionárias).
    // color = vec3(fpos, 0.0);

    // Define a cor do fragmento.
    gl_FragColor = vec4(color, 1.0);
}
