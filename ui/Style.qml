pragma Singleton

import QtQuick

QtObject {
    readonly property color background: "#0f172a"
    readonly property color surface: "#1e293b"
    readonly property color surfaceMuted: "#334155"
    readonly property color textPrimary: "#f8fafc"
    readonly property color textSecondary: "#94a3b8"
    readonly property color textMuted: "#64748b"
    readonly property color accent: "#3b82f6"
    readonly property color accentSecondary: "#6366f1"
    readonly property color success: "#22c55e"
    readonly property color danger: "#ef4444"

    readonly property int radiusSmall: 8
    readonly property int radiusLarge: 20
    readonly property int spacingSmall: 10
    readonly property int spacingMedium: 20
    readonly property int spacingLarge: 30
    readonly property int spacingXLarge: 40
}
