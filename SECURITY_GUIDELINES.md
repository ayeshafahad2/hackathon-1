# Security Guidelines

## Handling Sensitive Information

### 1. API Keys and Secrets Management
- **Never commit API keys, passwords, or other sensitive information** to the repository
- Use environment variables to store sensitive data
- Create template files with placeholder values instead of real secrets

### 2. Environment Files
- Store sensitive data in `.env` files that are ignored by Git
- Create `.env.example` files with dummy values for other developers to reference:

```bash
# Example .env.example file
OPENAI_API_KEY=your_openai_api_key_here
QDRANT_URL=your_qdrant_url_here
QDRANT_API_KEY=your_qdrant_api_key_here
NEONDB_API_KEY=your_neondb_api_key_here
POSTGRES_URL=your_postgres_url_here
```

### 3. Git Ignore Configuration
Make sure your `.gitignore` file includes:
```
# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Secrets directory
secrets/
config.json
*.key
```

## Pre-commit Checklist
Before committing code, make sure:
- [ ] No API keys or secrets are present in the code
- [ ] Environment files with real values are not committed
- [ ] Sensitive configuration is handled via environment variables
- [ ] .gitignore properly excludes sensitive files

## Developer Guidelines
1. If you accidentally commit a secret:
   - Rotate the secret immediately (get a new one from the service provider)
   - Use `git filter-repo` or similar tools to remove the secret from Git history
   - Regenerate the .gitignore if necessary

2. For local development:
   - Copy `.env.example` to `.env` and fill with your own values
   - Never commit the `.env` file

3. For production deployment:
   - Set environment variables through your hosting platform's interface
   - Never hard-code values in source files

## Recovery Steps if Secrets Are Exposed
If you commit and push secrets to a repository:

1. **Immediate Action:**
   - Change/revoke the exposed credentials immediately
   - Contact the service provider if necessary

2. **Repository Cleanup:**
   - Use `git filter-repo` to completely remove the sensitive data from history:
     ```bash
     git filter-repo --path path/to/file --replace-text <(echo "sensitive_data::REMOVED")
     ```
   
   - Force push the corrected history:
     ```bash
     git push --force-with-lease origin main
     ```

3. **Verification:**
   - Check that the sensitive data is no longer accessible in any commit
   - Update all affected credentials

## Tools and Resources
- Use a credential scanner like `truffleHog`, `git-secrets`, or GitHub's own secret scanning
- Consider using a secrets management service for production environments
- Regularly audit your repository history for accidental secret exposure