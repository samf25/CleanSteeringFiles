# Collect Arguements
from components.args import get_args
args = get_args()

# Set Up Services
from Configurables import GeoSvc, UniqueIDGenSvc, EventDataSvc, THistSvc
geoservice = GeoSvc("GeoSvc",
                    detectors = [the_args.DD4hepXMLFile],
                    OutputLevel = INFO,
                    EnableGeant4Geo = False
)
evtsvc = EventDataSvc()
id_service = UniqueIDGenSvc("UniqueIDGenSvc",
                            Seed = 1
)
THistSvc().Output = ["histos DATAFILE='histograms.root' TYP='ROOT' OPT='RECREATE'"]
THistSvc().PrintAll = True
THistSvc().AutoSave = True
THistSvc().AutoFlush = True
THistSvc().OutputLevel = WARNING

# BIB Overlay
if the_args.doOverlayFull:
    from components.overlay_full import new_overlay_full
    algList.append(new_overlay_full(the_args.OverlayFullPathToMuPlus,
                                    the_args.OverlayFullPathToMuMinus,
                                    the_args.OverlayFullNumberBackground))

# Tracker Digitization
from components.tracking_vertex import new_VXDBarrel, new_VXDEndcap
algList.append(new_VXDBarrel())
algList.append(new_VXDEndcap())
from components.tracking_inner  import new_ITBarrel, new_ITEndcap
algList.append(new_ITBarrel())
algList.append(new_ITEndcap())
from components.tracking_outer  import new_OTBarrel, new_OTEndcap
algList.append(new_OTBarrel())
algList.append(new_OTEndcap())

# EM and Hadronic Calorimeter Digitization
from components.calorimetry_EM  import new_ECalBarrelDigi, new_ECalPlugDigi, new_ECalEndcapDigi, new_ECalBarrelReco, new_ECalPlugReco, new_ECalEndcapReco
algList.append(new_ECalBarrelDigi())
algList.append(new_ECalBarrelReco())
#algList.append(new_ECalPlugDigi())
#algList.append(new_ECalPlugReco())
algList.append(new_ECalEndcapDigi())
algList.append(new_ECalEndcapReco())
from components.calorimetry_HAD import new_HCalBarrelDigi, new_HCalEndcapDigi, new_HCalRingDigi, new_HCalBarrelReco, new_HCalEndcapReco, new_HCalRingReco
algList.append(new_HCalBarrelDigi())
algList.append(new_HCalBarrelReco())
algList.append(new_HCalEndcapDigi())
algList.append(new_HCalEndcapReco())
#algList.append(new_HCalRingDigi())
#algList.append(new_HCalRingReco())

# Muon Calorimeter Digitization
from components.calorimetry_MU  import new_MuonBarrelDigi, new_MuonEndcapDigi
algList.append(new_MuonBarrelDigi())
algList.append(new_MuonEndcapDigi())

# Vertex Filtering
if the_args.doFilterDL:
    from components.filterDL_vertex import new_filterDL_vertexBarrel, new_filterDL_vertexEndcap
    algList.append(new_filterDL_vertexBarrel())
    algList.append(new_filterDL_vertexEndcap())


# Declare the IOSvc and pass the input to it
from k4FWCore import IOSvc, ApplicationMgr
svc = IOSvc("IOSvc",
            Input = "output_sim.edm4hep.root",
            Output = "output_digi_highBIB.edm4hep.root"
)
# Run the Application Manager
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc, geoservice],
                OutputLevel=INFO
              )