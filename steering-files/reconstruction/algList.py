from Gaudi.Configuration import *

def makeAlgList(the_args):
    '''-------------------------------------------------------------'''
    '''   Add the Reconstruction Algorithms to the Algorithm List   '''
    '''-------------------------------------------------------------'''
    algList = []
    # Merging
    from components.mergers import new_mergehits, new_mergehitsrelations
    algList.append(new_mergehits())
    algList.append(new_mergehitsrelations())

    # CKF Tracking
    from components.CKF_tracking import new_CKFTracker, new_deduper, new_track_filter
    algList.append(new_CKFTracker(
        the_args.MatFile,
        the_args.TGeoFile))
    algList.append(new_deduper())
    algList.append(new_track_filter())

    # Track Performance Monitoring
    from components.track_performance import new_trackTruth, new_trackPerf
    algList.append(new_trackTruth())
    algList.append(new_trackPerf())

    # Pandora PFOs
    from components.pandora import new_pandoraPFA
    algList.append(new_pandoraPFA())

    return algList