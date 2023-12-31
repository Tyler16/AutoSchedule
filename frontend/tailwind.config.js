/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      spacing: {
        '1/12': '8.333333%',
        '5/12': '41.666667%',
        '7/12': '58%',
        '11/12': '91.666667%',
        '5/8': '62.5%'
      }
    },
  },
  plugins: [],
}

