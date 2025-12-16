# Deployment Configuration

This document explains how to properly configure and deploy your Docusaurus site to avoid common deployment issues.

## Understanding Base URL

The `baseUrl` in `docusaurus.config.ts` is the most critical configuration for deployment. It determines the base URL for all site assets and pages.

### When to use different baseUrl values:

- `baseUrl: "/"` - When deployed to root domain (e.g., `https://myproject.vercel.app/`)
- `baseUrl: "/reponame/"` - When deployed to subdirectory (e.g., `https://username.github.io/reponame/`)

## Common Vercel Deployment Issues

### Issue: "Your Docusaurus site did not load properly"
**Cause**: Usually incorrect `baseUrl` configuration
**Solution**:
1. Check your actual deployment URL
2. Ensure `baseUrl` matches the path structure
3. For `https://project-name.vercel.app/`, use `baseUrl: "/"`

### Issue: CSS and assets not loading
**Cause**: Assets are requested from wrong path due to incorrect `baseUrl`
**Solution**: Verify that the path in your browser matches your `baseUrl` setting

## Recommended Vercel Configuration

Update your `vercel.json` with:

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "build",
  "framework": "docusaurus"
}
```

## Pre-deployment Checklist

Before deploying, verify:

- [ ] `npm run build` completes without errors
- [ ] `npm run serve` shows a properly styled site locally
- [ ] `baseUrl` in `docusaurus.config.ts` matches expected deployment path
- [ ] All internal links work correctly

## Troubleshooting Steps

1. **Check browser console** for 404 errors on assets
2. **Verify the deployment URL** in your Vercel dashboard
3. **Test the build locally** with `npm run build && npm run serve`
4. **Compare asset paths** in browser dev tools Network tab
5. **Clear browser cache** and hard refresh (Ctrl+Shift+R)

## Quick Fix for Common Issues

If your site works locally but not on Vercel:

1. Change `baseUrl` to `"./"` (relative path) temporarily
2. If that works, revert to `"/"` and check Vercel project settings
3. Ensure no custom base path is set in Vercel project configuration

## Environment-specific Configuration

For more complex deployments, you can use environment-aware configuration:

```javascript
// In docusaurus.config.js
const isProd = process.env.NODE_ENV === 'production';
const isVercel = !!process.env.VERCEL;

const config = {
  url: isProd ? 'https://your-vercel-url.vercel.app' : 'http://localhost:3000',
  baseUrl: isVercel ? '/' : '/',
  // ...
};
```

## Testing Your Deployment

After making configuration changes:

1. Commit and push to trigger a new Vercel deployment
2. Wait for the build to complete
3. Visit the deployment URL
4. Test multiple pages to ensure navigation works
5. Check browser console for any errors
6. Verify all assets (CSS, images, JS) load correctly

## Additional Resources

- [Docusaurus Deployment Guide](https://docusaurus.io/docs/deployment)
- [Vercel Documentation for Docusaurus](https://vercel.com/docs/frameworks/docusaurus)
- Check the [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) file for more detailed information