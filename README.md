## Getting Started

To start using this environment:

1. Navigate to the GitHub repository
2. Click on the "Code" button
3. Select the "Codespaces" tab
4. Click "Create codespace on main"

This will launch a cloud-based development environment with VS Code in your browser, complete with ROS2 Humble already installed and configured.

---
## How to View the Simulator (via VNC)

To view graphical simulations like `turtlesim` or Gazebo in your Codespace, follow these steps:

### 1. Start the VNC Server

Open a terminal in your Codespace and run:

```bash
/usr/local/bin/start-vnc.sh
```
### 2. Access the VNC Viewer
In the Codespace UI, go to the Ports tab.

Find the port mapped to 6080.

Click the 🌍 globe icon next to it to open the URL in your browser.

###  3. Connect to the Desktop
When the browser tab opens, select vnc.html

Click Connect (no password is required).

You should now see the graphical desktop where you can run tools like RViz or Gazebo.