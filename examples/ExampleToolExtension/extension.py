# Scene Weaver: Tool Extension Declaration
# Declaration information for a Scene Weaver Tool Extension.

# Imports
import argparse

from SceneWeaver.interfaces.extensions.ToolExtensionInterface import ToolExtension

from extensions.ExampleToolExtension.component import doSomeStuff # NOTE: This is how you can import code from your extension!

# Classes
class ExampleToolExtension(ToolExtension):
    """
    An example tool extension.
    """
    # Constructor
    def __init__(self):
        super().__init__("exampleTool", "An example tool extension.")

    # Tool Extension Functions
    def registerWithCli(self, parser: argparse.ArgumentParser):
        """
        Registers this Tool Extension with the Scene Weaver command line interface.
        This is called when the CLI is started.

        parser: An `argparse.ArgumentParser` object that you should use to define any command line arguments that are needed for your tool extension.
        """
        # Add required arguments
        parser.add_argument("text", help="A string to print.", type=str)

        # Add optional arguments
        parser.add_argument("-d", "--debug", action="store_true", help="If provided, runs in debug mode.")

        # NOTE: You can also provide `pass` in this function to indicate no arguments are needed.

    def startFromCli(self, arguments: dict):
        """
        Called by the Command Line Interface when this Tool Extension is being started by a command.
        Consider this the call for execution.

        arguments: A dict of the arguments, if any, specified in the `registerWithCli` funciton.
        """
        doSomeStuff(arguments)

# Command Line
if __name__ == "__main__":
    print("This file cannot be run on the command line.")
