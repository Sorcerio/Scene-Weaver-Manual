# Using Image Generators with Scene Weaver

- [Using Image Generators with Scene Weaver](#using-image-generators-with-scene-weaver)
  - [Built-In Image Generators](#built-in-image-generators)
    - [Mock Image Generator](#mock-image-generator)
      - [To Use](#to-use)
    - [Stable Diffusion Web API Generator](#stable-diffusion-web-api-generator)
      - [To Use](#to-use-1)
  - [The Image Generator Interface](#the-image-generator-interface)
    - [Generation Functions](#generation-functions)
    - [Delegate Functions](#delegate-functions)

---

Image Generators are the backbone of Scene Weaver.
These classes comply with Scene Weaver's `ImageGenerationInterface` protocol to allow for flexible production of images for a Screenplay.
Since each Image Generator is implemented using a common interface protocol, maximum flexibility is afforded to the Scene Weaver system.

## Built-In Image Generators
### Mock Image Generator

Scene Weaver's included `MockImageGenerator` is an implementation of the `ImageGenerationInterface` that produces simple mock images.
Compared to the compute required for real world generators like Stable Diffusion, MidJourney, and by-hand art production the weight of the `MockImageGenerator` is minimal.
As such, it lends itself well to the purpose of testing and experimenting with Scene Weaver's functional inner workings.
Because of this, the `MockImageGenerator` is even used with Scene Weaver's automated unit tests.

#### To Use

The `MockImageGenerator` can be selected from the Scene Weaver Command Line Interface and used directly without any other prep.

The `MockImageGenerator` can also be directly imported for use with the `SceneWeaverEngine` class.
When created, the `MockImageGenerator` requires no inputs and is intended to work out of the box without any complications.

### Stable Diffusion Web API Generator

Scene Weaver's included `SDWebApiImageGenerator` is an implementation of the `ImageGenerationInterface` that uses the [AUTOMATIC1111/stable-diffusion-webui API](https://github.com/AUTOMATIC1111/stable-diffusion-webui) to generated images using Stable Diffusion.
This implementation of the `ImageGenerationInterface` requires the Stable Diffusion Web UI to be running in `--api` mode alongside Scene Weaver's operation.
However, this affords a great level of flexibility and configuration since Stable Diffusion's settings and models can be directly managed through the web interface.

Functionally, the `SDWebApiImageGenerator` connects to the Stable Diffusion Web UI's API through either a local or remote network connection.
From there, images can be requested in both Text2Image and Image2Image modes directly.

#### To Use

1. Ensure the machine you are using is capable of running the [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui).
2. Install the [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) following the instructions included in that repository.
3. Ensure the Web UI starts and you can generate images on your machine.
4. Add the `--api` flag to the `webui-user.bat` file so your file looks something like this:

```bat
@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=--api

call webui.bat
```

4. Start the Web UI.
5. Wait for the message indicating the Web UI has completed startup.

Once setup, the `SDWebApiImageGenerator` can be selected from the Scene Weaver Command Line Interface and used directly.

The same goes for using the `SDWebApiImageGenerator` as a direct import for use with the `SceneWeaverEngine` class.
Though when created in this way elements such as the base API url target and more can be defined directly.

## The Image Generator Interface

The `ImageGenerationInterface` allows for a wide variety of options to be created for image generation in Scene Weaver.
Any system whether it be machine learning driven or digitalization of hand painted paintings can be made to work within the Scene Weaver infrastructure.
All that must be done is to create a custom class that conforms to the `ImageGenerationInterface` protocol.
Primarily this entails having to provide images in both Text2Image and Image2Image modes.
A handful of delegate hook functions are also available to help facilitate more advanced functionality.

The `ImageGenerationInterface` is available at: `SceneWeaver.components.screenplay.SceneWeaverSceneSegment`.

### Generation Functions

* `textToImage(...)`: A function that takes a prompt and some supporting parameters to create a specified number of images at a given size from scratch.
* `imageToImage(...)`: A function that takes a prompt and some supporting parameters to create a specified number of images at a given size based on a provided initial image path.

### Delegate Functions

* `sceneSegmentStarted(...)`: This delegate function is called when a Scene Segment's render is started.
    * The `SceneWeaverSceneSegment` that called this function is provided as a parameter.
    * Use Case: The generator needs to prepare some resources before each Scene Segment.
* `sceneSegmentEnded(...)`: This delegate function is called when a Scene Segment has finished rendering.
    * The `SceneWeaverSceneSegment` that called this function is provided as a parameter.
    * Use Case: The generator needs to clean up some created resources after each Scene Segment.
* `renderCompleted(...)`: This delegate function is called when the render has completed and all output files have been moved into the project directory.
    * Use Case: The generator needs to clean up temporary files created during the render operation.
