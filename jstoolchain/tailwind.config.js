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
        "form-text": "var(--form-text)",
        "blue-light": "var(--blue-light)",
        "blue-primary" : "var(--blue-primary)",
        "blue-darkest": "var(--blue-darkest)"
      },
      fontFamily: {
        epilogue: ["Epilogue", "system-ui"]
      }
    },
  },
  plugins: [],
};
