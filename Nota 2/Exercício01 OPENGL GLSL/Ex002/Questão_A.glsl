#ifdef GL_ES
precision mediump float;
#endif
uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

void main() {
    // Normaliza as coordenadas do fragmento para o intervalo [0, 1]
    vec2 st = gl_FragCoord.xy / u_resolution;

    // Inicializa a variável pct (porcentagem) como 1.0
    float pct = 1.0;

    // Calcula a distância do fragmento ao centro (0.5, 0.5)
    pct -= step(0.5, distance(st, vec2(0.5)));

    // Define a cor do fragmento com base na pct (1.0 ou 0.0)
    vec3 color = vec3(pct);

    // Define a cor final do fragmento com opacidade 1.0
    gl_FragColor = vec4(color, 1.0);
}
