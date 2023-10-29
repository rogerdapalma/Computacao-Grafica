//QUESTAO C
#ifdef GL_ES
precision mediump float;
#endif
uniform vec2 u_resolution;
uniform vec2 u_mouse;

void main() {
    // Normalizamos a posição do pixel na tela (st) e a posição do ponteiro do mouse (mouse_normalizado)
    vec2 st = gl_FragCoord.xy / u_resolution;
    vec2 mouse_normalizado = u_mouse / u_resolution;

    // Interpolação entre branco, cinza e preto com base na posição do mouse (mouse_normalizado.y)
    float t = mouse_normalizado.y;
    vec3 color = mix(vec3(1.0, 1.0, 1.0), vec3(0.5, 0.5, 0.5), t);
    color = mix(color, vec3(0.0, 0.0, 0.0), t);

    gl_FragColor = vec4(color, 1.0);
}