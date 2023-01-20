#version 300 es
precision mediump float;
uniform sampler2D Texture;

out vec4 color;
in vec2 v_text;
uniform float time;
float random(vec2 st)
{
    return fract(sin(dot(st.xy, vec2(12.9898,78.233))) * 43758.5453123);
}
void main() {
    vec2 v_text2 = pow(v_text,vec2(2.,2.)) - 0.1*sin(1.2*time)-0.3*cos(time+1.);
    color = vec4(texture(Texture, v_text2).rgb, 1.0);
}