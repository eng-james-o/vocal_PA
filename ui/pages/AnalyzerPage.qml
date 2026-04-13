import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "../components"

ColumnLayout {
    anchors.fill: parent
    anchors.margins: 40
    spacing: 30

    // Header
    RowLayout {
        Layout.fillWidth: true
        Label {
            text: "Vocal Range Analyzer"
            font.pixelSize: 32
            font.weight: Font.Bold
            color: "#f8fafc"
        }
        Item { Layout.fillWidth: true }
        Button {
            text: core.currentFreq > 0 ? "Stop Session" : "Start Session"
            onClicked: {
                if (core.currentFreq > 0) core.stopSession()
                else core.startSession()
            }
            contentItem: Text {
                text: parent.text
                color: "white"
                font.pixelSize: 16
                font.weight: Font.Medium
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }
            background: Rectangle {
                implicitWidth: 140
                implicitHeight: 44
                radius: 8
                color: parent.pressed ? "#1e293b" : (core.currentFreq > 0 ? "#ef4444" : "#3b82f6")
            }
        }
    }

    // Main Display Area
    RowLayout {
        Layout.fillWidth: true
        Layout.fillHeight: true
        spacing: 40

        // Left Side: Pitch & Tonic
        ColumnLayout {
            Layout.preferredWidth: parent.width * 0.6
            spacing: 20

            PitchDisplay {
                solfa: core.currentSolfa
                note: core.currentNote
                gain: core.currentGain
            }

            TonicControls {}
        }

        // Right Side: Range Info
        RangeDisplay {
            minNote: core.minNote
            maxNote: core.maxNote
            currentFreq: core.currentFreq
        }
    }

    // Footer / Status
    Label {
        text: "Status: " + (core.currentFreq > 0 ? "Analyzing..." : "Ready")
        color: "#64748b"
        font.pixelSize: 14
    }
}
