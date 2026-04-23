export const theme = {
  colors: {
    background: '#15121b',
    surface: '#15121b',
    surfaceDim: '#15121b',
    surfaceBright: '#3c3742',
    surfaceContainerLowest: '#100d16',
    surfaceContainerLow: '#1d1a24',
    surfaceContainer: '#221e28',
    surfaceContainerHigh: '#2c2833',
    surfaceContainerHighest: '#37333e',
    topbar: '#181818',

    primary: '#d2bbff',
    primaryContainer: '#7c3aed',
    primaryFixed: '#eaddff',
    primaryFixedDim: '#d2bbff',
    onPrimary: '#3f008e',
    onPrimaryContainer: '#ede0ff',
    onPrimaryFixedVariant: '#5a00c6',
    inversePrimary: '#732ee4',

    secondary: '#89ceff',
    secondaryContainer: '#00a2e6',
    secondaryFixed: '#c9e6ff',
    secondaryFixedDim: '#89ceff',
    onSecondary: '#00344d',
    onSecondaryContainer: '#00344e',
    onSecondaryFixed: '#001e2f',
    onSecondaryFixedVariant: '#004c6e',

    tertiary: '#ffb784',
    tertiaryContainer: '#a15100',
    tertiaryFixed: '#ffdcc6',
    tertiaryFixedDim: '#ffb784',
    onTertiary: '#4f2500',
    onTertiaryContainer: '#ffe0cd',
    onTertiaryFixed: '#301400',
    onTertiaryFixedVariant: '#713700',

    error: '#ffb4ab',
    errorContainer: '#93000a',
    onError: '#690005',
    onErrorContainer: '#ffdad6',

    onBackground: '#e8dfee',
    onSurface: '#e8dfee',
    onSurfaceVariant: '#ccc3d8',
    inverseSurface: '#e8dfee',
    inverseOnSurface: '#332f39',

    outline: '#958da1',
    outlineVariant: '#4a4455',
    surfaceTint: '#d2bbff',
    surfaceVariant: '#37333e',
  },

  typography: {
    bodySm: {
      family: "'Inter', sans-serif",
      size: '12px',
      lineHeight: '16px',
      weight: '400',
    },
    displayMono: {
      family: "'JetBrains Mono', monospace",
      size: '24px',
      lineHeight: '32px',
      letterSpacing: '-0.02em',
      weight: '600',
    },
    labelCaps: {
      family: "'Inter', sans-serif",
      size: '10px',
      lineHeight: '12px',
      letterSpacing: '0.05em',
      weight: '700',
    },
    dataTabular: {
      family: "'JetBrains Mono', monospace",
      size: '11px',
      lineHeight: '14px',
      weight: '500',
    },
  },

  spacing: {
    unit: '4px',
    xs: '4px',
    sm: '8px',
    md: '12px',
    lg: '16px',
    panelPadding: '12px',
    gutter: '1px',
  },

  radii: {
    default: '2px',
    lg: '4px',
    xl: '8px',
    full: '12px',
  },
} as const

export type Theme = typeof theme
