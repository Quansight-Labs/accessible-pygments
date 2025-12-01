// Get the <select> element
const select = document.querySelector("select");

// Get the current theme
let currentTheme = select.value;

// Whenever user chooses a new option from the <select> dropdown, reload all the
// iframes on the page with examples from the new chosen theme
select.addEventListener("change", (event) => {
  const nextTheme = event.currentTarget.value;
  document.querySelectorAll("iframe").forEach((element) => {
    // Replace theme name in URL to load example from new theme
    element.src = element.src.replace(currentTheme, nextTheme);
  });
  currentTheme = nextTheme;
});
