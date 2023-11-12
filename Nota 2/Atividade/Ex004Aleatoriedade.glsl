// Autor: @patriciogv - 2015
// Título: DeFrag

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
// Compartilho esta obra para fins educacionais e você pode vinculá-la
// através de uma URL, atribuição adequada e captura de tela não modificada,
// como parte de seu material educacional. Se essas condições forem muito restritivas,
// entre em contato comigo e definitivamente resolveremos isso.

// Declaração de variáveis uniformes, fornecidas pela aplicação (como a resolução da tela, posição do mouse e tempo).
uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

// Função para gerar números pseudoaleatórios a partir de uma coordenada x.
float random(in float x) { return fract(sin(x)*1e4); }

// Função para gerar números pseudoaleatórios a partir de uma coordenada 2D (_st).
float random(in vec2 _st) { return fract(sin(dot(_st.xy, vec2(12.9898, 78.233))) * 43758.5453123); }

void main() {
    // Calcula as coordenadas normalizadas (0.0 a 1.0) do fragmento em relação à resolução da tela.
    vec2 st = gl_FragCoord.xy / u_resolution.xy;

    // Ajusta as coordenadas para considerar a proporção da resolução da tela.
    st.x *= u_resolution.x / u_resolution.y;

    // Define as dimensões da grade.
    vec2 grid = vec2(100.0, 50.0);
    st *= grid;

    // Coordenadas inteiras (parte inteira) da posição escalada.
    vec2 ipos = floor(st);

    // Velocidade baseada no tempo.
    vec2 vel = floor(vec2(u_time * 10.0));

    // Direção da velocidade.
    vel *= vec2(-1.0, 0.0);

    // Direção oposta em função da linha (y).
    vel *= (step(1.0, mod(ipos.y, 2.0)) - 0.5) * 2.0;

    // Velocidade aleatória.
    vel *= random(ipos.y);

    // Porcentagem do total de células na grade.
    float totalCells = grid.x * grid.y;
    float t = mod(u_time * max(grid.x, grid.y) + floor(1.0 + u_time * u_mouse.y), totalCells);
    vec2 head = vec2(mod(t, grid.x), floor(t / grid.x));

    // Offset para melhor posicionamento.
    vec2 offset = vec2(0.1, 0.0);

    // Cor inicial.
    vec3 color = vec3(1.0);

    // Atribui um valor aleatório baseado nas coordenadas inteiras com a velocidade e o offset.
    color.r *= random(floor(st + vel + offset));
    color.g *= random(floor(st + vel));
    color.b *= random(floor(st + vel - offset));

    // Suaviza as cores.
    color = smoothstep(0.0, 0.5 + u_mouse.x / u_resolution.x * 0.5, color * color);

    // Aplica um limiar para obter um efeito "threshold".
    color = step(0.5 + u_mouse.x / u_resolution.x * 0.5, color);

    // Margem (borda) para um efeito adicional.
    color *= step(0.1, fract(st.x + vel.x)) * step(0.1, fract(st.y + vel.y));

    // Define a cor do fragmento.
    gl_FragColor = vec4(1.0 - color, 1.0);
}
