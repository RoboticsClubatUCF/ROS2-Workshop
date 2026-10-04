FROM ros:humble-ros-base

# Add the (OSRF) Gazebo apt repo
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://packages.osrfoundation.org/gazebo.gpg \
        -o /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable jammy main" \
        > /etc/apt/sources.list.d/gazebo-stable.list && \
    rm -rf /var/lib/apt/lists/*

#Install all require packages for workshop 2
RUN apt-get update && apt-get install -y \
    ros-humble-turtlesim \
    ignition-fortress \
    ros-humble-ros-gz-bridge \
    python3-colcon-common-extensions \
    xvfb fluxbox x11vnc websockify git && \
    rm -rf /var/lib/apt/lists/*

# noVNC web client
RUN git clone https://github.com/novnc/noVNC.git /opt/noVNC

# startup script to launch graphical environment
RUN printf '%s\n' \
    '#!/bin/bash' \
    'export DISPLAY=:0' \
    'pgrep -x Xvfb        >/dev/null || Xvfb :0 -screen 0 1280x800x24 &' \
    'sleep 2' \
    'pgrep -x fluxbox     >/dev/null || fluxbox &' \
    'pgrep -x x11vnc      >/dev/null || x11vnc -display :0 -forever -nopw -shared -rfbport 5900 &' \
    'pgrep -f novnc_proxy >/dev/null || /opt/noVNC/utils/novnc_proxy --vnc localhost:5900 --listen 6080 &' \
    'sleep 2' \
    'echo "Desktop ready: open the forwarded port 6080 in your browser."' \
    > /usr/local/bin/start-vnc.sh \
    && chmod +x /usr/local/bin/start-vnc.sh

# Environment setup for every shell
RUN echo 'export DISPLAY=:0'                 >> /root/.bashrc \
    && echo 'export LIBGL_ALWAYS_SOFTWARE=1'    >> /root/.bashrc \
    && echo 'source /opt/ros/humble/setup.bash' >> /root/.bashrc