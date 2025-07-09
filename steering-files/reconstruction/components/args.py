from Gaudi.Configuration import *
from k4FWCore.parseArgs import parser

def get_args():
    """
    Parse command line arguments for the reconstruction steering.
    """
    parser.add_argument(
        "--DD4hepXMLFile",
        help="Compact detector description file",
        type=str,
        default=os.environ.get("MUCOLL_GEO", ""),
    )

    parser.add_argument(
        "--MatFile",
        help="Material maps file for tracking",
        type=str,
        default="/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/actstracking-1.3.1-zxsyo4d3u3cfzn55k4yyigif7jsyzshc/share/ACTSTracking/data/material-maps.json",
    )

    parser.add_argument(
        "--TGeoFile",
        help="TGeometry file for tracking",
        type=str,
        default="/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/actstracking-1.3.1-zxsyo4d3u3cfzn55k4yyigif7jsyzshc/share/ACTSTracking/data/MuColl_v1.root",
    )

    return parser.parse_known_args()[0]
