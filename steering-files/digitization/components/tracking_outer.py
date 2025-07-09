from Gaudi.Configuration import *
from Configurables import DDPlanarDigi

def new_OTBarrel():
    """
    Create a new outer barrel digitiser instance with the given parameters.
    """
    return DDPlanarDigi("OTBarrelDigitiser",
                        CorrectTimesForPropagation = True,
                        IsStrip = False,
                        ResolutionT = [0.06],
                        ResolutionU = [0.007],
                        ResolutionV = [0.09],
                        SubDetectorName = "OuterTrackers",
                        TimeWindowMax = [0.3],
                        TimeWindowMin = [-0.18],
                        UseTimeWindow = True,
                        SimTrackerHitCollectionName = ["OverlayOuterTrackerBarrelCollection"],
                        SimTrkHitRelCollection = ["OTBarrelHitsRelations"],
                        TrackerHitCollectionName = ["OTBarrelHits"],
                        OutputLevel = INFO)

def new_OTEndcap():
    """
    Create a new outer endcap digitiser instance with the given parameters.
    """
    return DDPlanarDigi("OTEndcapDigitiser",
                        CorrectTimesForPropagation = True,
                        IsStrip = True,
                        ResolutionT = [0.06],
                        ResolutionU = [0.007],
                        ResolutionV = [0.09],
                        SubDetectorName = "OuterTrackers",
                        TimeWindowMax = [0.3],
                        TimeWindowMin = [-0.18],
                        UseTimeWindow = True,
                        SimTrackerHitCollectionName = ["OverlayOuterTrackerEndcapCollection"],
                        SimTrkHitRelCollection = ["OTEndcapHitsRelations"],
                        TrackerHitCollectionName = ["OTEndcapHits"],
                        OutputLevel = INFO)
