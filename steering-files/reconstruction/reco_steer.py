'''-------------------------------------------------------------'''
''' Reconstruction Steering File for the Muon Collider Detector '''
'''-------------------------------------------------------------'''
# Collect Arguements
from components.args import get_args
args = get_args()

# Set Up Services
from components.services import set_services
[evtsvc, geoservice, THistSvc()] = set_services(args)

# Import the Algorithm List
from algList import makeAlgList
algList = makeAlgList(args)

'''-------------------------------------------------------------'''
'''    Run the Digitization Algorithms in the ApplicationMgr    '''
'''-------------------------------------------------------------'''
# Declare Input and Output for the IOSvc
from k4FWCore import IOSvc, ApplicationMgr
svc = IOSvc(
    "IOSvc",
    Input = "digi_output.edm4hep.root", # Input file from digitization
    Output = "reco_output.edm4hep.root" # Output file for reconstruction
)

# Run the Application Manager
ApplicationMgr(
    TopAlg = algList,
    EvtSel = 'NONE',
    EvtMax   = 10,
    ExtSvc = [evtsvc, geoservice],
    OutputLevel=DEBUG
)