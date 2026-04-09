console.log('[GlanceLib/LIOD] Library: "Load iFrame on demand".');

document.addEventListener('DOMContentLoaded', function() {
    console.log('[GlanceLib/LIOD] Initializing...');
    const observedElements = [];
    const glanceMainElement = document.querySelector("main#page");

    const intersectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const container = entry.target;
            if (entry.isIntersecting) {
                if (!container.querySelector('iframe')) {
                    const iframe = document.createElement('iframe');
                    iframe.src = container.dataset.libLiodSrc;
                    iframe.className = container.dataset.libLiodClasses;
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
    const mutationObserver = new MutationObserver((mutationList) => {
        for (const mutation of mutationList) {
            if (mutation.type !== "attributes") continue;
            console.log("Mutation on main#page: ", mutation);
            console.log(document.getElementsByTagName('body')[0].innerHTML);
        }
        /* document.querySelectorAll('div[data-lib-liod]').forEach(elem => {
            if (!observedElements.includes(elem)) {
                console.log('[GlanceLib/LIOD] Observing: ', elem);
                elem.classList.add('glance-lib-liod')
                intersectionObserver.observe(elem);
                observedElements.push(elem);
            }
        });*/
        console.log('[GlanceLib/LIOD] Initialized.');
    });

    console.log("Waiting for Glance page to fully load...");
    mutationObserver.observe(glanceMainElement, {
        attributes: true
    });
});