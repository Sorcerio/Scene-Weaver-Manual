# Using Cameras with Scene Weaver

- [Using Cameras with Scene Weaver](#using-cameras-with-scene-weaver)
  - [Script Defined Cameras](#script-defined-cameras)
  - [Python Defined Cameras](#python-defined-cameras)

---

Cameras in Scene Weaver are a way to impart frame by frame movement to content generated using Scene Weaver.
They are defined on a per-Scene Segment basis and allow for a variety of movement controls.
These include X, Y, and Z axis movement as well as Pitch, Roll, and Yaw adjustment.
All that must be done to use a camera is to define it in your Script File or as a Python script, and then reference it by name in the Scene Segment where you want it applied.

## Script Defined Cameras

Script Defined Cameras are cameras that are explicitly described within a Scene Weaver Script File as [detailed here](ProjectStructureReference.md#scene-segement-reference).
They exist only within the specific Script File where they were defined, but can be reused indefinitely within that scope.
These cameras are also limited to progressive value based modification of any particular movement axis.
That is to say, they can only move the camera linearly in the specified directions and cannot take more advanced actions like [Python Defined Cameras](#python-defined-cameras) can.

## Python Defined Cameras

Python Defined Cameras are cameras defined in a Python script that has been placed within the `.../SceneWeaver/cameras/` directory.
These scripts must contain a subclass of the `CameraInterface` protocol in the Scene Weaver package.
While output is limited to the methods provided by the protocol, Python Defined Cameras are free to use whatever code is desired to decide how those values should be returned.
This allows for more complex and sequenced camera behaviors that are not limited to linearly moving the camera in one direction like [Script Defined Cameras](#script-defined-cameras) are.

An example of a very basic camera can be found within `.../SceneWeaver/cameras/` directory.

The `CameraInterface` is available at: `SceneWeaver.interfaces.camera.CameraInterface`.
