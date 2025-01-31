import mne
import numpy as np

def analyze_signal(signal: str):
    try:
        # Преобразуем строку в массив чисел
        signal_data = np.array([float(i) for i in signal.split(',')])
        print(signal_data, len(signal_data), type(signal_data[0]))
        # Создаем объект MNE Raw, имитируя ЭЭГ сигнал
        info = mne.create_info(ch_names=["EEG"], sfreq=len(signal_data), ch_types=["eeg"])
        raw = mne.io.RawArray([signal_data], info)

        # Применяем фильтрацию (например, частотный фильтр 1-50 Гц)
        raw.filter(1, 7.4, l_trans_bandwidth=0.5, filter_length='auto')

        # Рассчитываем спектральную плотность мощности (PSD)
        psd, freqs = mne.time_frequency.psd_welch(raw)

        # Рассчитываем статистику
        signal_max = np.max(signal_data)
        signal_min = np.min(signal_data)
        signal_mean = np.mean(signal_data)
        signal_std = np.std(signal_data)

        result = {
            "max": signal_max,
            "min": signal_min,
            "mean": signal_mean,
            "std_dev": signal_std,
            "psd_mean": np.mean(psd),  # Средняя PSD
            "psd_max": np.max(psd),    # Максимальная PSD
            "message": "Signal analyzed with MNE successfully!"
        }

        return result
    #except ValueError:
    #    return {"error": "Invalid input data. Ensure the signal consists of comma-separated numbers."}
    except Exception as e:
        return {"error": str(e)}