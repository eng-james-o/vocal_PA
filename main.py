import sys
import os
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from core.bridge import CoreBridge

def main():
    os.environ.setdefault("QT_QUICK_CONTROLS_STYLE", "Basic")

    app = QGuiApplication(sys.argv)
    app.setApplicationName("Vocal Range Analyzer")
    app.setOrganizationName("VocalPA")

    # Create the bridge instance
    bridge = CoreBridge()

    # Create the QML engine
    engine = QQmlApplicationEngine()
    engine.addImportPath(os.path.dirname(__file__))
    engine.addImportPath(os.path.join(os.path.dirname(__file__), "ui"))

    # Expose the bridge to QML as a context property named 'core'
    engine.rootContext().setContextProperty("core", bridge)

    # Resolve the path to the main QML file
    qml_path = os.path.join(os.path.dirname(__file__), "ui", "main.qml")
    
    # Load the QML file
    engine.load(qml_path)

    # Check if the engine loaded correctly
    if not engine.rootObjects():
        print(f"Error: Could not load QML from {qml_path}")
        sys.exit(-1)

    print("Vocal Range Analyzer started successfully.")
    
    # Execute the application
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
