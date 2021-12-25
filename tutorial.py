import os
import numpy as np
import mne
import pooch
import mne_qt_browser
import matplotlib.pyplot as plt

# sample_data_folder = mne.datasets.sample.data_path()
# print(sample_data_folder)
sample_data_raw_file = os.path.join('/Users/maxwellchen/mne_data/MNE-sample-data', 'MEG', 'sample', 'sample_audvis_filt-0-40_raw.fif')
raw = mne.io.read_raw_fif(sample_data_raw_file)
print(raw)
print(raw.info)
# raw.plot_psd(fmax=50)
# raw.plot(duration = 5, n_channels=30)
mne.viz.set_browser_backend("pyqtgraph")
raw.plot(block = True)
print(raw.info['sfreq'])
data = raw.get_data()
print(np.shape(data))
plt.plot(data[:, 300:400])
plt.show()