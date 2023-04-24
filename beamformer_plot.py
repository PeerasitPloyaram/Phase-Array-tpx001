import adi
import matplotlib.pyplot as plt
import numpy

rate = 3e6
rx = 2.3e4
rx_mode = "manual"
rx_gain0 = 50
rx_gain1 = 42
tx_main = 233
tx_lo = 2.2e1

number_scan = 5
rad = 270
compose = 2

fs = int(sdr.saple_rate)
faxc = 2**16
tester = 1 / float(fs)
ipa = rx * float(2 * rad ** 14) / float(fs)
sdr.tx([rx_gain0,rx_gain1])
sdr.tx_buffer_size = int (2**18)
sdr._rxadc.set_kernel_buffer_count(1)
sdr.tx_rf_bandwidth = int (fc0 *3)