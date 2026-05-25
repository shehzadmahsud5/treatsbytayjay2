# Treats By Tayjah - Local SEO & Discovery Strategy

## 📍 Local SEO Focus (Manchester M14)
Since Treats By Tayjah is a home-based business, capturing high-intent local traffic is crucial. We don't need national traffic; we need people in Manchester looking for "custom cakes near me."

### 1. Google Business Profile (GBP) Optimization
Because the business operates from a private address, it must be set up as a **Service-Area Business (SAB)** on Google.
- **Action Required**: Create or claim the Google Business Profile for "Treats By Tayjah".
- **Address Setting**: Hide the physical street address (since it's a home), but set the service area to "Manchester", "M14", "Fallowfield", "Withington", and surrounding postcodes.
- **Categories**: Primary category: "Bakery". Secondary: "Cake Shop", "Wedding Bakery".
- **Trust Signal**: Add a photo of the "5/5 Food Hygiene Rating" certificate directly to the GBP photos.

### 2. On-Page SEO (Completed & Planned)
- **Title Tag**: `<title>Treats By Tayjah | Custom Cakes in Manchester (M14)</title>` (Implemented)
- **Meta Description**: Configured to include target keywords: "Bespoke, custom cakes, cupcakes, and cookies based in Manchester (M14)." (Implemented)
- **H1 Strategy**: The H1 contains the primary local intent keyword: "Bespoke Bakes for Every Occasion in Manchester". (Implemented)

### 3. Schema Markup (To be Implemented)
To help Google perfectly understand the business, we need to inject `LocalBusiness` or `FoodEstablishment` JSON-LD schema into the `<head>` of the `index.html` file. 

**Proposed Schema Injection:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FoodEstablishment",
  "name": "Treats By Tayjah",
  "image": "https://www.instagram.com/treatsbytayjah",
  "description": "Bespoke home-based bakery specializing in custom cakes, cupcakes, and cookies.",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Manchester",
    "postalCode": "M14",
    "addressCountry": "UK"
  },
  "servesCuisine": "Bakery",
  "priceRange": "$$",
  "sameAs": [
    "https://www.instagram.com/treatsbytayjah",
    "https://www.tiktok.com/@treatsbytayjah",
    "https://www.facebook.com/people/Treats-By-Tayjah/61559094343694/"
  ]
}
</script>
```

## 🔍 Double Check Process
- **Verification 1**: Checked the HTML source code to ensure H1 and Title tags aren't cannibalizing each other and that they perfectly target "Manchester M14" search intent. 
- **Verification 2**: Ensured that the Schema markup proposed strictly hides the street address to protect the privacy of the home-based business, only outputting Locality and Postal Code.

---
**SEO Specialist**: Antigravity
**Date**: 2026-05-25
**Status**: Ready for implementation.
