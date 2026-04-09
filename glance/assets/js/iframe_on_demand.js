console.log('[GlanceLib/LIOD] Library: "Load iFrame on demand".');

window.document.onload = function(e) {
    console.log('[GlanceLib/LIOD] Initializing...');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const container = entry.target;
            if (entry.isIntersecting) {
                if (!container.querySelector('iframe')) {
                    const iframe = document.createElement('iframe');
                    iframe.src = container.getAttribute('data-lib-liod-src');
                    iframe.className = container.getAttribute('data-lib-liod-classes')
                    iframe.classList.add('glance-lib-liod');
                    container.appendChild(iframe);
                    console.log('iframe loaded');
                }
            } else {
                const iframe = container.querySelector('iframe');
                if (iframe) {
                    iframe.remove();
                    console.log('iframe unloaded');
                }
            }
        });
    }, {
        root: null,
        threshold: 0.1
    });
    document.querySelector('[data-lib-liod]').forEach(elem => {
        console.log('[GlanceLib/LIOD] Observing: ', elem);
        elem.classList.add('glance-lib-liod')
        observer.observe(elem);
    });
    console.log('[GlanceLib/LIOD] Initialized.');
}