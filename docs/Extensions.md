# Scene Weaver Extensions

- [Scene Weaver Extensions](#scene-weaver-extensions)
  - [Extension Safety](#extension-safety)
  - [Tool Extensions](#tool-extensions)
    - [\_\_init\_\_.py](#__init__py)
    - [extension.py](#extensionpy)
    - [Other Files](#other-files)

---

## Extension Safety

Keep in mind that extensions of any type are written in Python.
As such, they inherently allow the execution of within them.
Never use extensions that you suspect are malicious and you should always review the code in any extensions before executing them!

## Tool Extensions

Tool Extensions provide a way to interact with the components of Scene Weaver on a direct level as well as extending it with your own code.
Any added Tool Extensions will appear automatically in the Scene Weaver CLI under the `extensions` category along with their unique command line arguments.
An example of a basic, but complete Tool Extension can be found at [examples/ExampleToolExtension](../examples/ExampleToolExtension/).

Tool Extensions live in the `extensions/` directory, at the very least, comply with the following directory structure:

```
extensions/
├─ MyExtension/
│  ├─ __init__.py
│  ├─ extension.py
```

### \_\_init\_\_.py
`__init__.py` is a required Python file to allow importing the Python scripts within this directory.

The simplest way to include this is to use the [automated general use file](../examples/ExampleToolExtension/__init__.py) found in the Tool Extension example.
This version of the `__init__.py` script will automatically collect all `.py` files within the directory and add them to the `__all__` declaration for the directory.

Alternatively, you can supply your own to limit specific exports.
Just be sure to include the `extension.py` file!

### extension.py
The `extension.py` file is how the Scene Weaver system knows that your extension is a Tool Extension. In this file, you should introduce a class named uniquely for your Tool Extension comforming to the `ToolExtension` interface.

In the `__init__` function, you should call the `super()` of your custom class and define your extension's `name` and `description` properties.

* `name` refers to how your extension will be referred to within the Scene Weaver system and the command used to invoke it in the Scene Weaver CLI.
* `description` defines the explanation text for your extension in the Scene Weaver CLI.

The delegate functions `registerWithCli(...)` and `startFromCli(...)` define the operation of your Tool Extension.

* `registerWithCli(...)` is how your Tool Extension registers with the Scene Weaver CLI and is where you can define any command line arguments.
* `startFromCli(...)` is called by Scene Weaver when your Tool Extension is executed from the CLI and is effectively your `main()` function.

### Other Files

And remember that `__init__.py` and `extension.py` are the _required_ items to include in your extension.
You can always include any other files or directories you need within your Tool Extension as shown in the [ExampleToolExtension](../examples/ExampleToolExtension/).

To import these files into other files in your extension, remember that the contextual execution point is at Scene Weaver's `cli.py` file.
As such, to import a file within your Tool Extension, you must use an import statement similar to the following:

```Python
from extensions.YourExtension.Foo import Bar
```

An example of how this importation works is also included in the [ExampleToolExtension](../examples/ExampleToolExtension/extension.py).
