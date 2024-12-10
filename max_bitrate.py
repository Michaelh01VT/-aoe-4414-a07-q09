# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# 
# Calculates the maximum achievable bitrate given the transmitter power,
# gains, frequency, distance, noise spectral density, and bandwidth. Assumes fixed
# line and atmospheric losses.
#
# Parameters:
# tx_w: Transmitter power in W
# tx_gain_db: Transmitter antenna gain in dB
# freq_hz: Frequency in Hz
# dist_km: Distance between transmitter and receiver in km
# rx_gain_db: Receiver antenna gain in dB
# n0_j: Noise spectral density in J
# bw_hz: Bandwidth in Hz
#
# Output:
# The maximum achievable bitrate in bits per second.
#
# Written by Michael Hoffman
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import math  # math module
import sys  # argv

# Constants
C = 2.99792458e8  # Speed of light in m/s
LINE_LOSS_DB = -1  # Fixed transmitter to antenna line loss (dB)
ATMOSPHERIC_LOSS_DB = 0  # Fixed atmospheric loss (dB)

# Function to calculate maximum achievable bitrate
def max_bitrate(tx_w, tx_gain_db, freq_hz, dist_km, rx_gain_db, n0_j, bw_hz):
    tx_gain_linear = 10 ** (tx_gain_db / 10)
    rx_gain_linear = 10 ** (rx_gain_db / 10)
    wavelength = C / freq_hz  
    distance_m = dist_km * 1000  

    # Calculate received power
    pr_linear = (tx_w * tx_gain_linear * rx_gain_linear * (wavelength**2)) / \
                ((4 * math.pi)**2 * (distance_m**2))

    # Convert to dB scale
    pr_db = 10 * math.log10(pr_linear) + LINE_LOSS_DB + ATMOSPHERIC_LOSS_DB

    # Calculate noise power
    noise_power = n0_j * bw_hz

    # Calculate signal-to-noise ratio 
    snr_linear = pr_linear / noise_power

    # Calculate maximum achievable bitrate 
    r_max = bw_hz * math.log2(1 + snr_linear)
    return r_max

if len(sys.argv) == 8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
    
    # Calculate maximum bitrate
    r_max = max_bitrate(tx_w, tx_gain_db, freq_hz, dist_km, rx_gain_db, n0_j, bw_hz)
    
    # Print result
    print(math.floor(r_max))
