import Rhino.Geometry as rg


#1.
#compute face normals using rg.Mesh.FaceNormals.ComputeFaceNormals()
faceNormals = []
facenum = len(m.Faces)
for i in range(facenum):
    norm = m.FaceNormals[i]
    normNeg = rg.Vector3d.Negate(norm)
    faceNormals.append(normNeg)
#output the vectors to a
a = faceNormals

#2
#get the centers of each faces using rg.Mesh.Faces.GetFaceCenter()
centers = []
for i in range(facenum):
    face = m.Faces.GetFaceCenter(i)
    centers.append(face)
#output that list to b
b = centers

#3.
#calculate the angle between the sun and each FaceNormal using rg.Vector3d.VectorAngle()
angleList = []
for i in range(facenum):
    angle = rg.Vector3d.VectorAngle(a[i],s)
    angleList.append(angle)
#store the angles in a list called angleList and output it to c
c = angleList

#4.
#explode the mesh - convert each face of the mesh into a mesh
#for this, you have to first copy the mesh using rg.Mesh.Duplicate()
#then iterate through each face of the copy, extract it using rg.Mesh.ExtractFaces
exploded = []
mesh2 = len(rg.Mesh.Duplicate(m).Faces)
mDup = m.Duplicate()
for i in range(mesh2):
     meshFace = mDup.Faces.ExtractFaces([0])
     exploded.append(meshFace)
#and store the result into a list called exploded in output d
d = exploded

