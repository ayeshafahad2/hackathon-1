# Deployment Guide for Docusaurus on Vercel

This guide provides best practices and troubleshooting for deploying your Docusaurus site to Vercel.

## Configuration Settings

### Docusaurus Configuration (`docusaurus.config.ts`)

The key configuration for Vercel deployment is the `baseUrl` setting:

```typescript
const config = {
  url: "https://your-project-name.vercel.app",  // Your Vercel project URL
  baseUrl: "/",  // Use "/" for root deployment, "/repo-name/" for subdirectory
  // ...
};
```

### Vercel Configuration (`vercel.json`)

Use the modern Vercel framework configuration:

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "build",
  "framework": "docusaurus"
}
```

## Common Deployment Issues and Solutions

### 1. CSS Not Loading / Assets Not Found

**Symptoms**:
- Site appears unstyled
- Console shows 404 errors for CSS/JS files
- "Your Docusaurus site did not load properly" error

**Solutions**:
1. Check your `baseUrl` setting in `docusaurus.config.ts`
   - Use `/` for root deployment (e.g., `https://myproject.vercel.app/`)
   - Use `/reponame/` if deployed to subdirectory (e.g., `https://username.github.io/reponame/`)

2. Verify your Vercel project settings:
   - Go to Vercel Dashboard → Project Settings
   - Ensure the "Build & Development Settings" are not overriding paths

### 2. Base URL Configuration Issues

The error "Current configured baseUrl = / (default value), We suggest trying baseUrl = /" means the baseUrl is already correct but the deployment path doesn't match.

**To determine the correct baseUrl**:
- If deployed to `https://my-project.vercel.app/` → use `baseUrl: "/"`
- If deployed to `https://my-project.vercel.app/specbook/` → use `baseUrl: "/specbook/"`

### 3. GitHub Repository vs Vercel Project Name

If your GitHub repo name is `specbook` but Vercel creates a project with a different name, the deployment path might be affected. Always check your actual deployment URL.

## Environment-Specific Configuration

For different environments, you can use conditional configuration:

```typescript
const isDeployed = process.env.NODE_ENV === 'production';
const baseUrl = process.env.VERCEL_URL ? `/${process.env.VERCEL_GIT_REPO_SLUG || ''}/` : '/';

const config = {
  url: isDeployed ? `https://${process.env.VERCEL_URL}` : 'http://localhost:3000',
  baseUrl: baseUrl,
  // ...
};
```

## Deployment Process

### 1. Pre-deployment Checklist

- [ ] Run `npm run build` locally and test with `npm run serve`
- [ ] Verify all links work correctly
- [ ] Check that assets (images, CSS, JS) load properly
- [ ] Confirm `baseUrl` matches your expected deployment path

### 2. Vercel Deployment Steps

1. Push your code to GitHub
2. Vercel will automatically detect and deploy your Docusaurus site
3. Check the deployment logs for any errors
4. Visit your deployment URL to verify everything works

### 3. Post-deployment Verification

- [ ] All pages load without errors
- [ ] CSS and styling appear correctly
- [ ] Navigation works properly
- [ ] Images and assets load
- [ ] Search functionality works (if enabled)

## Troubleshooting Steps

### If Site Still Doesn't Load Properly

1. **Check Browser Console**: Look for 404 errors on asset requests
2. **Verify Base URL**: Ensure it matches your actual deployment path
3. **Clear Cache**: Try hard refresh (Ctrl+F5 or Cmd+Shift+R)
4. **Test Locally**: Run `npm run build && npm run serve` to test locally

### Common Error Messages

**"Your Docusaurus site did not load properly"**:
- Usually caused by incorrect `baseUrl` configuration
- Check that assets are loading from the correct path

**CSS/JS files returning 404**:
- Indicates `baseUrl` doesn't match the deployment path
- Adjust `baseUrl` in `docusaurus.config.ts`

## Advanced Configuration

### For Custom Domain Deployments

When using a custom domain, keep `baseUrl: "/"` and ensure your domain points to the root path.

### For Subdirectory Deployments

If you need to deploy to a subdirectory, update both configurations:

1. In `docusaurus.config.ts`: `baseUrl: "/your-subdirectory/"`
2. In Vercel project settings: Set "Base Path" if using the Vercel for GitHub app

## Development vs Production Differences

Remember that during local development (`npm run start`), the site runs on `http://localhost:3000` with `baseUrl: "/"`, but in production, the actual path might differ based on Vercel's deployment.

## Quick Fix Checklist

If experiencing deployment issues:

1. ✅ Ensure `baseUrl: "/"` in `docusaurus.config.ts` for root deployment
2. ✅ Verify `vercel.json` uses the modern configuration format
3. ✅ Run local build test: `npm run build && npm run serve`
4. ✅ Check browser console for 404 errors
5. ✅ Confirm Vercel deployment URL matches expectations
6. ✅ Clear browser cache and hard refresh

## Environment Variables for Dynamic Configuration

You can also use environment variables for dynamic configuration:

```typescript
const GITHUB_REPO_NAME = "specbook"; // Replace with your repo name

const config = {
  url: process.env.DEPLOYMENT_URL || "http://localhost:3000",
  baseUrl: process.env.BASE_URL || "/",
  // For GitHub Pages: baseUrl: process.env.NODE_ENV === 'production' ? `/${GITHUB_REPO_NAME}/` : '/',
  // ...
};
```

Add these to your Vercel project environment variables if needed.