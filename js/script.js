// Basic interactions scripts
document.addEventListener('DOMContentLoaded', () => {
    console.log('AV Pool Bros site loaded');

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Mobile Menu Toggle
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const navMenu = document.querySelector('.nav-menu');
    const icon = mobileBtn ? mobileBtn.querySelector('i') : null;

    if (mobileBtn && navMenu) {
        mobileBtn.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent bubbling
            navMenu.classList.toggle('active');

            // Toggle icon
            if (icon) {
                if (navMenu.classList.contains('active')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-times');
                } else {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });

        // Close menu when clicking a link
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                if (icon) {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (navMenu.classList.contains('active') && !navMenu.contains(e.target) && !mobileBtn.contains(e.target)) {
                navMenu.classList.remove('active');
                if (icon) {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });
    }


    // Dynamic Year in Footer
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // FAQ Accordion Functionality
    document.querySelectorAll('.accordion-header').forEach(header => {
        header.addEventListener('click', function () {
            const item = this.parentElement;
            const content = item.querySelector('.accordion-content');
            const icon = this.querySelector('i');

            // Toggle active class
            item.classList.toggle('active');

            // Toggle content visibility
            if (item.classList.contains('active')) {
                content.style.maxHeight = content.scrollHeight + 'px';
                if (icon) icon.style.transform = 'rotate(180deg)';
            } else {
                content.style.maxHeight = '0';
                if (icon) icon.style.transform = 'rotate(0deg)';
            }
        });
    });

    // Comparison Slider Logic (Enhanced with Mobile Support)
    document.querySelectorAll('.av-yard-ba-slider').forEach(slider => {
        const range = slider.querySelector('.av-yard-range');
        const after = slider.querySelector('.av-yard-after');
        const divider = slider.querySelector('.av-yard-divider');
        const handle = slider.querySelector('.av-yard-handle');

        function update(val) {
            try {
                const clampedVal = Math.max(0, Math.min(100, val));
                if (after) after.style.clipPath = `inset(0 0 0 ${clampedVal}%)`;
                if (divider) divider.style.left = clampedVal + '%';
                if (handle) handle.style.left = clampedVal + '%';
            } catch (e) {
                console.error('Slider update error:', e);
            }
        }

        if (range && after && divider && handle) {
            // Initialize
            update(range.value || 50);

            // Desktop: input event
            range.addEventListener('input', e => update(e.target.value));

            // Mobile: touch events for better responsiveness
            range.addEventListener('touchstart', e => {
                e.preventDefault();
            }, { passive: false });

            range.addEventListener('touchmove', e => {
                e.preventDefault();
                const touch = e.touches[0];
                const rect = range.getBoundingClientRect();
                const percent = Math.max(0, Math.min(100, ((touch.clientX - rect.left) / rect.width) * 100));
                range.value = percent;
                update(percent);
            }, { passive: false });
        }
    });

    // Painting Quote Modal (DISABLED FOR NOW)
    /*
    setTimeout(() => {
        // Check if user has already seen the popup in this session
        if (sessionStorage.getItem('av-popup-shown')) {
            return;
        }
    
        // Create modal HTML
        const modalHTML = `
            <div id="av-security-modal" style="
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.8);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 10000;
                animation: fadeIn 0.3s ease-in-out;
            ">
                <div style="
                    background: white;
                    border-radius: 12px;
                    max-width: 500px;
                    width: 90%;
                    padding: 40px 30px;
                    position: relative;
                    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
                    text-align: center;
                ">
                    <button id="av-modal-close" style="
                        position: absolute;
                        top: 15px;
                        right: 15px;
                        background: none;
                        border: none;
                        font-size: 28px;
                        cursor: pointer;
                        color: #666;
                        line-height: 1;
                        padding: 0;
                        width: 30px;
                        height: 30px;
                    ">&times;</button>
                    
                    <img src="/images/escobedo-painting-logo.webp" alt="Escobedo Painting" style="
                        width: 120px;
                        height: 120px;
                        border-radius: 50%;
                        object-fit: contain;
                        margin: 0 auto 20px;
                        display: block;
                        border: 4px solid var(--primary-gold, #D4AF37);
                        padding: 10px;
                        background: var(--primary-navy, #0A1628);
                    ">
                    
                    <h3 style="
                        font-size: 1.8rem;
                        color: #1a1a1a;
                        margin-bottom: 15px;
                        font-weight: 700;
                    ">Planning a Painting Project?</h3>
                    
                    <p style="
                        font-size: 1.1rem;
                        color: #666;
                        margin-bottom: 25px;
                        line-height: 1.6;
                    ">We are booking estimates for Spring and Summer interior and exterior painting. Secure your spot on our calendar today!</p>
                    
                    <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                        <a href="tel:6615557890" style="
                            background: linear-gradient(135deg, #D4AF37 0%, #F5E6D3 100%);
                            color: #1a1a1a;
                            padding: 15px 30px;
                            border-radius: 8px;
                            text-decoration: none;
                            font-weight: 700;
                            font-size: 1.1rem;
                            display: inline-block;
                            transition: transform 0.2s;
                        " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                            📞 Call (661) 555-7890
                        </a>
                        <a href="/contact/" style="
                            background: #0A1628;
                            color: white;
                            padding: 15px 30px;
                            border-radius: 8px;
                            text-decoration: none;
                            font-weight: 700;
                            font-size: 1.1rem;
                            display: inline-block;
                            transition: transform 0.2s;
                        " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                            Get Free Quote
                        </a>
                    </div>
                </div>
            </div>
        `;
    
        // Add fade-in animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        `;
        document.head.appendChild(style);
    
        // Insert modal into page
        document.body.insertAdjacentHTML('beforeend', modalHTML);
    
        // Mark as shown in session
        sessionStorage.setItem('av-popup-shown', 'true');
    
        // Close button functionality
        const modal = document.getElementById('av-security-modal');
        const closeBtn = document.getElementById('av-modal-close');
    
        closeBtn.addEventListener('click', () => {
            modal.style.animation = 'fadeOut 0.3s ease-in-out';
            setTimeout(() => modal.remove(), 300);
        });
    
        // Close on background click
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.style.animation = 'fadeOut 0.3s ease-in-out';
                setTimeout(() => modal.remove(), 300);
            }
        });
    
        // Add fade-out animation
        style.textContent += `
            @keyframes fadeOut {
                from { opacity: 1; }
                to { opacity: 0; }
            }
        `;
    }, 5000);
    */
    // Fence Restoration Slider Logic
    const baRange = document.getElementById('ba-range');
    const beforeImage = document.getElementById('before-image');
    if (baRange && beforeImage) {
        baRange.addEventListener('input', (e) => {
            beforeImage.style.width = e.target.value + '%';
        });
        // Initial state
        beforeImage.style.width = baRange.value + '%';
    }
});
