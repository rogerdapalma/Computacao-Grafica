//QUESTAO D
#ifdef GL_ES
precision mediump float;
#endif
uniform vec2 u_resolution;

void main() {
    // Normalizamos a posição do pixel na tela (st)
    vec2 st = gl_FragCoord.xy / u_resolution;

    // Definimos as cores com base na coordenada x normalizada (st.x)
    vec3 color;
    if (st.x < 0.5) {
        // Parte esquerda: Verde
        color = vec3(0.0, 0.49804, 0.0);
    } else {
        // Parte direita: Rosa
        color = vec3(0.9922, 0.50196, 0.8);
    }

    gl_FragColor = vec4(color, 1.0);
}