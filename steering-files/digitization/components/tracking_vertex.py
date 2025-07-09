from Gaudi.Configuration import *
from Configurables import DDPlanarDigi

def new_VXDBarrel():
    """
    Create a new vertex barrel instance with the given parameters.
    """
    return DDPlanarDigi("VXDBarrelDigitiser",
                        CorrectTimesForPropagation = True,
                        IsStrip = False,
                        ResolutionT = [0.03],
                        ResolutionU = [0.005],
                        ResolutionV = [0.005],
                        SubDetectorName = "Vertex",
                        TimeWindowMax = [0.15],
                        TimeWindowMin = [-0.09],
                        UseTimeWindow = True,
                        SimTrackerHitCollectionName = ["OverlayVertexBarrelCollection"],
                        SimTrkHitRelCollection = ["VXDBarrelHitsRelations"],
                        TrackerHitCollectionName = ["VXDBarrelHits"],
                        OutputLevel = INFO)

def new_VXDEndcap():
    """
    Create a new vertex endcap instance with the given parameters.
    """
    return DDPlanarDigi("VXDEndcapDigitiser",
                        CorrectTimesForPropagation = True,
                        IsStrip = False,
                        ResolutionT = [0.03],
                        ResolutionU = [0.005],
                        ResolutionV = [0.005],
                        SubDetectorName = "Vertex",
                        TimeWindowMax = [0.15],
                        TimeWindowMin = [-0.09],
                        UseTimeWindow = True,
                        SimTrackerHitCollectionName = ["OverlayVertexEndcapCollection"],
                        SimTrkHitRelCollection = ["VXDEndcapHitsRelations"],
                        TrackerHitCollectionName = ["VXDEndcapHits"],
                        OutputLevel = INFO)