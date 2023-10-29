#ifdef GL_ES
precision mediump float;
#endif
uniform vec2 u_resolution;

float plota(vec2 st, float pct){
    float v1 = smoothstep(pct - 0.02, pct, st.y);
    float v2 = smoothstep(pct, pct + 0.02, st.y);
    return v1 - v2;
}

void main() {
    vec2 st = gl_FragCoord.xy / u_resolution;
    st *= 4.0; // aumenta a área de visualização
    st -= 2.0; // desloca o gráfico da função

    // Cálculo das duas ondas
    float y1 = sin(5.0 * st.x);
    float y2 = sin(5.0 * st.x + 1.0);

    // Combina as duas ondas
    float combinedWave = (y1 + y2) * 0.5;

    // Ajusta a cor para vermelho neon
    vec3 color = vec3(1.0, 0.0, 0.0);

    // Desenha a função utilizando a função plota
    float value = plota(st, combinedWave);
    color *= value;

    gl_FragColor = vec4(color, 1.0);
}
