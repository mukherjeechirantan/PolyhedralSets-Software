print("We are in test", LoopI, "with method =", ModeCall):

P := PolyhedralSets:-PolyhedralSet(parse(FileTools:-Text:-ReadFile(LoopI))):

if ModeCall = newmethod then
	Prof2 := profile(PolyhedralSets:-VerticesAndRays, PolyhedralSets:-IntegerHull2D, PolyhedralSets:-IntegerHull, PolyhedralSets:-New_replaceNonIntegerFacets, PolyhedralSets:-replaceRationalVertices, PolyhedralSets:-triangle_convex_hull, ComputationalGeometry:-ConvexHull, PolyhedralSets:-FacetIntegerHull):

	print("newmethod time for", LoopI, "is", time(PolyhedralSets:-IntegerHull(P, mode=newmethod)));
	showprofile(Prof2);
	unprofile(Prof2):

elif ModeCall = oldmethod then
	Prof1 := profile(PolyhedralSets:-VerticesAndRays, PolyhedralSets:-IntegerHull2D, PolyhedralSets:-IntegerHull, PolyhedralSets:-replaceNonIntegerFacets, PolyhedralSets:-replaceRationalVertices, PolyhedralSets:-triangle_convex_hull, ComputationalGeometry:-ConvexHull, PolyhedralSets:-FacetIntegerHull):

	print("oldmethod time for", LoopI, "is", time(PolyhedralSets:-IntegerHull(P)));
	showprofile(Prof1);
	unprofile(Prof1):
end if;