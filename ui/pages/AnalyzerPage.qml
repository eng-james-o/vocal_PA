import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import ui 1.0
import components 1.0

ColumnLayout {
    anchors.fill: parent
    anchors.margins: Style.spacingXLarge
    spacing: Style.spacingLarge

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
            text: core.isSessionRunning ? "Stop Session" : "Start Session"
            onClicked: {
                if (core.isSessionRunning) core.stopSession()
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
                radius: Style.radiusSmall
                color: parent.pressed ? Style.surface : (core.isSessionRunning ? Style.danger : Style.accent)
            }
        }
    }

    // Main Display Area
    RowLayout {
        Layout.fillWidth: true
        Layout.fillHeight: true
        spacing: Style.spacingXLarge

        // Left Side: Pitch & Tonic
        ColumnLayout {
            Layout.fillWidth: true
            Layout.preferredWidth: 520
            spacing: Style.spacingMedium

            PitchDisplay {
                solfa: core.currentSolfa
                note: core.currentNote
                gain: core.currentGain
            }
            
            TonicControls {}
        }

        // Right Side: Range Info
        RangeDisplay {
            Layout.preferredWidth: 280
            Layout.fillHeight: true
            minNote: core.minNote
            maxNote: core.maxNote
            currentFreq: core.currentFreq
        }
    }

    // Footer / Status
    Label {
        text: "Status: " + core.statusMessage
        color: Style.textMuted
        font.pixelSize: 14
    }
}
