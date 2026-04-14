import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import ui 1.0
import pages 1.0

Window {
    width: 900
    height: 600
    visible: true
    title: "Vocal Range Analyzer"
    color: Style.background

    AnalyzerPage {
        anchors.fill: parent
    }
}
