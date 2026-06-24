# How to push this repo to GitHub

This folder is already a git repository with one commit. You only need to create an empty
GitHub repo and push to it.

## Step 1 — Create an empty repo on GitHub
1. Go to https://github.com/new
2. Repository name: `UniVision-SOC` (or anything you like)
3. **Do NOT** tick "Add a README", ".gitignore", or "license" — keep it empty.
4. Click **Create repository**. Copy the URL it shows, e.g.
   `https://github.com/<your-username>/UniVision-SOC.git`

## Step 2 — Connect and push
Open a terminal **inside this folder** (`Desktop\UniVision-SOC`) and run:

```bash
git remote add origin https://github.com/<your-username>/UniVision-SOC.git
git push -u origin main
```

When prompted for credentials, log in through the browser window, **or** use a
Personal Access Token as the password (GitHub no longer accepts your account password):
- Create one at https://github.com/settings/tokens → "Generate new token (classic)" → tick `repo`.

That's it — refresh the GitHub page and all your files will be there.

## Making further changes later
```bash
git add .
git commit -m "describe what changed"
git push
```

## (Optional) If you install GitHub CLI
With `gh` installed and `gh auth login` done, Steps 1–2 become one command:
```bash
gh repo create UniVision-SOC --public --source=. --remote=origin --push
```
