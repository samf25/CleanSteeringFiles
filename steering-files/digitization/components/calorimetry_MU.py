from Gaudi.Configuration import *
from Configurables import DDMuonDigiSimple

def new_MuonBarrelDigi():
    """
    Create a new Muon Barrel digitiser instance with the given parameters.
    """
    return DDMuonDigiSimple(
        "MuonBarrelDigitiser",
        calibrationCoeffmuon = 70.1,
        MuonThreshold = 1e-06,
        maxMuonHitEnergy = 2.0,
        CaloLayout = "barrel",
        MUONCollection = ["OverlayYokeBarrelCollection"],
        MUONOutputCollections = ["MuonBarrelHits"],
        RelationOutputCollection = ["MuonBarrelHitsRelations"],
        OutputLevel = INFO
    )


def new_MuonEndcapDigi():
    """
    Create a new Muon Endcap digitiser instance with the given parameters.
    """
    return DDMuonDigiSimple(
        "MuonEndcapDigitiser",
        calibrationCoeffmuon = 70.1,
        MuonThreshold = 1e-06,
        maxMuonHitEnergy = 2.0,
        CaloLayout = "endcap",
        MUONCollection = ["OverlayYokeEndcapCollection"],
        MUONOutputCollections = ["MuonEndcapHits"],
        RelationOutputCollection = ["MuonEndcapHitsRelations"],
        OutputLevel = INFO
    )