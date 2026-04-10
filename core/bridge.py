from PySide6.QtCore import QObject, Signal, Slot, Property, QTimer, QThread
import numpy as np
import threading
from typing import Optional

from core.audio_capture import AudioCapture
from core.pitch_detector import PitchDetector
from core.note_converter import NoteConverter
from core.range_tracker import RangeTracker
from models.solfa_result import SolfaResult

class AudioWorker(QObject):
    """
    Worker class to handle the audio processing loop in a separate thread.
    """
    pitch_detected = Signal(float, float)  # freq, confidence

    def __init__(self, capture: AudioCapture, detector: PitchDetector):
        super().__init__()
        self.capture = capture
        self.detector = detector
        self.active = False

    @Slot()
    def process(self):
        self.active = True
        while self.active:
            block = self.capture.get_next_block(timeout=0.1)
            if block is not None:
                freq, conf = self.detector.detect(block.flatten())
                if freq:
                    self.pitch_detected.emit(freq, conf)

    def stop(self):
        self.active = False

class CoreBridge(QObject):
    """
    Bridge between Python processing and QML UI.
    """
    pitchChanged = Signal()
    solfaChanged = Signal()
    rangeChanged = Signal()

    def __init__(self):
        super().__init__()
        self._capture = AudioCapture()
        self._detector = PitchDetector()
        self._converter = NoteConverter()
        self._tracker = RangeTracker()

        # UI Properties
        self._current_freq = 0.0
        self._current_note = ""
        self._current_solfa = ""
        self._min_note = "---"
        self._max_note = "---"

        # Threading for Audio
        self._audio_thread = QThread()
        self._worker = AudioWorker(self._capture, self._detector)
        self._worker.moveToThread(self._audio_thread)
        self._audio_thread.started.connect(self._worker.process)
        self._worker.pitch_detected.connect(self._on_pitch_detected)

    @Property(float, notify=pitchChanged)
    def currentFreq(self):
        return self._current_freq

    @Property(str, notify=pitchChanged)
    def currentNote(self):
        return self._current_note

    @Property(str, notify=solfaChanged)
    def currentSolfa(self):
        return self._current_solfa

    @Property(str, notify=rangeChanged)
    def minNote(self):
        return self._min_note

    @Property(str, notify=rangeChanged)
    def maxNote(self):
        return self._max_note

    def _on_pitch_detected(self, freq: float, conf: float):
        self._current_freq = freq
        self._current_note = self._converter.hz_to_note_name(freq)
        
        # Update Solfa if calibrated
        solfa_res = self._converter.hz_to_solfa(freq)
        if solfa_res:
            self._current_solfa = f"{solfa_res.syllable}{' ' + str(solfa_res.octave) if solfa_res.octave != 0 else ''}"
        
        # Update Range
        self._tracker.add_sample(freq, conf)
        v_range = self._tracker.get_range()
        if v_range:
            self._min_note = v_range.min_note_name
            self._max_note = v_range.max_note_name

        self.pitchChanged.emit()
        self.solfaChanged.emit()
        self.rangeChanged.emit()

    @Slot()
    def startSession(self):
        print("Bridge: Starting session...")
        self._capture.start()
        self._audio_thread.start()

    @Slot()
    def stopSession(self):
        print("Bridge: Stopping session...")
        self._worker.stop()
        self._audio_thread.quit()
        self._audio_thread.wait()
        self._capture.stop()

    @Slot()
    def calibrateTonic(self):
        """
        Calculates tonic from the last few seconds of history or a specific capture.
        For now, just takes the current frequency.
        """
        if self._current_freq > 0:
            self._converter.set_tonic(self._current_freq)
            print(f"Bridge: Tonic calibrated to {self._current_freq} Hz")
