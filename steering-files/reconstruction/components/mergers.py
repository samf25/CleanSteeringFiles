from Gaudi.Configuration import *
from Configurables import CollectionMerger

def new_mergehits():
    """
    Create a new CollectionMerger instance for merging hits.
    """
    return CollectionMerger(
        "MergeHits",
        InputCollections = ["VXDBarrelHits", "ITBarrelHits", "OTBarrelHits", "VXDEndcapHits", "ITEndcapHits", "OTEndcapHits"],
        OutputCollection = ["MergedTrackerHits"],
        OutputLevel = INFO
    )

def new_mergehitsrelations():
    """
    Create a new CollectionMerger instance for merging hits relations.
    """
    return CollectionMerger(
        "MergeHitsRelations",
        InputCollections = ["VXDBarrelHitsRelations", "ITBarrelHitsRelations", "OTBarrelHitsRelations",
                            "VXDEndcapHitsRelations", "ITEndcapHitsRelations", "OTEndcapHitsRelations"],
        OutputCollection = ["MergedTrackerHitsRelations"],
        OutputLevel = INFO
    )
