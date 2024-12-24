/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}", // Ajoutez cette ligne pour inclure tous vos fichiers Angular
  ],
  theme: {
    extend: {
      colors: {
        fonce : '#5DA5B9',
        clair: '#D3E7E8',
        blanc: '#FFFFFF',
        
      },
    },
  },
  plugins: [],
};


