import numpy as np
import scipy.io

files = ['/Users/maxwellchen/Desktop/Nguyen_et_al/Short_words/sub_1_ch64_s_eog_removed_256Hz.mat',
         '/Users/maxwellchen/Desktop/Nguyen_et_al/Short_words/sub_3_ch64_s_eog_removed_256Hz.mat',
         '/Users/maxwellchen/Desktop/Nguyen_et_al/Short_words/sub_5_ch64_s_eog_removed_256Hz.mat',
         '/Users/maxwellchen/Desktop/Nguyen_et_al/Short_words/sub_6b_ch80_s_eog_removed_256Hz.mat',
         '/Users/maxwellchen/Desktop/Nguyen_et_al/Short_words/sub_8g_ch64_s_eog_removed_256Hz.mat',
         '/Users/maxwellchen/Desktop/Nguyen_et_al/Short_words/sub_12b_ch64_s_eog_removed_256Hz.mat']
for x in range(6):
    dict = scipy.io.loadmat(files[x])
    keys = list(dict.keys())
    print(keys)
    all_words = dict[keys[4]]
    Out = all_words[0][1]
    In = all_words[1]
    Up = all_words[2]
    print(np.shape(Out))