#!/usr/bin/env python

# This is a singleton example of running the plugin without compspec,
# primarily to test, etc. There is no validation of the schema or other.

import os

import compspec.artifact

from compspec_ior.plugin import Plugin

here = os.path.dirname(os.path.abspath(__file__))
test_file = os.path.join(here, "test", "ior-data.json")


def main():
    # Load data we've generated with IOR
    plugin = Plugin("ior")
    attributes = plugin.load_metadata(test_file)
    artifact = compspec.artifact.generate(plugin, "ior-compat-example", attributes)
    print(artifact.render())


if __name__ == "__main__":
    main()
