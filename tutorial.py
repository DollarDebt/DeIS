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
info = raw.info
data = raw.get_data()
data = data[:, :1280]
raw = mne.io.RawArray(data, info)

# max min etc
print(np.max(raw.get_data()))
print(np.min(raw.get_data()))

print(raw)
print(raw.info)
# raw.plot_psd(fmax=50)
# raw.plot(duration = 5, n_channels=30)
# mne.viz.set_browser_backend("pyqtgraph")
# raw.plot(block = True)
raw.plot()
# raw.plot_psd()
sampling_freq = 200
times = np.linspace(0, 1, sampling_freq, endpoint=False)
sine = 2*np.sin(20 * np.pi * times)
cosine = np.cos(10 * np.pi * times)
data = np.array([sine, cosine])

info = mne.create_info(ch_names=['10 Hz sine', '5 Hz cosine'],
                       ch_types=['misc'] * 2,
                       sfreq=sampling_freq)

simulated_raw = mne.io.RawArray(data, info)
print(info)
simulated_raw.plot(show_scrollbars=False, show_scalebars=False)

eeg = raw.copy().pick_types(meg=False, eeg=True, eog=False)
data = eeg.get_data()
eeg = mne.io.RawArray(data, eeg.info)
print(np.max(data))
print(np.min(data))
mne.viz.set_browser_backend("pyqtgraph")
eeg.plot(block = True)