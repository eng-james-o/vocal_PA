import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "../ui/pages"

Window {
    width: 900
    height: 600
    visible: true
    title: "Vocal Range Analyzer"
    color: "#0f172a" // Slate 950

    AnalyzerPage {
        anchors.fill: parent
    }
}
