
import os

# New footer section with granular keywords
neighborhood_block = """
                    <!-- Neighborhoods SEO Block -->
                    <div class="aw-footer-neighborhoods" style="margin-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px;">
                        <h4 style="font-size: 0.9rem; color: #aaa; margin-bottom: 10px;">Neighborhoods Served</h4>
                        <p style="font-size: 0.8rem; color: #888; line-height: 1.6;">
                            West Lancaster • East Palmdale • Quartz Hill • Rancho Vista • Anaverde • Sun Village • 
                            Littlerock • Pearblossom • Lake Los Angeles • Leona Valley • Rosamond • Antelope Acres • 
                            White Fence Farms • Desert View Highlands • Joshua Ranch
                        </p>
                    </div>
"""

def update_footer(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Avoid duplicate injection
    if "West Lancaster • East Palmdale" in content:
        print(f"Skipping {filepath}: Already has neighborhood block.")
        return

    # Targeting the end of the inner footer container
    target = '                    </div>\n\n                </div>\n\n                <!-- Bottom Bar -->'
    
    if target not in content:
        # Fallback target if formatting is slightly different
        target = '</div>\n                </div>\n                <div class="aw-footer-bottom">'
        if target not in content:
             # loose target
            target = '<div class="aw-footer-bottom">'
            
            if target in content:
                 # Insert before bottom bar
                new_content = content.replace(target, neighborhood_block + '\n' + target)
            else:
                print(f"Could not find footer target in {filepath}")
                return
    else:
        # Precision replacement
        new_content = content.replace(target, neighborhood_block + '\n' + target)

    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Updated footer in {filepath}")

def main():
    for root, dirs, files in os.walk("."):
        if ".git" in root or ".gemini" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                update_footer(os.path.join(root, file))

if __name__ == "__main__":
    main()
