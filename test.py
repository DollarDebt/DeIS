import mne
import numpy as np
import scipy.io
import matplotlib
import matplotlib.pyplot as plt
import mne_qt_browser

files = ['/Users/maxwellchen/Desktop/Nguyen_et_al/Long_words/sub_2b_ch64_l_eog_removed_256Hz.mat',
         '/Users/maxwellchen/Desktop/Nguyen_et_al/Long_words/sub_3b_ch80_l_eog_removed_256Hz.mat',
         '/Users/maxwellchen/Desktop/Nguyen_et_al/Long_words/sub_6_ch64_l_eog_removed_256Hz.mat',
         '/Users/maxwellchen/Desktop/Nguyen_et_al/Long_words/sub_7_ch64_l_eog_removed_256Hz.mat',
         '/Users/maxwellchen/Desktop/Nguyen_et_al/Long_words/sub_9c_ch64_l_eog_removed_256Hz.mat',
         '/Users/maxwellchen/Desktop/Nguyen_et_al/Long_words/sub_11b_ch64_l_eog_removed_256Hz.mat']

dict = scipy.io.loadmat(files[0])
keys = list(dict.keys())
# all_words = dict[keys[4]]
# Out = all_words[0][1]
all_words = dict['eeg_data_wrt_task_rep_no_eog_256Hz_last_beep']
trial = all_words[0][0]
# In = all_words[1]
# Up = all_words[2]
# print(np.shape(Out))

ch_names = ['Fp1', 'Fz', 'F3', 'F7', 'FT9', 'FC5', 'FC1', 'C3', 'T7', 'TP9', 'CP5', 'CP1', 'Pz', 'P3', 'P7',
            'O1', 'Oz', 'O2', 'P4', 'P8', 'TP10', 'CP6', 'CP2', 'Cz', 'C4', 'T8', 'FT10', 'FC6', 'FC2', 'F4', 'F8', 'Fp2',
            'AF7', 'AF3', 'AFz', 'F1', 'F5', 'FT7', 'FC3', 'FCz', 'C1', 'C5', 'TP7', 'CP3', 'P1', 'P5', 'PO7', 'PO3',
            'POz', 'PO4', 'PO8', 'P6', 'P2', 'CPz', 'CP4', 'TP8', 'C6', 'C2', 'FC4', 'FT8', 'F6', 'F2', 'AF4', 'AF8']
ch_types = ['eeg'] * 64
info = mne.create_info(ch_names, ch_types=ch_types, sfreq=256)
info['highpass'] = 8
info['lowpass'] = 70
bad_channels = ['Fp1', 'TP9', 'AF7', 'AF8']
info.set_montage('standard_1020')
info['bads'] = bad_channels
# mne.viz.set_browser_backend("pyqtgraph")
raw = mne.io.RawArray(trial, info)
# raw['custom_ref_applied'] = True
print(raw.info)
raw.plot()
raw.plot_psd()