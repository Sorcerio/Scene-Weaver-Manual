# Scene Weaver: The Manual

![Scene Weaver Demo Gif](./repo/bannerVideo_short_small.gif)

_Scene Weaver is a toolkit that allows you to turn non-visual works into dynamic visual accompanyment using generative artwork._

---

- [Scene Weaver: The Manual](#scene-weaver-the-manual)
  - [What is Scene Weaver?](#what-is-scene-weaver)
    - [What Inputs Are Available?](#what-inputs-are-available)
    - [What is the Output?](#what-is-the-output)
    - [Output Operation Details](#output-operation-details)
  - [Why is There No Code?](#why-is-there-no-code)
  - [Supporting the Project](#supporting-the-project)

---

## What is Scene Weaver?

Scene Weaver is a toolkit that allows you to turn non-visual works into dynamic visual accompanyment using (primarily) generative artwork.

Beginning with something as simple as a [Scene Weaver Script file](./docs/ProjectStructureReference.md#script-spt-file-format) and a [Project Parameters file](./docs/ProjectStructureReference.md#parameters-file-reference), you can create a full video complete with optional subtitles and [frame-based camera movements](./docs/UsingCameras.md).
To do this, Scene Weaver runs on top of an [Image Generator](./docs/UsingImageGenerators.md) like the [AUTOMATIC1111/stable-diffusion-webui Web API](https://github.com/AUTOMATIC1111/stable-diffusion-webui).
But, you're not limited to Stable Diffusion.
By creating a subclass of the [ImageGenerationInterface](./SceneWeaver/interfaces/generator/image/ImageGenerationInterface.py) class, you can implement custom generation sources targeting anything from manual hand-drawn input to any other generation platform that supports Text2Image and Image2Image requests.

### What Inputs Are Available?

* Plain text using a [Scene Weaver Script file](./docs/ProjectStructureReference.md#script-spt-file-format).
* See [Future Feature Ideas](#future-feature-ideas) for potential additions to this list.

### What is the Output?

* All images generated during the render process.
    * Based on the structure of your [input](#what-inputs-are-available) and configuration within your [Project Parameters file](./docs/ProjectStructureReference.md#parameters-file-reference).
* Videos of the generated images.
    * Based on configuration within your [Project Parameters file](./docs/ProjectStructureReference.md#parameters-file-reference).

### Output Operation Details

[In the Hull](https://www.youtube.com/watch?v=3WdzD9PYfIU) was generated from `287` Scene Segments at `24` FPS with a Render Ratio of `4`.
Images were generated at a size of `(768, 512)` using the [SDWebApiImageGenerator](./SceneWeaver/generators/image/SDWebApiImageGenerator.py) on an RTX 3080ti (12GB) with xformers enabled paired with an AMD 12 Core CPU.
The operation outputted two videos at `(1920, 1080)` and `(1080, 1920)`.

In this configuration, the complete render of all images and the two output videos took around 11 hours.
This time will vary _greatly_ depending on the hardware you have access to.

On the other end of the spectrum, the [Simple Example](examples\SimpleExample) included in this repo can be rendered with the same parameters in under 12 minutes.

## Why is There No Code?

TODO: Write this section

## Supporting the Project
While I get things rolling and measure engagement, the best way to support the project is by following me on your favorite social media platform to see more of Scene Weaver in action:

* [YouTube](https://www.youtube.com/@mbmcloude)
* [Instagram](https://www.instagram.com/mbmcloude/)
* [Twitch](https://www.twitch.tv/mbmcloude)
* [Twitter](https://twitter.com/mbmcloude)

Or by subscribing to the [MBM newsletter on the website](https://mbmcloude.com/newsletter/).
