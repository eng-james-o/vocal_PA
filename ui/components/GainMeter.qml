import QtQuick
import QtQuick.Layouts

RowLayout {
    property real gain: 0.0
    Layout.preferredWidth: 200
    Layout.alignment: Qt.AlignHCenter
    spacing: 10
    
    Rectangle {
        Layout.fillWidth: true
        height: 4
        color: "#334155"
        radius: 2
        Rectangle {
            width: parent.width * Math.min(gain * 5, 1.0)
            height: parent.height
            color: gain > 0.2 ? "#ef4444" : "#22c55e"
            radius: 2
        }
    }
}
