import sounddevice as sd
import numpy as np
import queue
from typing import Callable, Optional
from utils.constants import SAMPLE_RATE, BLOCK_SIZE, CHANNELS

class AudioCapture:
    """
    Handles audio input streaming from the microphone.
    Provides a callback mechanism for processing audio blocks.
    """
    def __init__(self, 
                 sample_rate: int = SAMPLE_RATE, 
                 block_size: int = BLOCK_SIZE,
                 channels: int = CHANNELS):
        self.sr = sample_rate
        self.block_size = block_size
        self.channels = channels
        self.stream: Optional[sd.InputStream] = None
        self.is_running = False
        
        # Internal queue for thread-safe processing
        self.audio_queue = queue.Queue()

    def _callback(self, indata: np.ndarray, frames: int, time_info: dict, status: sd.CallbackFlags) -> None:
        """
        Internal callback for sounddevice.
        """
        if status:
            print(f"Audio Capture Status: {status}")
        
        # Put a copy of the block into the queue
        self.audio_queue.put(indata.copy())

    def start(self) -> None:
        """
        Starts the audio input stream.
        """
        if self.is_running:
            return

        self.stream = sd.InputStream(
            samplerate=self.sr,
            blocksize=self.block_size,
            channels=self.channels,
            callback=self._callback
        )
        self.stream.start()
        self.is_running = True

    def stop(self) -> None:
        """
        Stops the audio input stream.
        """
        if self.stream and self.is_running:
            self.stream.stop()
            self.stream.close()
        self.is_running = False

    def get_next_block(self, timeout: Optional[float] = None) -> Optional[np.ndarray]:
        """
        Retrieves the next available audio block from the queue.
        """
        try:
            return self.audio_queue.get(timeout=timeout)
        except queue.Empty:
            return None
