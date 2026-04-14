# User Workflows

This guide walks you through the primary use cases of the Vocal Range Analyzer.

## 1. Initial Calibration (Set Your DOH)

Before any session, you must calibrate the system to your "tonic" or "DOH". This allows the analyzer to display your pitch in relative solfa notation.

```mermaid
flowchart TD
    A[Start App] --> B[Calibration Screen]
    B --> C[Click 'Capture Tonic']
    C --> D[Sing your comfortable 'Do' for 2s]
    D --> E{Stable Pitch?}
    E -- No --> D
    E -- Yes --> F[System Saves Tonic Hz]
    F --> G[Navigate to Live Session]
```

**Tip**: Choose a pitch that feels like your "home" note for the day. For most beginners, this is near the bottom of their middle register.

## 2. Measuring Your Vocal Range

The Range Finder track your highest and lowest successfully sustained notes.

```mermaid
flowchart TD
    A[Open New Session] --> B[Select 'Range Finder' Mode]
    B --> C[Start Recording]
    C --> D[Sing lowest note possible]
    D --> E[Hold for 2 seconds]
    E --> F[Slide up to highest note]
    F --> G[Hold highest note for 2 seconds]
    G --> H[Stop Recording]
    H --> I[Review Range Summary]
    I --> J[Save to Profile]
```

**Important**: The system filters out quick spikes and breath noise. Ensure you *sustain* the note for the counter to register it.

## 3. Finding the Optimal Key for a Song

Use this workflow to transpose a song into your most comfortable register.

```mermaid
flowchart TD
    A[Go to Song Library] --> B[Enter Song's original Range]
    B --> C[e.g., Min: G3, Max: D5]
    C --> D[Analyzercompares to Your Range]
    D --> E[Recommendation Engine Runs]
    E --> F{Select Strategy}
    F -- Center --> G[Balances high/low comfort]
    F -- High --> H[Prioritizes high notes]
    G --> I[Output: '+2 Semitones']
    H --> I
    I --> J[Apply to Performance]
```

## 4. Troubleshooting Workflow

If you encounter "No Pitch Detected":
1.  **Check Hardware**: Is the mic selected in settings?
2.  **Environment**: Is there too much background noise?
3.  **Tonic Adjustment**: If Solfa feels "off", recalibrate your DOH.
4.  **Gain**: Ensure your input level isn't clipping (turning red).
