/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/**/*.html",
    "../job_portal/templates/**/*.html",
    "../users/templates/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        "main-text": "var(--main-text)",
        "secondary-text": "var(--secondary-text)",
        "main-background": "var(--main-background)",
      },
    },
  },
  plugins: [],
};
