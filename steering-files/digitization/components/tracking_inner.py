from Gaudi.Configuration import *
from Configurables import DDPlanarDigi

def new_ITBarrel():
    """
    Create a new inner barrel digitiser instance with the given parameters.
    """
    return DDPlanarDigi("InnerBarrelDigitiser",
                        CorrectTimesForPropagation = True,
                        IsStrip = True,
                        ResolutionT = [0.06],
                        ResolutionU = [0.007],
                        ResolutionV = [0.09],
                        SubDetectorName = "InnerTrackers",
                        TimeWindowMax = [0.3],
                        TimeWindowMin = [-0.18],
                        UseTimeWindow = True,
                        SimTrackerHitCollectionName = ["OverlayInnerTrackerBarrelCollection"],
                        SimTrkHitRelCollection = ["ITBarrelHitsRelations"],
                        TrackerHitCollectionName = ["ITBarrelHits"],
                        OutputLevel = INFO)

def new_ITEndcap():
    """
    Create a new inner endcap digitiser instance with the given parameters.
    """
    return DDPlanarDigi("InnerEndcapDigitiser",
                        CorrectTimesForPropagation = True,
                        IsStrip = False,
                        ResolutionT = [0.06],
                        ResolutionU = [0.007],
                        ResolutionV = [0.09],
                        SubDetectorName = "InnerTrackers",
                        TimeWindowMax = [0.3],
                        TimeWindowMin = [-0.18],
                        UseTimeWindow = True,
                        SimTrackerHitCollectionName = ["OverlayInnerTrackerEndcapCollection"],
                        SimTrkHitRelCollection = ["ITEndcapHitsRelations"],
                        TrackerHitCollectionName = ["ITEndcapHits"],
                        OutputLevel = INFO)