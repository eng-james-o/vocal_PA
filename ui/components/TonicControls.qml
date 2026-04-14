import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ColumnLayout {
    spacing: 20
    Layout.alignment: Qt.AlignHCenter

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
        contentItem: Text {
            text: parent.text
            color: "white"
            font.pixelSize: 16
            font.weight: Font.Medium
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
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
            padding: 8
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
            contentItem: Text {
                text: parent.text
                color: "white"
                font.pixelSize: 14
                font.weight: Font.Medium
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }
        }
    }
}
