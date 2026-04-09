var loadIframeOnDemand = loadIframeOnDemand || function(containerId, iframeSrc, iframeClasses) {
    console.log("Executing loadIframeOnDemand", containerId, iframeSrc, iframeClasses)
    const container = document.getElementById(containerId);
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                if (!container.querySelector('iframe')) {
                    const iframe = document.createElement('iframe');
                    iframe.src = iframeSrc;
                    iframe.class = iframeClasses;
                    container.appendChild(iframe);
                    console.log("iframe loaded");
                }
            } else {
                const iframe = container.querySelector('iframe');
                if (iframe) {
                    iframe.remove();
                    console.log("iframe unloaded");
                }
            }
        });
    }, {
        threshold: 0.1
    })
    observer.observe(container);
}