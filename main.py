from wannier import Wannier
import numpy as np

lattice_vec = np.array(
        [[4.0771999359, 0.0000000000, 0.0000000000],
         [0.0214194091, 4.0771436725, 0.0000000000],
         [0.0214194091, 0.0213071771, 4.0770879964]]

)
system = Wannier('wannier90_hr.dat', lattice_vec)
system.read_hr()
kpt_list = np.array(
    [
        [0.5, 0.5, 0],
        [0, 0, 0],
        [0.5, 0.5, 0.5]
    ]
)
system.plot_band(kpt_list, 50)
print("Stop Here")