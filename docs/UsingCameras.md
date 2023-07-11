# Using Cameras with Scene Weaver

- [Using Cameras with Scene Weaver](#using-cameras-with-scene-weaver)
  - [What Are Cameras?](#what-are-cameras)
  - [Camera Safety](#camera-safety)
  - [Types of Camera](#types-of-camera)
    - [Script Defined Cameras](#script-defined-cameras)
    - [Python Defined Cameras](#python-defined-cameras)
    - [Camera Sequences](#camera-sequences)
  - [Testing Cameras](#testing-cameras)

---

## What Are Cameras?

Cameras in Scene Weaver are a way to impart frame by frame movement to content generated using Scene Weaver.
They are defined on a per-Scene Segment basis and allow for a variety of movement controls.
These include X, Y, and Z axis movement as well as Pitch, Roll, and Yaw adjustment.
All that must be done to use a camera is to define it in your Script File or as a Python script, and then reference it by name in the Scene Segment where you want it applied.

## Camera Safety

Keep in mind that cameras of any type are written in Python.
As such, they inherently allow the execution of within them.
Never use cameras that you suspect are malicious and you should always review the code in any cameras before executing them!

## Types of Camera

### Script Defined Cameras

Script Defined Cameras are cameras that are explicitly described within a Scene Weaver Script File as [detailed here](ProjectStructureReference.md#scene-segement-reference).
They exist only within the specific Script File where they were defined, but can be reused indefinitely within that scope.
These cameras are also limited to progressive value based modification of any particular movement axis.
That is to say, they can only move the camera linearly in the specified directions and cannot take more advanced actions like [Python Defined Cameras](#python-defined-cameras) can.

### Python Defined Cameras

Python Defined Cameras are cameras defined in a Python script that has been placed within the `.../SceneWeaver/cameras/` directory.
These scripts must contain a subclass of the `CameraInterface` protocol in the Scene Weaver package.
While output is limited to the methods provided by the protocol, Python Defined Cameras are free to use whatever code is desired to decide how those values should be returned.
This allows for more complex and sequenced camera behaviors that are not limited to linearly moving the camera in one direction like [Script Defined Cameras](#script-defined-cameras) are.

An example of a very basic camera can be found within `.../SceneWeaver/cameras/` directory.

The `CameraInterface` is available at: `SceneWeaver.interfaces.camera.CameraInterface`.

### Camera Sequences

Camera Sequences are a type of [Python Defined Camera](#python-defined-cameras) that allows for explicit sequencing of multiple `CameraInterface` and `CameraValueSet` objects at frame intervals.

## Testing Cameras

Cameras can be tested using the Camera Grapher utility available through the command line.
This tool will graph a camera's frame by frame movement over a specified number of frames without rendering any images from an image generator.
The output can be viewed as individual images, a collected `.gif`, in the `matplotlib` graph viewer, or any combination of the three.

This tool is intended to provide the ability to test your cameras at any time leading to faster iterations and bug discovery.
