#version 300 es
precision mediump float;
uniform sampler2D Texture;

out vec4 Color;
in vec2 v_text;
uniform float time;
float random(vec2 st)
{
    return fract(sin(dot(st.xy, vec2(12.9898,78.233))) * 43758.5453123);
}
void main() {
  vec2 offset = v_text - vec2(0.5,0.5);
  float offset_size = offset.x*offset.x + offset.y*offset.y;
  Color.rgb = vec3(texture(Texture,v_text)) + (vec3(2)*sin(time)*vec3(offset_size))%1.;
}