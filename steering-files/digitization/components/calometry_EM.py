from Gaudi.Configuration import *
from Configurables import RealisticCaloDigiSilicon, RealisticCaloRecoSilicon

def new_ECalBarrelDigi():
    """
    Create a new ECal barrel digitiser instance with the given parameters.
    """
    return RealisticCaloDigiSilicon(
        "ECalBarrelDigi",
        calibration_mip = 0.0001575,
        threshold = 5e-05,
        thresholdUnit = "GeV",
        timingCorrectForPropagation = 1,
        timingCut = 1,
        timingResolution = 0.0,
        timingWindowMax = 10.0,
        timingWindowMin = -0.5,
        elec_range_mip = 15000.0,
        CaloType = "em", CaloID = "ecal", CaloLayout = "barrel",
        inputHitCollections = ["OverlayECalBarrelCollection"],
        outputHitCollections = ["EcalBarrelCollectionDigi"],
        outputRelationCollections = ["EcalBarrelRelationsSimDigi"],
        OutputLevel = INFO
    )

def new_ECalBarrelReco():
    """
    Create a new ECal barrel reco instance with the given parameters.
    """
    return RealisticCaloRecoSilicon(
        "ECalBarrelReco",
        calibration_factorsMipGev = [0.00641222630095],
        calibration_layergroups = [41],
        inputLinkCollections = ["EcalBarrelRelationsSimDigi"],
        outputHitCollections = ["EcalBarrelCollectionRec"],
        outputRelationCollections = ["EcalBarrelRelationsSimRec"],
        OutputLevel = INFO
    )

def new_ECalPlugDigi():
    """
    Create a new ECal plug digitiser instance with the given parameters.
    """
    return RealisticCaloDigiSilicon(
        "ECalPlugDigi",
        calibration_mip = 0.0001575,
        threshold = 5e-05,
        thresholdUnit = "GeV",
        timingCorrectForPropagation = 1,
        timingCut = 1,
        timingResolution = 0.0,
        timingWindowMax = 10.0,
        timingWindowMin = -0.5,
        elec_range_mip = 15000.0,
        CaloType = "em", CaloID = "ecal", CaloLayout = "plug",
        inputHitCollections = ["OverlayECalPlugCollection"],
        outputHitCollections = ["ECalPlugCollectionDigi"],
        outputRelationCollections = ["ECalPlugRelationsSimDigi"],
        OutputLevel = INFO
    )

def new_ECalPlugReco():
    """
    Create a new ECal plug reco instance with the given parameters.
    """
    return RealisticCaloRecoSilicon(
        "ECalPlugReco",
        calibration_factorsMipGev = [0.00641222630095],
        calibration_layergroups = [41],
        inputLinkCollections = ["ECalPlugRelationsSimDigi"],
        outputHitCollections = ["ECalPlugCollectionRec"],
        outputRelationCollections = ["ECalPlugRelationsSimRec"],
        OutputLevel = INFO
    )

def new_ECalEndcapDigi():
    """
    Create a new ECal endcap digitiser instance with the given parameters.
    """
    return RealisticCaloDigiSilicon(
        "ECalEndcapDigi",
        calibration_mip = 0.0001575,
        threshold = 5e-05,
        thresholdUnit = "GeV",
        timingCorrectForPropagation = 1,
        timingCut = 1,
        timingResolution = 0.0,
        timingWindowMax = 10.0,
        timingWindowMin = -0.5,
        elec_range_mip = 15000.0,
        CaloType = "em", CaloID = "ecal", CaloLayout = "endcap",
        inputHitCollections = ["OverlayECalEndcapCollection"],
        outputHitCollections = ["EcalEndcapCollectionDigi"],
        outputRelationCollections = ["EcalEndcapRelationsSimDigi"],
        OutputLevel = INFO
    )

def new_ECalEndcapReco():
    """
    Create a new ECal endcap reco instance with the given parameters.
    """
    return RealisticCaloRecoSilicon(
        "ECalEndcapReco",
        calibration_factorsMipGev = [0.00641222630095],
        calibration_layergroups = [41],
        inputLinkCollections = ["EcalEndcapRelationsSimDigi"],
        outputHitCollections = ["EcalEndcapCollectionRec"],
        outputRelationCollections = ["EcalEndcapRelationsSimRec"],
        OutputLevel = INFO
    )