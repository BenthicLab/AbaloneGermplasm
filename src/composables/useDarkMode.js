import { ref, watch } from 'vue';

const isDark = ref(localStorage.getItem('darkMode') === 'true');

function applyDarkMode() {
  if (isDark.value) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
}

applyDarkMode();

watch(isDark, (val) => {
  localStorage.setItem('darkMode', val);
  applyDarkMode();
});

export function useDarkMode() {
  function toggle() {
    isDark.value = !isDark.value;
  }

  return { isDark, toggle };
}