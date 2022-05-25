/* eslint-disable no-undef */
const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#0fa9e6', // brand
          light: '#3fbaeb', // brand-light
          dark: '#0c87b8', // brand-dark
        },
      },
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
    },
  },
  variants: {
    extend: {
      backgroundColor: ['active'], // enable the active focus state variant
    },
  },
  plugins: [require('@tailwindcss/forms')],
};
