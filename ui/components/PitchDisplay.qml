import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {
    property string solfa: "---"
    property string note: "Silence"
    property real gain: 0.0

    Layout.fillWidth: true
    Layout.preferredHeight: 250
    color: "#1e293b"
    radius: 20

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 10

        Label {
            text: solfa || "---"
            font.pixelSize: 84
            font.weight: Font.Black
            color: "#3b82f6"
            Layout.alignment: Qt.AlignHCenter
        }

        Label {
            text: note || "Silence"
            font.pixelSize: 24
            font.weight: Font.Medium
            color: "#94a3b8"
            Layout.alignment: Qt.AlignHCenter
        }

        GainMeter {
            gain: parent.parent.gain
        }
    }
}
