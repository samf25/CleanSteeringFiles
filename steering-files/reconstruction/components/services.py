from Gaudi.Configuration import *
from Configurables import GeoSvc, EventDataSvc, THistSvc

def set_services(the_args):
    """
    Set up the necessary services for the reconstruction process.
    
    Parameters:
    the_args: Argument parser object containing configuration parameters.
    """
    geoservice = GeoSvc(
        "GeoSvc",
        detectors = [the_args.DD4hepXMLFile],
        OutputLevel = INFO,
        EnableGeant4Geo = False
    )

    evtsvc = EventDataSvc("EventDataSvc")

    THistSvc().Output = ["histos DATAFILE='histograms.root' TYP='ROOT' OPT='RECREATE'"]
    THistSvc().PrintAll = True
    THistSvc().AutoSave = True
    THistSvc().AutoFlush = True

    return [evtsvc, geoservice, THistSvc()]