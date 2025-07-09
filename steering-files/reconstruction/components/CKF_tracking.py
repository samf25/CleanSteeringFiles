from Gaudi.Configuration import *
from Configurables import ACTSSeededCKFTrackingAlg, ACTSDuplicateRemoval, FilterTracksAlg

def new_CKFTracker(matFile, TGeoFile):
    """
    Create a new ACTSSeededCKFTrackingAlg instance for CKF tracking.
    """
    return ACTSSeededCKFTrackingAlg(
        "Reconstructor",
        CKF_Chi2CutOff = 10,
        CKF_NumMeasurementsCutOff = 1,
        MatFile = matFile,
        RunCKF = "True",
        SeedFinding_CollisionRegion = 3.5,
        SeedFinding_DeltaRMax = 60,
        SeedFinding_DeltaRMin = 2,
        SeedFinding_MinPt = 500,
        SeedFinding_RMax = 150,
        SeedFinding_RadLengthPerSeed = 0.1,
        SeedFinding_SigmaScattering = 3,
        SeedingLayers = ["13", "2", "13", "6", "13", "10", "13", "14", "14", "2", "14", "6", "14", "10", "14", "14", "15", "2", "15", "6", "15", "10", "15", "14"],
        TGeoFile = TGeoFile,
        OutputTrackCollectionName = ["AllTracks"],
        OutputSeedCollectionName = ["SeedTracks"],
        InputTrackerHitCollectionName = ["MergedTrackerHits"]
        OutputLevel = INFO
    )

def new_deduper():
    """
    Create a new ACTSDuplicateRemoval instance for removing duplicate tracks.
    """
    return ACTSDuplicateRemoval(
        "Deduper",
        InputTrackCollectionName = ["AllTracks"],
        OutputTrackCollectionName = ["DedupedTracks"],
        OutputLevel = INFO
    )


def new_track_filter():
    """
    Create a new FilterTracksAlg instance for filtering tracks.
    """
    return FilterTracksAlg(
        "Filterer",
        InputTrackCollectionName = ["DedupedTracks"],
        MinPt = "0.5",
        MaxD0 = 10,
        MaxZ0 = 10,
        NHitsInner = "0",
        NHitsOuter = "0",
        NHitsTotal = "6",
        NHitsVertex = "0",
        OutputTrackCollectionName = ["SiTracks"],
        OutputLevel = INFO
    )
