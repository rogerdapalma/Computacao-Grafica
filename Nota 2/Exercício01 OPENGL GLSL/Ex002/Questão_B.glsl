#ifdef GL_ES
precision mediump float;
#endif
uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

void main() {
    vec2 st = gl_FragCoord.xy / u_resolution.xy;
    vec3 color = vec3(1.0); // Inicialmente, configure a cor como branca

    // bottom-left
    vec2 bl = step(vec2(0.1), st);

    // top-right
    vec2 tr = step(vec2(0.1), 1.0 - st);

    // Inverta a operação AND, ou seja, faça um OR lógico para inverter as cores
    color = vec3(1.0 - bl.x * bl.y * tr.x * tr.y);

    gl_FragColor = vec4(color, 1.0);
}
