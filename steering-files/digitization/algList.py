from Gaudi.Configuration import *

def makeAlgList(the_args):
    '''-------------------------------------------------------------'''
    '''    Add the Digitization Algorithms to the Algorithm List    '''
    '''-------------------------------------------------------------'''
    algList = []
    # BIB Overlay
    if the_args.doOverlayFull:
    from components.overlay_full import new_overlay_full
    algList.append(new_overlay_full(
        the_args.OverlayFullPathToMuPlus,
        the_args.OverlayFullPathToMuMinus,
        the_args.OverlayFullNumberBackground))

    # Tracker Digitization
    from components.tracking_vertex import new_VXDBarrel, new_VXDEndcap
    from components.tracking_inner import new_ITBarrel, new_ITEndcap
    from components.tracking_outer import new_OTBarrel, new_OTEndcap
    algList.append(new_VXDBarrel())
    algList.append(new_VXDEndcap())
    algList.append(new_ITBarrel())
    algList.append(new_ITEndcap())
    algList.append(new_OTBarrel())
    algList.append(new_OTEndcap())

    # EM, Hadronic, Muon Calorimeter Digitization
    from components.calorimetry_EM import new_ECalBarrelDigi, new_ECalBarrelReco
    from components.calorimetry_EM import new_ECalPlugDigi, new_ECalPlugReco
    from components.calorimetry_EM import new_ECalEndcapDigi, new_ECalEndcapReco
    algList.append(new_ECalBarrelDigi())
    algList.append(new_ECalBarrelReco())
    #algList.append(new_ECalPlugDigi())
    #algList.append(new_ECalPlugReco())
    algList.append(new_ECalEndcapDigi())
    algList.append(new_ECalEndcapReco())
    from components.calorimetry_HAD import new_HCalBarrelDigi, new_HCalBarrelReco
    from components.calorimetry_HAD import new_HCalEndcapDigi, new_HCalEndcapReco
    from components.calorimetry_HAD import new_HCalRingDigi, new_HCalRingReco
    algList.append(new_HCalBarrelDigi())
    algList.append(new_HCalBarrelReco())
    algList.append(new_HCalEndcapDigi())
    algList.append(new_HCalEndcapReco())
    #algList.append(new_HCalRingDigi())
    #algList.append(new_HCalRingReco())
    from components.calorimetry_MU import new_MuonBarrelDigi, new_MuonEndcapDigi
    algList.append(new_MuonBarrelDigi())
    algList.append(new_MuonEndcapDigi())

    # Vertex Filtering
    if the_args.doFilterDL:
        from components.filterDL_vertex import new_filterDL_vertexBarrel, new_filterDL_vertexEndcap
        algList.append(new_filterDL_vertexBarrel())
        algList.append(new_filterDL_vertexEndcap())

    return algList
