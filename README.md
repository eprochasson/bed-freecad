# Bed in FreeCAD

A simple model of a bed done in FreeCAD.

The dimensions can be modified to adjust to different mattress sizes (current: Queen). It should be fairly explanatory.

The `cutlist.py` file is a super simple Python script to generate the list of cuts. Select the parts you want in FreeCAD, run the script from the Python console, and it will generate a file named `cutlist.csv`, indicating the list of cuts you need. FTR, the existing one includes the mattress, which you're not expected to cut, given for reference.

Dimensions are all in millimeters.

## Disclaimer

I'm by no mean an expert, use at your own risk. This is most likely not how someone is supposed to develop stuff with FreeCAD.

## License

MIT

