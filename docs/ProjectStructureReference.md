# Scene Weaver Project Structure Reference

- [Scene Weaver Project Structure Reference](#scene-weaver-project-structure-reference)
  - [A Scene Weaver Project](#a-scene-weaver-project)
  - [The Parameters File](#the-parameters-file)
    - [Parameters File Reference](#parameters-file-reference)
  - [The Script (.spt) File](#the-script-spt-file)
    - [Script (.spt) File Format](#script-spt-file-format)
    - [Scene Segement Reference](#scene-segement-reference)

---

## A Scene Weaver Project

A Scene Weaver Project is composed of:

* A `parameters.json` [Parameters file](#the-parameters-file).
* A `*.spt` [Script file](#the-script-spt-file).
* Any additional assets like `initialImage` that may be in a subdirectory.

A Scene Weaver Project should exist in a single directory following a structure like the following:

```
Scene Weaver Project/
├─ Assets/
│  ├─ initialImage.png
│  ├─ etc ...
├─ parameters.json
├─ script.spt
```

## The Parameters File

The `parameters.json` file defines a Scene Weaver Project's [Script File](#the-script-spt-file) alongside all other project parameters.
These include the parameters for both image and video generation.

Filepaths inside the `parameters.json` file can be either absolute or relative.
However, preference is made to relative paths as this will allow your project to be transportable around your filesystem and to other devices.
As such, it is recommended to store your assets like `initialImage` and `cornerImages` images inside your Scene Weaver Project's directory or a subdirectory within it.

All values in the `parameters.json` file are optional.
As such, an empty dictionary (`{}`) can be supplied to use the absolute default configuration, but this is not recommended.
This allows you to supply the values that are important to your project as they are needed.
However, keep in mind that providing elements such as `script`, the [Script File](#the-script-spt-file) path, is almost always something you should include or your script may not be found.

### Parameters File Reference

The following is an example of a complete `parameters.json` file.
The complete project this file is associated with can be found in the `examples/` directory of Scene Weaver.

```json
{
    "_v": "1.0.0",
    "script": "./script.spt",
    "seed": 42,
    "framerate": 30,
    "width": 768,
    "height": 512,
    "renderRatio": 3,
    "initialImage": "./initImage.png",
    "defaults": {
        "initialWeight": 0.75,
        "frameWeight": 0.5,
        "promptPrefix": "a blueprint of ",
        "promptPostfix": ", realistic, design documentation, hirez",
        "readtimeWeight": 3.0
    },
    "videos": {
        "widescreen": {
            "width": 1920,
            "height": 1080,
            "content": {
                "render": true,
                "fitInCanvas": true
            },
            "background": {
                "render": true,
                "blur": 7.0
            },
            "cornerImages": {
                "topLeft": "./squareBlue.png",
                "topRight": "./squareGreen.png",
                "bottomRight": "./squareRed.png",
                "bottomLeft": "./squareYellow.png",
                "inset": 24
            },
            "subtitles": {
                "fontPath": "./AdventPro-Medium.ttf",
                "fontSize": 72,
                "position": "center",
                "color": [242, 216, 95],
                "buffer": 64,
                "strokeWidth": 8,
                "strokeColor": "black"
            }
        },
        "vertical": {
            "width": 1080,
            "height": 1920,
            "subtitles": {
                "position": "subtitle"
            }
        }
    }
}
```
* `_v`: Scene Weaver version.
    * This value is used internally.
* `script`: A filepath pointing to the project's `.spt` Script File.
    * The filepath can be absolute or relative _(preferred)_ to the Parameters File.
* `seed`: An int to use as the seed for image generation.
* `framerate`: An int specifying the desired frames per second for generation.
* `width`: An int specifying the width of each generated image.
* `height`: An int specifying the height of each generated image.
* `renderRatio`: A float >=1 specifying the ratio between rendered frames and total frames _per Scene Segment_.
    * Providing `3` (a 1:3 ratio) to a Scene Segment with 150 frames total would result in 50 frames being rendered by the image generator and 100 frames interpolated between them during video generation.
    * Providing `1` (a 1:1 ratio) to a Scene Segment with 150 frames would result in 150 frames being rendered by the image generator.
        * This can be considered the "Off" state.
* `initialImage`: A filepath pointing to the project's initial image.
    * If `null` is provided or `initialImage` is not specified, an intial image will be generated using the first Scene Segment's prompt.
    * The filepath can be absolute or relative _(preferred)_ to the Parameters File.
* `defaults`: A dictionary of definitions to override the default values for generation.
    * `initialWeight`: A float specifying the Image2Image weight to use for the first image in a Scene Segment.
    * `frameWeight`: A float specifying the Image2Image weight to use for each image in a Scene Segment after the initial frame.
    * `promptPrefix`: A string prefix to add to the beginning of the `text` of any Scene Segments that do not have an explicit prompt.
    * `promptPostfix`: A string postfix to add to the beginning of the `text` of any Scene Segments that do not have an explicit prompt.
    * `readtimeWeight`: A float specifying the weight to use when calculating the read time for any given line. Higher positive values will produce a higher calculated read time.
* `videos`: A dictionary of desired output video configurations.
    * `widescreen`/`vertical`/_etc_: The Key Value of each configuration will be used as the name of the associated output video.
        * `width`: An int specifying the width of the rendered output video.
        * `height`: An int specifying the height of the rendered output video.
        * `content`: A dictionary specifying how the primary image for each video frame should be rendered.
            * `render`: If `false`, no content will be rendered.
            * `fitInCanvas`: If `true`, the content will be scaled to fit within the bounds of the video's dimensions and may expose the `background`. If `false`, the content will be scaled to cover the dimensions of the video and some of the content may be cut off.
        * `background`: A dictionary specifying how the image that may be shown behind the content should be rendered.
            * `render`: If `false`, no background will be rendered and the base background color will be shown.
            * `blur`: A float specifying the amount of gaussian blur applied to the background.
        * `cornerImages`: A dictionary specifying how the images superimposed in any of the corners of the final video should be rendered.
            * `topLeft`: A filepath pointing to an image to superimpose in the top left corner of the final video.
                * The filepath can be absolute or relative _(preferred)_ to the Parameters File.
            * `topRight`: A filepath pointing to an image to superimpose in the top right corner of the final video.
                * The filepath can be absolute or relative _(preferred)_ to the Parameters File.
            * `bottomRight`: A filepath pointing to an image to superimpose in the bottom right corner of the final video.
                * The filepath can be absolute or relative _(preferred)_ to the Parameters File.
            * `bottomLeft`: A filepath pointing to an image to superimpose in the top bottom left corner of the final video.
                * The filepath can be absolute or relative _(preferred)_ to the Parameters File.
            * `inset`: An int specifying how far any provided corner image should be inset from the edge of the video's dimensions.
        * `subtitles`: A dictionary specifying how the `text` from any given Scene Segment should be rendered onto the final video.
            * `fontPath`: A filepath pointing to a `.ttf` to use for the subtitles.
                * If no font path is provided, the default font located in `.../SceneWeaver/bin/` will be used.
                * If the default Scene Weaver font is missing, the default PIL Image Font will be used.
            * `fontSize`: An int specifying the size of the font used by the subtitles.
            * `position`: A string indicating where the text should be rendered on the final video.
                * The options for this key are: `center`, `subtitles`, `topLeft`, `topRight`, `bottomRight`, and `bottomLeft`.
            * `color`: A color expressed as an HTML Color String or an array of RGB color values to use for the text color.
            * `buffer`: An int specifying how far the text should be rendered from the edge of the final video's dimensions.
            * `strokeWidth`: An int specifying the width of the stroke around the subtitles.
            * `strokeColor`: A color expressed as an HTML Color String or an array of RGB color values to use for the stroke.

## The Script (.spt) File

The Scene Weaver Script File defines the content that will be rendered by Scene Weaver.
Each Script File should have an extension of `.spt` and can be parsed as YAML.
The file extension having been inspired by one of Scene Weaver's own inspirations: [SCUMM](https://en.wikipedia.org/wiki/SCUMM).
The specific Script File to use is defined in the [Parameters File](#the-parameters-file) and, as such, can be named as you please.

The Script File is broken up into parts referred to as Scene Segments.
A group of these components makeup a Scene and a group of Scenes makeup Screenplay which is directly respresented by the Script File as a whole.
Each Scene Segment can be configured differently with various prompts, render parameters, and camera movements.

### Script (.spt) File Format

The following is an example of a complete `.spt` Script File or Screenplay.
The complete project this file is associated with can be found in the `examples/` directory of Scene Weaver.

```yaml
# Title: The Cat's Meow

---
Zoom in on Cat:
    text: "A cat perched on a chair."
    parameters:
        prompt: "dslr photograph of an extreme close up view of a tuxedo cat's face in a nice kitchen, realistic"
        duration: 5
        camera:
            name: "zoom"
            z: -10
            x: 0
            y: 0
            roll: 0
            pitch: 0
            yaw: 0

---
Zoom in on Computer:
    text: "Surfing the internet for warmth."
    parameters:
        prompt: "dslr photograph of a wide view of a laptop on a wooden table in a nice kitchen, realistic"
        duration: 5
        camera: "zoom"
        initialWeight: 1.0

---
Cat is on top of the Computer:
    text: "In the winter chill."
    parameters:
        prompt: "dslr photograph of a wide view of a tuxedo cat sitting on laptop on a wooden table in a nice kitchen, realistic"
        duration: 7
        initialWeight: 0.5
```
* The title of the Screenplay is described at the top of the document in the `Title: <etc>` format.
* In the first Scene, these is only one Scene Segment.
* A Scene can be composed of one or many Scene Segments.
* See below for [documentation of what each Scene Segment can contain](#scene-segement-reference).
* The `---` characters indicate a new Scene has begun.
* Within any two given `---` elements the primary key for each Scene Segment in that Scene _must not be the same value_.
    * This means a Scene with two Scene Segments must have unique names for each Scene Segment.
    * Calling every Scene Segment, for example, "Untitled Scene Segment" _will_ result in them being overwritten when loaded into Python!
* This process is repeated until an entire story is expressed through Scene Segments.

### Scene Segement Reference

The Scene Segment is the smallest building block of a Scene Weaver Script.
Each Scene Segment can thought of as a single sentence, or even sentence part, within a classic text-only story.

Within a Scene Segment all values _except_ the Primary Key, which functions as the name of the Scene Segment, and the `text` Key are optional.
If only the Primary Key and `text` values are specified, then a prompt will be created using the Parameters File's `promptPrefix` and `promptPostfix`, or Scene Weaver's default if the values are not defined.
Additonally, the `duration` will be calculated based on the estimated read time of the `text` value.
All other values will be drawn from the defaults for Scene Weaver.

The following is an example of a single complete Scene Segment.
Keep in mind, it is recommended to use double quotes for any strings defined in each Scene Segment to handle natural language punctuation.

```yaml
An Example Scene Segment:
    text: A cat perched on a chair.
    parameters:
        prompt: dslr photograph of an extreme close up view of a tuxedo cat's face in a nice kitchen, realistic
        duration: 5
        camera:
            name: "zoomIn"
            z: -10
            x: 0
            y: 0
            roll: 0.0
            pitch: 0
            yaw: 0
        initialWeight: 0.75
        frameWeight: 0.5
        usingImage: null
```
* `primaryKey`: The Primary Key (here "An Example Scene Segment") is a _required_ name for the Scene Segment both for organization and future identification within the code.
    * `text`: A _required_ string expressing the text associated with this Scene Segment.
    * `parameters`: A dictionary of parameters defining how the Scene Segment will be rendered.
        * `prompt`: A string specifying a custom prompt for this particular Scene Segment.
        * `duration`: An int specifying the amount of time in seconds this Scene Segment should remain on screen.
        * `camera`: This value can either be a string like `basicForwardZoom` to reference a Python Defined Camera in the `.../SceneWeaver/cameras` directory **or** a dictionary defining a Script Defined Camera with the following key-value pairs.
            * `name`: A string specifying the name of the camera.
                * This can be used later within the Script File in other Scene Segmenets by name without redefining the details.
            * `z`: An int specifying the amount of Z-Axis movement _in pixels_ to be applied between each frame of the Scene Segment.
                * A negative value will zoom into the frame while a positive value will zoom out of the frame.
            * `x`: An int specifying the amount of X-Axis movement _in pixels_ to be applied between each frame of the Scene Segment.
            * `y`: An int specifying the amount of Y-Axis movement _in pixels_ to be applied between each frame of the Scene Segment.
            * `roll`: A float specifying the amount of Roll _in degrees_ to be applied to each frame of the Scene Segment.
            * `pitch`: An int specifying the amount of Pitch _in pixels_ to be applied to each frame of the Scene Segment.
                * A negative value will visually bank the frame up while a positive value will visually bank the frame down.
            * `yaw`: An int specifying the amount of Yaw _in pixels_ to be applied to each frame of the Scene Segment.
                * A negative value will visually turn the frame to the left while a positive value will visually turn the frame to the right.
        * `initialWeight`: A Scene Segment specific override of the Parameter File's initial Image2Image weight that is used for generation of the first image in a Scene Segment.
        * `frameWeight`: A Scene Segment specific override of the Parameter File's frame Image2Image weight to use for each image in a Scene Segment after the initial frame.
        * `usingImage`: An string absolute or relative path (preferred when loading from a project directory) to an image to use as an explicit initial image in generation of the Scene Segment's first image.
            * Specifying `usingImage` will override any image passed to this Scene Segment from the previous Scene Segment.
            * When generating using the provided image, the `initialWeight` _will be respected_ during generation of the first frame of the Scene Segment as usual.
