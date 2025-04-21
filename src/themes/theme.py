from textual.theme import Theme

darkwave_theme = Theme(
    name="darkwave",

    # BRANDING COLORS
    primary="#4E9093",  # Highlighted command (keyword-style blue)
    secondary="#AAABA8",  # Label and subtext, softer than primary
    accent="#5AB0B2",  # Border glow, used sparingly for separation

    # TEXT COLORS
    foreground="#9E9F9C",  # General text (good contrast on dark bg)

    # BACKGROUND COLORS
    background="#181E24",  # App background (screen base)
    surface="#26272D",  # Default widget background
    panel="#23262E",  # Slightly distinct panel areas (e.g. command list)

    # STATUS COLORS
    success="#1a1e26",  # Can be used for positive visual cues
    warning="#151820",  # Use for mild warning states or emphasis (not nav!)
    error="#bf616a",  # Only for real errors — not used in layout

    dark=True,
    variables={
        "block-cursor-text-style": "none",
        "footer-key-foreground": "#88C0D0",
        "input-selection-background": "#81a1c1 35%",
    },
)