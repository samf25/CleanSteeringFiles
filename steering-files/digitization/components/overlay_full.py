from Gaudi.Configuration import *
from Configurables import OverlayTiming

def new_overlay_full(pathMuPlus, pathMuMinus, numberBackground):
    """
    Create a new overlay instance with the given parameters.
    """
    return OverlayTiming(
        "OverlayFull",
        BackgroundFileNames = [[pathMuPlus], [pathMuMinus]],
        TimeWindows = {
            "VertexBarrelCollection": [-0.5, 15.],
            "VertexEndcapCollection": [-0.5, 15.],
            "InnerTrackerBarrelCollection": [-0.5, 15.],
            "InnerTrackerEndcapCollection": [-0.5, 15.],
            "OuterTrackerBarrelCollection": [-0.5, 15.],
            "OuterTrackerEndcapCollection": [-0.5, 15.],
            "ECalBarrelCollection": [-0.5, 15.],
            "ECalPlugCollection": [-0.5, 15.],
            "ECalEndcapCollection": [-0.5, 15.],
            "HCalBarrelCollection": [-0.5, 15.],
            "HCalEndcapCollection": [-0.5, 15.],
            "HCalRingCollection": [-0.5, 15.],
            "YokeBarrelCollection": [-0.5, 15.],
            "YokeEndcapCollection": [-0.5, 15.] },
        BackgroundMCParticleCollectionName = "MCParticle",
        MergeMCParticles = False,
        NumberBackground = [numberBackground, numberBackground],
        SimTrackerHits = [
            "VertexBarrelCollection", "VertexEndcapCollection", 
            "InnerTrackerBarrelCollection", "InnerTrackerEndcapCollection",
            "OuterTrackerBarrelCollection", "OuterTrackerEndcapCollection"],
        SimCalorimeterHits = [
            "ECalBarrelCollection", "ECalEndcapCollection", 
            "HCalBarrelCollection", "HCalEndcapCollection",
            "YokeBarrelCollection", "YokeEndcapCollection"],
        MCParticles = ["MCParticles"],
        OutputSimTrackerHits = [
            "OverlayVertexBarrelCollection", "OverlayVertexEndcapCollection", 
            "OverlayInnerTrackerBarrelCollection", "OverlayInnerTrackerEndcapCollection",
            "OverlayOuterTrackerBarrelCollection", "OverlayOuterTrackerEndcapCollection"],
        OutputSimCalorimeterHits = [
            "OverlayECalBarrelCollection", "OverlayECalEndcapCollection", 
            "OverlayHCalBarrelCollection", "OverlayHCalEndcapCollection",
            "OverlayYokeBarrelCollection", "OverlayYokeEndcapCollection"],
        OutputCaloHitContributions = [
            "OverlayECalBarrelContributionCollection", "OverlayECalEndcapContributionCollection",
            "OverlayHCalBarrelContributionCollection", "OverlayHCalEndcapContributionCollection",
            "OverlayYokeBarrelContributionCollection", "OverlayYokeEndcapContributionCollection"],
        OutputLevel = INFO
    )