//
// Created by Олександра Биліна on 21.05.2026.
//
#include <fstream>
#include <iostream>
#include <sstream>
#include <thread>
#include <chrono>
#include <vector>
#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

#define STB_IMAGE_IMPLEMENTATION
#include "../external/stb_image.h"

#include "shader_utils.h"

float lastX = 400.0f;
float lastY = 300.0f;
bool firstMouse = true;

float yaw = -90.0f;
float pitch = 0.0f;

glm::vec3 cameraPos = glm::vec3(0.0f, 0.0f, 5.0f);
glm::vec3 cameraFront = glm::vec3(0.0f, 0.0f, -1.0f);
glm::vec3 cameraUp = glm::vec3(0.0f, 1.0f, 0.0f);

void mouse_callback(GLFWwindow* window, double xpos, double ypos)
{
    if (firstMouse)
    {
        lastX = xpos;
        lastY = ypos;
        firstMouse = false;
    }

    float xoffset = xpos - lastX;
    float yoffset = lastY - ypos;

    lastX = xpos;
    lastY = ypos;

    float sensitivity = 0.1f;

    xoffset *= sensitivity;
    yoffset *= sensitivity;

    yaw += xoffset;
    pitch += yoffset;

    if (pitch > 89.0f)
    {
        pitch = 89.0f;
    }

    if (pitch < -89.0f)
    {
        pitch = -89.0f;
    }

    glm::vec3 direction;

    direction.x = cos(glm::radians(yaw)) * cos(glm::radians(pitch));
    direction.y = sin(glm::radians(pitch));
    direction.z = sin(glm::radians(yaw)) * cos(glm::radians(pitch));

    cameraFront = glm::normalize(direction);
}

GLuint loadTexture(const char* path)
{
    GLuint texture;

    glGenTextures(1, &texture);
    glBindTexture(GL_TEXTURE_2D, texture);

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
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
        std::cout << stbi_failure_reason() << std::endl;
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
    glfwWindowHint(GLFW_STENCIL_BITS, 8);

    window = glfwCreateWindow(800, 600, "Textured Cubes", NULL, NULL);

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

    glfwSetCursorPosCallback(window, mouse_callback);
    glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);

    glViewport(0, 0, 800, 600);

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_STENCIL_TEST);

    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE);

    glClearColor(1.0, 1.0, 1.0, 1.0);

    std::string vertexShaderName = "/Users/oleksandrabylina/Documents/University/ComputerGraphics/ComputerGraphicsCpp/src/res/shaders/cube.vert";
    std::string fragmentShaderName = "/Users/oleksandrabylina/Documents/University/ComputerGraphics/ComputerGraphicsCpp/src/res/shaders/cube.frag";

    std::string outlineVertexShaderName = "/Users/oleksandrabylina/Documents/University/ComputerGraphics/ComputerGraphicsCpp/src/res/shaders/cube_outline.vert";
    std::string outlineFragmentShaderName = "/Users/oleksandrabylina/Documents/University/ComputerGraphics/ComputerGraphicsCpp/src/res/shaders/cube_outline.frag";

    GLuint shaderProgram = createProgram(
        vertexShaderName,
        fragmentShaderName
    );

    GLuint outlineShaderProgram = createProgram(
        outlineVertexShaderName,
        outlineFragmentShaderName
    );

    glUseProgram(shaderProgram);
    glUniform1i(glGetUniformLocation(shaderProgram, "texture1"), 0);

    GLuint texture1 = loadTexture("/Users/oleksandrabylina/Documents/University/ComputerGraphics/ComputerGraphicsCpp/src/textures/pg-10.jpg");

    float vertices[] = {
        -0.5f, -0.5f, -0.5f,  0.0f, 0.0f,
         0.5f, -0.5f, -0.5f,  1.0f, 0.0f,
         0.5f,  0.5f, -0.5f,  1.0f, 1.0f,
         0.5f,  0.5f, -0.5f,  1.0f, 1.0f,
        -0.5f,  0.5f, -0.5f,  0.0f, 1.0f,
        -0.5f, -0.5f, -0.5f,  0.0f, 0.0f,

        -0.5f, -0.5f,  0.5f,  0.0f, 0.0f,
         0.5f, -0.5f,  0.5f,  1.0f, 0.0f,
         0.5f,  0.5f,  0.5f,  1.0f, 1.0f,
         0.5f,  0.5f,  0.5f,  1.0f, 1.0f,
        -0.5f,  0.5f,  0.5f,  0.0f, 1.0f,
        -0.5f, -0.5f,  0.5f,  0.0f, 0.0f,

        -0.5f,  0.5f,  0.5f,  1.0f, 0.0f,
        -0.5f,  0.5f, -0.5f,  1.0f, 1.0f,
        -0.5f, -0.5f, -0.5f,  0.0f, 1.0f,
        -0.5f, -0.5f, -0.5f,  0.0f, 1.0f,
        -0.5f, -0.5f,  0.5f,  0.0f, 0.0f,
        -0.5f,  0.5f,  0.5f,  1.0f, 0.0f,

         0.5f,  0.5f,  0.5f,  1.0f, 0.0f,
         0.5f,  0.5f, -0.5f,  1.0f, 1.0f,
         0.5f, -0.5f, -0.5f,  0.0f, 1.0f,
         0.5f, -0.5f, -0.5f,  0.0f, 1.0f,
         0.5f, -0.5f,  0.5f,  0.0f, 0.0f,
         0.5f,  0.5f,  0.5f,  1.0f, 0.0f,

        -0.5f, -0.5f, -0.5f,  0.0f, 1.0f,
         0.5f, -0.5f, -0.5f,  1.0f, 1.0f,
         0.5f, -0.5f,  0.5f,  1.0f, 0.0f,
         0.5f, -0.5f,  0.5f,  1.0f, 0.0f,
        -0.5f, -0.5f,  0.5f,  0.0f, 0.0f,
        -0.5f, -0.5f, -0.5f,  0.0f, 1.0f,

        -0.5f,  0.5f, -0.5f,  0.0f, 1.0f,
         0.5f,  0.5f, -0.5f,  1.0f, 1.0f,
         0.5f,  0.5f,  0.5f,  1.0f, 0.0f,
         0.5f,  0.5f,  0.5f,  1.0f, 0.0f,
        -0.5f,  0.5f,  0.5f,  0.0f, 0.0f,
        -0.5f,  0.5f, -0.5f,  0.0f, 1.0f
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
        3,
        GL_FLOAT,
        GL_FALSE,
        5 * sizeof(float),
        (void*)0
    );

    glEnableVertexAttribArray(posAttribLocation);

    GLuint texCoordAttribLocation = glGetAttribLocation(shaderProgram, "aTexCoord");

    glVertexAttribPointer(
        texCoordAttribLocation,
        2,
        GL_FLOAT,
        GL_FALSE,
        5 * sizeof(float),
        (void*)(3 * sizeof(float))
    );

    glEnableVertexAttribArray(texCoordAttribLocation);

    glBindVertexArray(0);

    glm::vec3 cubePositions[] = {
        glm::vec3(-1.5f, 0.0f, 0.0f),
        glm::vec3(1.5f, 0.0f, -1.0f),
        glm::vec3(0.0f, 1.3f, -2.0f),
        glm::vec3(0.0f, -1.2f, -1.5f)
    };

    glm::vec3 cubeScales[] = {
        glm::vec3(0.8f, 0.8f, 0.8f),
        glm::vec3(0.5f, 1.0f, 0.5f),
        glm::vec3(0.7f, 0.7f, 0.7f),
        glm::vec3(1.0f, 0.4f, 0.6f)
    };

    int activeCube = 0;

    double lastTime = glfwGetTime();
    float activeAngle = 0.0f;
    float cameraSpeed = 2.5f;

    do
    {
        double frameStart = glfwGetTime();

        double currentTime = glfwGetTime();
        double deltaTime = currentTime - lastTime;
        lastTime = currentTime;

        float currentCameraSpeed = cameraSpeed * deltaTime;

        if (glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS)
        {
            cameraPos += currentCameraSpeed * cameraFront;
        }

        if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
        {
            cameraPos -= currentCameraSpeed * cameraFront;
        }

        if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
        {
            cameraPos -= glm::normalize(glm::cross(cameraFront, cameraUp)) * currentCameraSpeed;
        }

        if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
        {
            cameraPos += glm::normalize(glm::cross(cameraFront, cameraUp)) * currentCameraSpeed;
        }

        if (glfwGetKey(window, GLFW_KEY_SPACE) == GLFW_PRESS)
        {
            cameraPos += cameraUp * currentCameraSpeed;
        }

        if (glfwGetKey(window, GLFW_KEY_LEFT_SHIFT) == GLFW_PRESS)
        {
            cameraPos -= cameraUp * currentCameraSpeed;
        }

        if (glfwGetKey(window, GLFW_KEY_1) == GLFW_PRESS)
        {
            activeCube = 0;
        }

        if (glfwGetKey(window, GLFW_KEY_2) == GLFW_PRESS)
        {
            activeCube = 1;
        }

        if (glfwGetKey(window, GLFW_KEY_3) == GLFW_PRESS)
        {
            activeCube = 2;
        }

        if (glfwGetKey(window, GLFW_KEY_4) == GLFW_PRESS)
        {
            activeCube = 3;
        }

        activeAngle += deltaTime;

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT);

        glm::mat4 view = glm::lookAt(
            cameraPos,
            cameraPos + cameraFront,
            cameraUp
        );

        glm::mat4 projection = glm::perspective(
            glm::radians(45.0f),
            800.0f / 600.0f,
            0.1f,
            100.0f
        );

        glUseProgram(shaderProgram);

        glUniformMatrix4fv(
            glGetUniformLocation(shaderProgram, "view"),
            1,
            GL_FALSE,
            glm::value_ptr(view)
        );

        glUniformMatrix4fv(
            glGetUniformLocation(shaderProgram, "projection"),
            1,
            GL_FALSE,
            glm::value_ptr(projection)
        );

        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D, texture1);

        glBindVertexArray(VAO);

        for (int i = 0; i < 4; i++)
        {
            if (i == activeCube)
            {
                glStencilFunc(GL_ALWAYS, 1, 0xFF);
                glStencilMask(0xFF);
            }
            else
            {
                glStencilMask(0x00);
            }

            glm::mat4 model = glm::mat4(1.0f);

            model = glm::translate(model, cubePositions[i]);

            if (i == activeCube)
            {
                model = glm::rotate(model, activeAngle, glm::vec3(0.5f, 1.0f, 0.0f));
            }

            model = glm::scale(model, cubeScales[i]);

            glUniformMatrix4fv(
                glGetUniformLocation(shaderProgram, "model"),
                1,
                GL_FALSE,
                glm::value_ptr(model)
            );

            glDrawArrays(GL_TRIANGLES, 0, 36);
        }

        glStencilFunc(GL_NOTEQUAL, 1, 0xFF);
        glStencilMask(0x00);
        glDisable(GL_DEPTH_TEST);

        glUseProgram(outlineShaderProgram);

        glUniformMatrix4fv(
            glGetUniformLocation(outlineShaderProgram, "view"),
            1,
            GL_FALSE,
            glm::value_ptr(view)
        );

        glUniformMatrix4fv(
            glGetUniformLocation(outlineShaderProgram, "projection"),
            1,
            GL_FALSE,
            glm::value_ptr(projection)
        );

        glm::mat4 outlineModel = glm::mat4(1.0f);

        outlineModel = glm::translate(outlineModel, cubePositions[activeCube]);
        outlineModel = glm::rotate(outlineModel, activeAngle, glm::vec3(0.5f, 1.0f, 0.0f));
        outlineModel = glm::scale(outlineModel, cubeScales[activeCube] * 1.08f);

        glUniformMatrix4fv(
            glGetUniformLocation(outlineShaderProgram, "model"),
            1,
            GL_FALSE,
            glm::value_ptr(outlineModel)
        );

        glDrawArrays(GL_TRIANGLES, 0, 36);

        glStencilMask(0xFF);
        glStencilFunc(GL_ALWAYS, 1, 0xFF);
        glEnable(GL_DEPTH_TEST);

        glfwSwapBuffers(window);

        glfwPollEvents();

        double frameEnd = glfwGetTime();
        double frameTime = frameEnd - frameStart;
        double targetFrameTime = 1.0 / 60.0;

        if (frameTime < targetFrameTime)
        {
            std::this_thread::sleep_for(
                std::chrono::duration<double>(targetFrameTime - frameTime)
            );
        }

    } while (!glfwWindowShouldClose(window) && !glfwGetKey(window, GLFW_KEY_ESCAPE));

    glDeleteBuffers(1, &VBO);
    glDeleteVertexArrays(1, &VAO);

    glDeleteTextures(1, &texture1);

    glDeleteProgram(shaderProgram);
    glDeleteProgram(outlineShaderProgram);

    glfwTerminate();

    return 0;
}