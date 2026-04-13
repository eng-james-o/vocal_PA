import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ColumnLayout {
    property string minNote: "---"
    property string maxNote: "---"
    property real currentFreq: 0.0

    Layout.fillWidth: true
    spacing: 20

    Label {
        text: "Your Range"
        font.pixelSize: 20
        font.weight: Font.Bold
        color: "#f8fafc"
    }

    Rectangle {
        Layout.fillWidth: true
        Layout.fillHeight: true
        color: "#1e293b"
        radius: 20

        GridLayout {
            anchors.fill: parent
            anchors.margins: 30
            columns: 2
            rowSpacing: 20

            Label { text: "Lowest"; color: "#94a3b8"; font.pixelSize: 16 }
            Label { text: minNote; color: "#f8fafc"; font.pixelSize: 24; font.weight: Font.Bold }

            Label { text: "Highest"; color: "#94a3b8"; font.pixelSize: 16 }
            Label { text: maxNote; color: "#f8fafc"; font.pixelSize: 24; font.weight: Font.Bold }

            Label { text: "Current"; color: "#94a3b8"; font.pixelSize: 16 }
            Label { text: currentFreq.toFixed(1) + " Hz"; color: "#f8fafc"; font.pixelSize: 24; font.weight: Font.Bold }
        }
    }
}
