import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Effects

Window {
    width: 900
    height: 600
    visible: true
    title: "Vocal Range Analyzer"
    color: "#0f172a" // Slate 950

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

            // Pitch Info
            ColumnLayout {
                Layout.preferredWidth: parent.width * 0.6
                spacing: 20

                Rectangle {
                    Layout.fillWidth: true
                    Layout.preferredHeight: 250
                    color: "#1e293b"
                    radius: 20
                    
                    ColumnLayout {
                        anchors.centerIn: parent
                        spacing: 10
                        
                        Label {
                            text: core.currentSolfa || "---"
                            font.pixelSize: 84
                            font.weight: Font.Black
                            color: "#3b82f6"
                            Layout.alignment: Qt.AlignHCenter
                        }

                        
                        Label {
                            text: core.currentNote || "Silence"
                            font.pixelSize: 24
                            font.weight: Font.Medium
                            color: "#94a3b8"
                            Layout.alignment: Qt.AlignHCenter
                        }

                        // Gain Meter
                        RowLayout {
                            Layout.preferredWidth: 200
                            Layout.alignment: Qt.AlignHCenter
                            spacing: 10
                            Rectangle {
                                Layout.fillWidth: true
                                height: 4
                                color: "#334155"
                                radius: 2
                                Rectangle {
                                    width: parent.width * Math.min(core.currentGain * 5, 1.0)
                                    height: parent.height
                                    color: core.currentGain > 0.2 ? "#ef4444" : "#22c55e"
                                    radius: 2
                                }
                            }
                        }
                    }
                }
                
                Button {
                    text: "Calibrate DOH"
                    Layout.alignment: Qt.AlignHCenter
                    onClicked: core.calibrateTonic()
                    enabled: core.currentFreq > 0
                    background: Rectangle {
                        implicitWidth: 200
                        implicitHeight: 44
                        radius: 8
                        color: parent.enabled ? "#6366f1" : "#334155"
                    }
                }


                RowLayout {
                    Layout.alignment: Qt.AlignHCenter
                    spacing: 10
                    TextField {
                        id: tonicInput
                        placeholderText: "e.g., C4"
                        width: 80
                        background: Rectangle {
                            color: "#1e293b"
                            border.color: "#334155"
                            radius: 4
                        }
                        color: "white"
                    }
                    Button {
                        text: "Set Tonic"
                        onClicked: core.setTonicByName(tonicInput.text)
                        background: Rectangle {
                            implicitWidth: 100
                            implicitHeight: 36
                            radius: 8
                            color: parent.pressed ? "#1e293b" : "#3b82f6"
                        }
                    }
                }
            }

            // Range Info
            ColumnLayout {
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
                        Label { text: core.minNote; color: "#f8fafc"; font.pixelSize: 24; font.weight: Font.Bold }
                        
                        Label { text: "Highest"; color: "#94a3b8"; font.pixelSize: 16 }
                        Label { text: core.maxNote; color: "#f8fafc"; font.pixelSize: 24; font.weight: Font.Bold }
                        
                        Label { text: "Current"; color: "#94a3b8"; font.pixelSize: 16 }
                        Label { text: core.currentFreq.toFixed(1) + " Hz"; color: "#f8fafc"; font.pixelSize: 24; font.weight: Font.Bold }
                    }
                }
            }
        }

        // Footer / Status
        Label {
            text: "Status: " + (core.currentFreq > 0 ? "Analyzing..." : "Ready")
            color: "#64748b"
            font.pixelSize: 14
        }
    }
}
