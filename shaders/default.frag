#version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;
in vec4 shadowCoord;

struct Light {
    vec3 position;
    vec3 Ia, Id, Is;
};

uniform Light light;
uniform sampler2D u_texture_0;
uniform vec3 camPos;
uniform sampler2DShadow shadowMap;
uniform vec2 u_resolution;

float lookup(float ox, float oy) {
    vec2 pixelOffset = 1 / u_resolution;
    return textureProj(shadowMap, shadowCoord + vec4(ox * pixelOffset.x * shadowCoord.w, oy * pixelOffset.y * shadowCoord.w, 0.0, 0.0));
}

float getSoftShadowX16() {
    float shadow;
    float shadowWidth = 1.0;
    float endPoint = shadowWidth * 1.5;
    for (float y = -endPoint; y <= endPoint; y+=shadowWidth) {
        for (float x = -endPoint; x <= endPoint; x+= shadowWidth) {
           shadow += lookup(x,y);
        }
    }
    return shadow / 16.0;
}

float getShadow() {
    float shadow = textureProj(shadowMap, shadowCoord);
    return shadow;
}

vec3 getLight(vec3 color) {
    vec3 Normal = normalize(normal);
    // ambient light
    vec3 ambient = light.Ia;

    // diffuse light
    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0,dot(lightDir, Normal));
    vec3 diffuse = diff * light.Id;

    // specular light
    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir,reflectDir), 0), 32);
    vec3 specular = spec * light.Is;

    // shadow
    float shadow = getSoftShadowX16();

    return color * (ambient + (diffuse + specular) * shadow);
}

void main() {
    float gamma = 2.2;
    vec3 color = texture(u_texture_0, uv_0).rgb;
    color = pow(color, vec3(gamma));
    color = getLight(color);
    color = pow(color, 1/vec3(gamma));
    fragColor = vec4(color,1.0);
}
