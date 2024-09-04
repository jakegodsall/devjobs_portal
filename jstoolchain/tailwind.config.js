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
        "primary-purple": "var(--primary-purple)",
        "secondary-purple": "var(--secondary-purple)"
      },
      fontFamily: {
        epilogue: ["Epilogue", "system-ui"]
      }
    },
  },
  plugins: [],
};
