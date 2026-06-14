import { onMounted, onUnmounted, nextTick } from 'vue';

export function useScrollAnimation(options = {}) {
  const {
    threshold = 0.08,
    rootMargin = '0px 0px -60px 0px',
    triggerOnce = false, // 改为 false，支持上下双向动画
  } = options;

  let observer = null;
  let rafId = null;

  const initObserver = () => {
    if (observer) observer.disconnect();

    observer = new IntersectionObserver(
      (entries) => {
        // 使用 rAF 批量更新，避免布局抖动
        if (rafId) cancelAnimationFrame(rafId);
        rafId = requestAnimationFrame(() => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add('scroll-animate-visible');
            } else if (!triggerOnce) {
              entry.target.classList.remove('scroll-animate-visible');
            }
          });
        });
      },
      {
        threshold,
        rootMargin,
      }
    );

    const elements = document.querySelectorAll('.scroll-animate, .scroll-animate-left, .scroll-animate-right, .scroll-animate-scale');
    elements.forEach((el) => observer.observe(el));
  };

  onMounted(() => {
    nextTick(() => {
      setTimeout(initObserver, 150);
    });

    // 监听 DOM 变化（路由切换、动态内容）
    const mutationObserver = new MutationObserver(() => {
      setTimeout(initObserver, 200);
    });
    mutationObserver.observe(document.body, {
      childList: true,
      subtree: true,
    });

    onUnmounted(() => {
      mutationObserver.disconnect();
      if (observer) observer.disconnect();
      if (rafId) cancelAnimationFrame(rafId);
    });
  });

  const refresh = () => {
    setTimeout(initObserver, 200);
  };

  return { refresh };
}
