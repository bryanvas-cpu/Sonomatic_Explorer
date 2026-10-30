# Sonomatic Product & Service Explorer

## Open locally

1. Extract the ZIP completely.
2. Double-click **index.html**, or open **docs/index.html** in Chrome, Firefox or Edge.
3. **sonomatic_bloom.html** is a single-file alternative with all map code, data and images embedded. The Photos link still opens the bundled gallery.

No installation, account, server or build is required. Diagram, search, details, photos and list view work offline. Official source links need internet access.

## Publish with GitHub Pages

1. Create a GitHub repository, for example `Sonomatic_Explorer`.
2. Upload the **contents of this folder** into the repository, keeping `docs/` intact.
3. In the repository, open Settings → Pages.
4. Under Build and deployment, select **Deploy from a branch**, then your default branch (usually `main`) and **/docs**. Save.
5. GitHub will display the Pages URL after deployment. Open it to use the map. `gallery.html` opens the photo catalogue.

If using Git locally, start in this extracted folder:

```sh
git init
git add .
git commit -m "Add Sonomatic product and service explorer"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Sonomatic_Explorer.git
git push -u origin main
```

Replace `YOUR_USERNAME` and the repository name with your own. No Git history, credentials or hosting account IDs are included in this ZIP.

## Controls

- Click a category/page to expand its branches in the original left/right hierarchy. Each vertical group bows outward: the middle blocks sit farther out than the top and bottom blocks. Zoom and pan stay in place.
- The explorer opens with a dark background and softly coloured category blocks. Use the theme button to switch to light mode.
- Every category and intermediate branch has a representative photo/illustration. Product photos remain on the item blocks. Integrity/software branches label their inspection-context imagery.
- Click a product or service for its activity, installation section, photo and official source.
- Use the info button to inspect a category without expanding it.
- Drag the background to pan; drag a card to move its subtree; scroll to zoom.
- Search across names, work and installation areas. `/` focuses search; Escape closes details.
- Use List view for the catalogue, or Photos for the visual index.
- Expand all and Collapse preserve your view. Use Fit to view only when you want to recenter and resize the diagram. The category legend and breadcrumbs intentionally navigate to a new branch.

## Editable files

- `docs/index.html`: map page structure
- `docs/style.css`: visual styling
- `docs/app.js`: interaction logic
- `docs/data.json`: readable catalogue
- `docs/data.js`: the same data assigned to `window.SONOMATIC_DATA`, so local file opening works without fetch
- `docs/assets/`: local images
- `docs/gallery.html`: photo catalogue
- `docs/photo-sources.csv` and `.json`: image provenance, brochure page and shared-image labels
- `scripts/rebuild.py`: synchronize data.js, standalone HTML and gallery from edited data.json and website files (Python 3 standard library only)

After editing the catalogue or images, run `python3 scripts/rebuild.py` from this folder. Refresh the browser after editing.

## Content scope and attribution

133 hierarchy entries include categories, pages, products, services, software and techniques; this is not a count of unique robots. The first level follows Sonomatic's main website categories. Product-family groupings are editorial navigation.

Research and navigation were reviewed on 28–29 October 2026. Photo package prepared on 30 October 2026. Historical products, custom systems and conflicting document specifications retain their labels and caveats. A published brochure does not establish current stock or commercial availability.

Photos, equipment renders and brochure excerpts are from Sonomatic's official website and publications. Each included image has a source link; these third-party materials remain the property of their respective rights holders. No blanket open-source licence is granted over manufacturer content. Shared fleet/family images are labelled and are not presented as verified individual-model photographs.

This is an independent reference tool, not an official Sonomatic website.
