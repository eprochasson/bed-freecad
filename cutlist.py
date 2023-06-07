import os

current = FreeCAD.ActiveDocument.FileName
output = os.path.join(os.path.dirname(current), "cutlist.csv")

with open(output, 'w') as fout:
    fout.write("part name,length,width,thickness\n")

    objs = FreeCADGui.Selection.getSelection()


    for obj in objs:
        a = obj.Label
        x = obj.Shape.BoundBox.XLength
        y = obj.Shape.BoundBox.YLength
        z = obj.Shape.BoundBox.ZLength
        length, width, thickness = sorted([x, y, z], reverse=True)
        fout.write(str(a) + "," + str(length) + "," + str(width) + "," + str(thickness) + "\n")

App.Console.PrintMessage("Exported cutlist into " + output)
