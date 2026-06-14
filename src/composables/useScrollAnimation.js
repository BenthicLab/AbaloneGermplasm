import { onMounted, onBeforeUnmount, nextTick } from 'vue';

export function useScrollAnimation(options = {}) {
  const {
    threshold = 0.08,
    rootMargin = '0px 0px -60px 0px',
    triggerOnce = true,
  } = options;

  let observer = null;
  let rafId = null;
  let mutationObserver = null;

  const initObserver = () => {
    if (observer) observer.disconnect();

    observer = new IntersectionObserver(
      (entries) => {
        if (rafId) cancelAnimationFrame(rafId);
        rafId = requestAnimationFrame(() => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add('scroll-animate-visible');
              if (triggerOnce) {
                observer.unobserve(entry.target);
              }
            } else if (!triggerOnce) {
              entry.target.classList.remove('scroll-animate-visible');
            }
          });
        });
      },
      { threshold, rootMargin }
    );

    const elements = document.querySelectorAll('.scroll-animate, .scroll-animate-left, .scroll-animate-right, .scroll-animate-scale');
    elements.forEach((el) => observer.observe(el));
  };

  onMounted(() => {
    nextTick(() => {
      setTimeout(initObserver, 150);
    });

    mutationObserver = new MutationObserver(() => {
      setTimeout(initObserver, 200);
    });
    mutationObserver.observe(document.body, {
      childList: true,
      subtree: true,
    });
  });

  onBeforeUnmount(() => {
    if (observer) observer.disconnect();
    if (rafId) cancelAnimationFrame(rafId);
    if (mutationObserver) mutationObserver.disconnect();
  });

  const refresh = () => {
    setTimeout(initObserver, 200);
  };

  return { refresh };
}
