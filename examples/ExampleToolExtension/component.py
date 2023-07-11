# A simple example component of the ExampleToolExtension that is imported.

# Imports
import webbrowser

# Functions
def doSomeStuff(args: dict):
    """
    Does some stuff.

    args: The arguments from the CLI.
    """
    # Report
    print(f"These are my arguments: {args}")

    # Open the MBM website
    siteAddr = "https://mbmcloude.com"
    print(f"Check out `{siteAddr}` while you're at it!")
    webbrowser.open(siteAddr)

# Command Line
if __name__ == "__main__":
    print("This file cannot be run on the command line.")
