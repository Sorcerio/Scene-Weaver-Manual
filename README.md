# Scene Weaver: The Manual

![Scene Weaver Demo Gif](./repo/bannerVideo_short_small.gif)

_The User Manual for Scene Weaver. A toolkit that allows you to turn non-visual works into dynamic visual accompanyment using generative artwork._

---

- [Scene Weaver: The Manual](#scene-weaver-the-manual)
  - [What is Scene Weaver?](#what-is-scene-weaver)
    - [What Inputs Are Available?](#what-inputs-are-available)
    - [What is the Output?](#what-is-the-output)
      - [An Example Output](#an-example-output)
  - [Why is There No Code?](#why-is-there-no-code)
  - [Can I Create Something with Scene Weaver?](#can-i-create-something-with-scene-weaver)
  - [User Manuals](#user-manuals)
  - [Supporting the Project](#supporting-the-project)

---

## What is Scene Weaver?

Scene Weaver is a toolkit that allows you to turn non-visual works into dynamic visual accompanyment using (primarily) generative artwork.

Beginning with something as simple as a [Scene Weaver Script file](./docs/ProjectStructureReference.md#script-spt-file-format) and a [Project Parameters file](./docs/ProjectStructureReference.md#parameters-file-reference), you can create a full video complete with optional subtitles and [frame-based camera movements](./docs/UsingCameras.md).
To do this, Scene Weaver runs on top of an [Image Generator](./docs/UsingImageGenerators.md) like the [AUTOMATIC1111/stable-diffusion-webui Web API](https://github.com/AUTOMATIC1111/stable-diffusion-webui).
But, you're not limited to Stable Diffusion.
By creating a subclass of the `ImageGenerationInterface` class, you can implement custom generation sources targeting anything from manual hand-drawn input to any other generation platform that supports Text2Image and Image2Image requests.

### What Inputs Are Available?

* Plain text using a [Scene Weaver Script file](./docs/ProjectStructureReference.md#script-spt-file-format).
* Additions included raw music input are planned.

### What is the Output?

* All images generated during the render process.
    * Based on the structure of your [input](#what-inputs-are-available) and configuration within your [Project Parameters file](./docs/ProjectStructureReference.md#parameters-file-reference).
* Videos of the generated images.
    * Based on configuration within your [Project Parameters file](./docs/ProjectStructureReference.md#parameters-file-reference).

#### An Example Output

[In the Hull](https://www.youtube.com/watch?v=3WdzD9PYfIU) was generated from `287` Scene Segments at `24` FPS with a Render Ratio of `4`.
Images were generated at a size of `(768, 512)` using the `SDWebApiImageGenerator` on an RTX 3080ti (12GB) with xformers enabled paired with an AMD 12 Core CPU.
The operation outputted two videos at `(1920, 1080)` and `(1080, 1920)`.

In this configuration, the complete render of all images and the two output videos took around 11 hours.
This time will vary _greatly_ depending on the hardware you have access to.

On the other end of the spectrum, the [Simple Example](./examples/SimpleExample) included in this repo can be rendered with the same parameters in under 12 minutes.

## Why is There No Code?

The short answer is that at this time there is no existing software license available that will provide the protection and expressiveness desired for this repository.

The intention, at the time of writing, is to release Scene Weaver in a semi-open format once an adequate software license is created and vetted.
In particular, the intention of this license will be to open the use of Scene Weaver up to artists and creators so that they can craft their own amazing works.
I want to leave full commercialization of the videos created with Scene Weaver in the hands of the end user (as limited by whatever license is present for the generative image solution that was used).

However, it is also desired to deny commercialization of the Scene Weaver _code_ for products like Software as a Service (SaaS) business models and extortionist mobile applications that feed off ignorance about the real inner workings of machine learning models ("ai").
The reasoning behind this is because of the technology in use by Scene Weaver.
Scene Weaver is a program that requires a large amount of compute and time to create an output as we are limited by the technology of our time.
As such, there are limited options for consumer hardware that can run the image generation models associated with Scene Weaver.
This means that large, already solidified businesses have a huge advantage over any competitors in this field.
An advantage that comes from the simple fact that they possess a larger pocket and have the ability to purchase or operate much larger amounts of compute than any average consumer.
And this presents the problem, that with current technology, creating a service for Scene Weaver would require a heavy amount of available computational power on standby.

I have plans for this project as an artistic tool but open source has a history of being subverted by those with more funding.
For the time being, only the documentation will be released while a good solution to this issue is worked on with [Illegal Astronauts](https://illegalastronauts.com).

## Can I Create Something with Scene Weaver?

While the licensing issues for the code base are being handled, commisions will be considered on a case by case basis.
Review the [User Manuals](#user-manuals) below and feel free to contact me through [Instagram](https://www.instagram.com/mbmcloude/) or [Twitter](https://twitter.com/mbmcloude) to discuss.

## User Manuals
* [Project Structure Reference](./docs/ProjectStructureReference.md): Reference documentation on the `parameters.json` and `script.spt` files that compose a Scene Weaver project.
* [Running Project Tests](./docs/RunningProjectTests.md): Documentation on how to run Scene Weaver's unit tests.
* [Using Cameras with Scene Weaver](./docs/UsingCameras.md): Documentation on how to use existing cameras for Scene Weaver and how to create your own.
* [Using Image Generators with Scene Weaver](./docs/UsingImageGenerators.md): Documentation on how to setup existing image generation interfaces for Scene Weaver and how to create your own.

## Supporting the Project
While I get things rolling and measure engagement, the best way to support the project is by following me on your favorite social media platform to see more of Scene Weaver in action:

* [YouTube](https://www.youtube.com/@mbmcloude)
* [Instagram](https://www.instagram.com/mbmcloude/)
* [Twitch](https://www.twitch.tv/mbmcloude)
* [Twitter](https://twitter.com/mbmcloude)

Or by subscribing to the [MBM newsletter on the website](https://mbmcloude.com/newsletter/).
