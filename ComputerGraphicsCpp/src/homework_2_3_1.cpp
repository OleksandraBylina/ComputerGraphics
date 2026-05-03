#include <fstream>
#include <iostream>
#include <sstream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>

#define STB_IMAGE_IMPLEMENTATION
#include "../external/stb_image.h"

#include "shader_utils.h"

GLuint loadTexture(const char* path)
{
    GLuint texture;

    glGenTextures(1, &texture);
    glBindTexture(GL_TEXTURE_2D, texture);

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

    int width;
    int height;
    int channels;

    stbi_set_flip_vertically_on_load(true);

    unsigned char* data = stbi_load(path, &width, &height, &channels, 0);

    if (data)
    {
        GLenum format = GL_RGB;

        if (channels == 1)
        {
            format = GL_RED;
        }
        else if (channels == 3)
        {
            format = GL_RGB;
        }
        else if (channels == 4)
        {
            format = GL_RGBA;
        }

        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            format,
            width,
            height,
            0,
            format,
            GL_UNSIGNED_BYTE,
            data
        );

        glGenerateMipmap(GL_TEXTURE_2D);
    }
    else
    {
        std::cout << "Failed to load texture: " << path << std::endl;
    }

    stbi_image_free(data);

    return texture;
}

int main(void)
{
    GLFWwindow* window;

    if (!glfwInit())
        return -1;

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);

    window = glfwCreateWindow(640, 480, "Hello World", NULL, NULL);

    if (!window)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);

    if (!gladLoadGLLoader((GLADloadproc) glfwGetProcAddress))
    {
        std::cout << "Failed to initialize GLAD" << std::endl;
        glfwTerminate();
        return -1;
    }

    glClearColor(1.0, 1.0, 1.0, 1.0);

    std::string vertexShaderName = "/Users/oleksandrabylina/Documents/University/ComputerGraphics/ComputerGraphicsCpp/src/res/shaders/triangle.vert";
    std::string fragmentShaderName = "/Users/oleksandrabylina/Documents/University/ComputerGraphics/ComputerGraphicsCpp/src/res/shaders/triangle.frag";

    GLuint shaderProgram = createProgram(
        vertexShaderName,
        fragmentShaderName
    );

    glUseProgram(shaderProgram);
    glUniform1i(glGetUniformLocation(shaderProgram, "texture1"), 0);

    GLuint texture1 = loadTexture("/Users/oleksandrabylina/Documents/University/ComputerGraphics/ComputerGraphicsCpp/src/textures/pg-10.jpg");
    GLuint texture2 = loadTexture("/Users/oleksandrabylina/Documents/University/ComputerGraphics/ComputerGraphicsCpp/src/textures/WildRat.jpg");
    GLuint texture3 = loadTexture("/Users/oleksandrabylina/Documents/University/ComputerGraphics/ComputerGraphicsCpp/src/textures/images.jpeg");

    float vertices[] = {
        -0.9f,  0.6f,   0.0f, 1.0f,
        -0.4f,  0.6f,   1.0f, 1.0f,
        -0.9f,  0.2f,   0.0f, 0.0f,

        -0.4f,  0.6f,   1.0f, 1.0f,
        -0.4f,  0.2f,   1.0f, 0.0f,
        -0.9f,  0.2f,   0.0f, 0.0f,

         0.4f,  0.6f,   0.0f, 1.0f,
         0.9f,  0.6f,   1.0f, 1.0f,
         0.4f,  0.2f,   0.0f, 0.0f,

         0.9f,  0.6f,   1.0f, 1.0f,
         0.9f,  0.2f,   1.0f, 0.0f,
         0.4f,  0.2f,   0.0f, 0.0f,

        -0.35f, -0.2f,   0.0f, 1.0f,
        0.35f, -0.2f,   1.0f, 1.0f,
        -0.35f, -0.55f,  0.0f, 0.0f,

        0.35f, -0.2f,   1.0f, 1.0f,
        0.35f, -0.55f,  1.0f, 0.0f,
        -0.35f, -0.55f,  0.0f, 0.0f
    };

    GLuint VBO;
    GLuint VAO;

    glGenBuffers(1, &VBO);
    glGenVertexArrays(1, &VAO);

    glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    GLuint posAttribLocation = glGetAttribLocation(shaderProgram, "aPos");

    glVertexAttribPointer(
        posAttribLocation,
        2,
        GL_FLOAT,
        GL_FALSE,
        4 * sizeof(float),
        (void*)0
    );

    glEnableVertexAttribArray(posAttribLocation);

    GLuint texCoordAttribLocation = glGetAttribLocation(shaderProgram, "aTexCoord");

    glVertexAttribPointer(
        texCoordAttribLocation,
        2,
        GL_FLOAT,
        GL_FALSE,
        4 * sizeof(float),
        (void*)(2 * sizeof(float))
    );

    glEnableVertexAttribArray(texCoordAttribLocation);

    glBindVertexArray(0);

    do
    {
        glClear(GL_COLOR_BUFFER_BIT);

        glUseProgram(shaderProgram);
        glBindVertexArray(VAO);

        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D, texture1);
        glDrawArrays(GL_TRIANGLES, 0, 6);

        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D, texture2);
        glDrawArrays(GL_TRIANGLES, 6, 6);

        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D, texture3);
        glDrawArrays(GL_TRIANGLES, 12, 6);

        glfwSwapBuffers(window);

        glfwPollEvents();

    } while (!glfwWindowShouldClose(window) && !glfwGetKey(window, GLFW_KEY_ESCAPE));

    glDeleteBuffers(1, &VBO);
    glDeleteVertexArrays(1, &VAO);

    glDeleteTextures(1, &texture1);
    glDeleteTextures(1, &texture2);
    glDeleteTextures(1, &texture3);

    glDeleteProgram(shaderProgram);

    glfwTerminate();

    return 0;
}