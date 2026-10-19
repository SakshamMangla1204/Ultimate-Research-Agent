export default {
  content: ['./index.html', './src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        flux: {
          bg: '#0B0D10',
          sidebar: '#090B0E',
          surface: '#11151A',
          surface2: '#151A20',
          text: '#F0F3F5',
          secondary: '#939CA8',
          muted: '#606A76',
          border: '#252C34',
          cyan: '#75E6F7',
          secondaryC: '#B5F2FA',
          green: '#7DD8B0',
          red: '#FF8A8A',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['ui-monospace', 'SF Mono', 'Consolas', 'monospace'],
      },
      borderRadius: {
        'none': '0px',
        'sm': '2px',
        'md': '4px',
        'lg': '6px',
      },
      spacing: {
        '96': '24rem',
        '128': '32rem',
      },
    },
  },
  plugins: [],
};
