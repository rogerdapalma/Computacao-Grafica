// Autor: @patriciogv - 2015
// Título: Ikeda Data Stream

// Verifica se estamos usando o GLSL ES (OpenGL ES), definindo a precisão para variáveis de ponto flutuante.
#ifdef GL_ES
precision mediump float;
#endif

// Aviso de direitos autorais
// Copyright (c) Patricio Gonzalez Vivo, 2015 - http://patriciogonzalezvivo.com/
// Sou o único proprietário dos direitos autorais desta obra.
//
// Você não pode hospedar, exibir, distribuir ou compartilhar esta obra de forma alguma,
// incluindo fisicamente e digitalmente. Você não pode usar esta obra em nenhum
// produto, site ou projeto comercial ou não comercial. Você não pode
// vender esta obra e não pode criar NFTs (tokens não fungíveis) com ela.
// Compartilho esta obra para fins educacionais, e você pode vinculá-la
// através de uma URL, atribuição adequada e captura de tela não modificada,
// como parte de seu material educacional. Se essas condições forem muito restritivas,
// entre em contato comigo e definitivamente resolveremos isso.

// Declaração de variáveis uniformes, fornecidas pela aplicação (como a resolução da tela, posição do mouse e tempo).
uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

// Função para gerar números pseudoaleatórios a partir de uma coordenada x.
float random(in float x) {
    return fract(sin(x) * 1e4);
}

// Função para gerar números pseudoaleatórios a partir de uma coordenada 2D (_st).
float random(in vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898, 78.233))) * 43758.5453123);
}

// Função para criar um padrão baseado em coordenadas e uma velocidade.
float pattern(vec2 st, vec2 v, float t) {
    vec2 p = floor(st + v);
    return step(t, random(100. + p * 0.000001) + random(p.x) * 0.5);
}

void main() {
    // Calcula as coordenadas normalizadas (0.0 a 1.0) do fragmento em relação à resolução da tela.
    vec2 st = gl_FragCoord.xy / u_resolution.xy;

    // Ajusta as coordenadas para considerar a proporção da resolução da tela.
    st.x *= u_resolution.x / u_resolution.y;

    // Define as dimensões da grade.
    vec2 grid = vec2(100.0, 50.0);
    st *= grid;

    // Coordenadas inteiras (parte inteira) e fracionárias da posição escalada.
    vec2 ipos = floor(st);
    vec2 fpos = fract(st);

    // Velocidade baseada no tempo.
    vec2 vel = vec2(u_time * 2.0 * max(grid.x, grid.y));

    // Direção da velocidade e multiplicador aleatório.
    vel *= vec2(-1.0, 0.0) * random(1.0 + ipos.y);

    // Offset para melhor posicionamento.
    vec2 offset = vec2(0.1, 0.0);

    // Cor inicial.
    vec3 color = vec3(0.0);

    // Atribui um valor aleatório baseado nas coordenadas com a velocidade e o offset para cada componente de cor.
    color.r = pattern(st + offset, vel, 0.5 + u_mouse.x / u_resolution.x);
    color.g = pattern(st, vel, 0.5 + u_mouse.x / u_resolution.x);
    color.b = pattern(st - offset, vel, 0.5 + u_mouse.x / u_resolution.x);

    // Margens para adicionar uma borda.
    color *= step(0.2, fpos.y);

    // Define a cor do fragmento.
    gl_FragColor = vec4(1.0 - color, 1.0);
}
