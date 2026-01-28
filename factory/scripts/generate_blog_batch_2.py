
import os

blog_template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | AV Pool Bros News</title>
    <meta name="description" content="{description}">
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://avpoolbros.com/blog/{slug}/">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="/images/av-pool-bros-logo.png">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
    
    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    
    <link rel="stylesheet" href="/css/styles.css?v=2.1">
    <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16x16.png">
</head>

<body>

    <!-- Header -->
    <header>
        <div class="container">
            <a href="/" class="logo">AV <span>Pool Bros</span></a>
            <nav class="nav-menu">
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/services/">Services</a></li>
                    <li><a href="/about/">About Us</a></li>
                    <li><a href="/news/" class="active">News</a></li>
                    <li><a href="/contact/">Contact</a></li>
                </ul>
            </nav>
            <div class="header-actions">
                <a href="tel:6614984444" class="phone-link mobile-hide"><i class="fas fa-phone"></i> (661) 498-4444</a>
                <a href="/contact/" class="btn btn-primary">Get Free Quote</a>
                <button class="mobile-menu-btn" aria-label="Toggle navigation"><i class="fas fa-bars"></i></button>
            </div>
        </div>
    </header>

    <!-- Page Hero -->
    <section class="page-hero" style="background-image: linear-gradient(rgba(0, 119, 190, 0.9), rgba(0, 119, 190, 0.8)), url('/images/pool-blue-hero.png'); padding: 80px 0; background-size: cover; background-position: center;">
        <div class="container" style="text-align: center;">
            <span style="color: #b0e0e6; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; font-size: 0.9rem;">{category}</span>
            <h1 style="color: white; font-size: 3rem; margin-top: 10px; max-width: 900px; margin-left: auto; margin-right: auto;">{title}</h1>
            <p style="color: rgba(255,255,255,0.9); margin-top: 15px;">Published by AV Pool Bros</p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 60px 0; background: #fff;">
        <div class="container" style="max-width: 800px;">
            <div class="blog-content" style="line-height: 1.8; color: #444; font-size: 1.1rem;">
                <p class="lead" style="font-size: 1.3rem; color: #0077be; font-weight: 600; margin-bottom: 30px;">
                    {lead_text}
                </p>
                
                {content_body}

                <div style="background: #f0faff; padding: 30px; border-left: 5px solid #0077be; margin: 40px 0; border-radius: 4px;">
                    <h3 style="margin-top: 0; color: #0077be;">Ready for Crystal Clear Water?</h3>
                    <p style="margin-bottom: 15px;">We serve the entire Antelope Valley with professional pool cleaning and maintenance.</p>
                    <a href="tel:6614984444" class="btn btn-primary">Call (661) 498-4444</a>
                </div>

                <hr style="margin: 50px 0; border: 0; border-top: 1px solid #eee;">
                
                <div style="font-size: 0.9rem; color: #666;">
                    <p><strong>Tags:</strong> {tags}</p>
                    <p><a href="/news/">&larr; Back to All Articles</a></p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="av-cta-section" style="padding: 80px 0; text-align: center; background: linear-gradient(rgba(0, 119, 190, 0.95), rgba(0, 119, 190, 0.95)), url('/images/pool-blue-hero.png'); background-size: cover; background-position: center; color: white;">
        <div class="container">
            <h2 style="font-size: 2.5rem; margin-bottom: 20px; color: white;">Need a Professional Pool Tech?</h2>
            <p style="font-size: 1.2rem; margin-bottom: 30px; opacity: 0.9;">
                Get your free estimate today. Weekly service available in Palmdale & Lancaster.
            </p>
            <a href="tel:6614984444" class="btn btn-secondary" style="font-size: 1.3rem; padding: 18px 50px; background: white; color: #0077be; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">
                Call (661) 498-4444
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="aw-footer">
        <div class="container aw-footer-inner">
            <div class="aw-footer-brand">
                <img src="/images/av-pool-bros-logo.png" alt="AV Pool Bros Logo" style="max-width: 250px; margin-bottom: 15px;">
                <p>Your trusted pool maintenance provider in the Antelope Valley.</p>
            </div>
            <div class="aw-footer-contact">
                <h4 style="color: white; margin-bottom: 15px; font-size: 1.1rem;">Contact Us</h4>
                <p class="aw-footer-phone"><a href="tel:6614984444">(661) 498-4444</a></p>
                <p class="aw-footer-email">Palmdale & Lancaster</p>
            </div>
            <div class="aw-footer-services">
                <h4>Our Services</h4>
                <ul>
                    <li><a href="/services/pool-cleaning/">Pool Cleaning</a></li>
                    <li><a href="/services/chemical-balancing/">Chemical Balancing</a></li>
                    <li><a href="/services/filter-equipment-repair/">Equipment Repair</a></li>
                </ul>
            </div>
            <div class="aw-footer-locations">
                <h4>Service Areas</h4>
                <ul>
                    <li><a href="/locations/palmdale/">Palmdale, CA</a></li>
                    <li><a href="/locations/lancaster/">Lancaster, CA</a></li>
                    <li><a href="/locations/quartz-hill/">Quartz Hill</a></li>
                </ul>
            </div>
        </div>
        <div class="aw-footer-bottom">
            <p>© <span id="year"></span> AV Pool Bros. All rights reserved. | <a href="/privacy/">Privacy Policy</a> | <a href="/terms/">Terms of Service</a></p>
        </div>
    </footer>
    <script src="/js/script.js"></script>
</body>
</html>
"""

articles = [
    {
        "slug": "green-to-clean-recovery-west-lancaster",
        "title": "Green-to-Clean Success in West Lancaster: A Before & After",
        "category": "Project Spotlight",
        "description": "See how we transformed a neglected 'swamp pool' in West Lancaster back to sparkling blue in just 3 visits.",
        "lead_text": "A homeowner in West Lancaster recently called us after their pool had been neglected for months. The water was dark green and opaque. Our Green-to-Clean process saved the day without a full drain and refill.",
        "tags": "Green-to-Clean, Lancaster, Algae Recovery, Project Spotlight",
        "content_body": '''
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">The Challenge: High Phosphate Algae Bloom</h2>
            <p>During the intense Antelope Valley summer heat, algae can take hold faster than most people realize. This pool was a breeding ground for mosquitoes and a major eyesore. The phosphate levels were off the charts due to local wind and dust.</p>
            
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">The AV Pool Bros Solution</h2>
            <p>Our three-visit recovery process included:</p>
            <ul style="margin-bottom: 30px; list-style-type: none; padding-left: 0;">
                <li style="margin-bottom: 10px; padding-left: 20px; position: relative;"><i class="fas fa-check" style="color: #0077be; position: absolute; left: 0; top: 5px;"></i> <strong>Visit 1:</strong> Chemical shock and phosphate removal.</li>
                <li style="margin-bottom: 10px; padding-left: 20px; position: relative;"><i class="fas fa-check" style="color: #0077be; position: absolute; left: 0; top: 5px;"></i> <strong>Visit 2:</strong> Flocculation and vacuuming debris to waste.</li>
                <li style="margin-bottom: 10px; padding-left: 20px; position: relative;"><i class="fas fa-check" style="color: #0077be; position: absolute; left: 0; top: 5px;"></i> <strong>Visit 3:</strong> Filter deep clean and final chemical balancing.</li>
            </ul>

            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">The Result: Crystal Clear Blue</h2>
            <p>By day five, the pool was museum-quality clear. The homeowner avoided the massive expense of a water truck and potential damage to the plaster from a drain. <strong>"I thought it was beyond hope, but AV Pool Bros made it look new again!"</strong></p>
            
            <p>Dealing with a green pool? <a href="/services/green-to-clean/" style="color: #0077be; font-weight: 600;">Check out our Green-to-Clean service page</a>.</p>
        '''
    },
    {
        "slug": "energy-efficient-pool-equipment-palmdale",
        "title": "Slashing Your SCE Bill: Energy Efficient Pool Pumps in Palmdale",
        "category": "Expert Advice",
        "description": "Learn how variable speed pumps can save Antelope Valley homeowners hundreds of dollars a year on energy bills compared to old single-speed units.",
        "lead_text": "With Southern California Edison (SCE) rates rising, your pool pump could be the most expensive appliance in your home. Switching to a variable speed pump is the fastest way to save money.",
        "tags": "Energy Efficiency, Pool Pumps, Palmdale, SCE Savings",
        "content_body": '''
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">Why Single Speed Pumps Fail</h2>
            <p>Old-fashioned single speed pumps have two modes: ON and OFF. They run at maximum RPM even when just filtering, which is like driving your car at 100mph just to go to the grocery store. It's loud and incredibly wasteful.</p>
            
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">The Variable Speed Advantage</h2>
            <p>Modern variable speed pumps can be programmed to run at lower, whisper-quiet speeds for most of the day. This uses up to 80% less electricity while actually improving filtration quality. Most units pay for themselves in electricity savings within 18 months.</p>

            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">Pro Tip for Palmdale Residents</h2>
            <p>During wind storms, you can temporarily increase the RPM to ensure the skimmers catch all the dust, then drop it back down for standard maintenance. It's smart pool care for the High Desert.</p>
            
            <p>Ready to upgrade? <a href="/services/filter-equipment-repair/" style="color: #0077be; font-weight: 600;">Explore our equipment installation services</a>.</p>
        '''
    },
    {
        "slug": "high-desert-filter-maintenance-guide",
        "title": "Sand, DE, or Cartridge? Filter Maintenance in the High Desert",
        "category": "Technical Guide",
        "description": "Understanding which pool filter type handles the Antelope Valley dust the best, and how to maintain them for maximum efficiency.",
        "lead_text": "Dust is the enemy of any High Desert pool. Your filter is your first line of defense, and knowing how to maintain it is critical for water clarity.",
        "tags": "Pool Filters, DE Filter, Cartridge Cleaning, Maintenance",
        "content_body": '''
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">Why DE Filters Rule in the AV</h2>
            <p>Diatomaceous Earth (DE) filters filter down to 3-5 microns, capturing the ultra-fine dust that blows in from the desert floor. While they require more maintenance than cartrige filters, they provide the clearest water results in our specific environment.</p>
            
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">Cartridge Filter Care</h2>
            <p>If you have cartridge filters, they need to be broken down and pressure washed at least twice a year—ideally after the spring wind season. Ignoring this leads to high pressure, poor circulation, and ultimately a failed pump motor.</p>
            
            <h2 style="color: #0077be; margin-top: 40px; margin-bottom: 20px;">The Importance of Backwashing</h2>
            <p>For DE and Sand filters, regular backwashing is mandatory after high-use weekends or dust storms. Always remember to recharge your DE after backwashing to protect the grids.</p>
        '''
    }
]

def generate_articles():
    base_dir = "blog"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    for article in articles:
        # Create directory
        article_dir = os.path.join(base_dir, article['slug'])
        if not os.path.exists(article_dir):
            os.makedirs(article_dir)
            
        # Create HTML
        html_content = blog_template.format(
            title=article['title'],
            description=article['description'],
            slug=article['slug'],
            category=article['category'],
            lead_text=article['lead_text'],
            content_body=article['content_body'],
            tags=article['tags']
        )
        
        # Write file
        file_path = os.path.join(article_dir, "index.html")
        with open(file_path, "w") as f:
            f.write(html_content)
        
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    generate_articles()
