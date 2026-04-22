FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies for Ursina and GUI
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    libgl1-mesa-glx \
    libxxf86vm1 \
    libxcursor1 \
    libxinerama1 \
    libxi6 \
    xvfb \
    x11vnc \
    fluxbox \
    novnc \
    websockify

# Install Ursina
RUN pip install ursina
