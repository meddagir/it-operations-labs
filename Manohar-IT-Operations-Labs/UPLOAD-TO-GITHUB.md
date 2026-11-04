# Upload to GitHub

## MacBook or Windows browser
1. Extract the ZIP first. Upload the files inside it, not the ZIP itself.
2. Sign in to https://github.com and create a new repository named `it-operations-labs`.
3. Add the description: `Reproducible endpoint readiness, connectivity troubleshooting, and backup recovery labs.`
4. Choose Public if you want recruiters to view it. Initialize with a README so the repository page is easy to open.
5. Open the repository, choose **Add file > Upload files**.
6. Drag the contents of Manohar-IT-Operations-Labs into the upload area, preserving the project folders. The supplied README replaces the initial README.
7. Enter a truthful commit message such as `Add reproducible IT operations lab projects`, and commit.
8. Confirm README.md is at the repository root, all three project folders open, and the screenshots render inside the README.
9. Add topics: `it-support`, `system-administration`, `python`, `powershell`, `troubleshooting`, `backup-recovery`.
10. Add the repository to your profile's pinned projects. After doing your repeat runs, commit your own notes and screenshots.

## If you only have an iPhone
Download the ZIP to Files and tap it to extract. You can read the Markdown files as text and view PNG evidence. Mobile browser folder upload may not preserve the structure reliably. Use a MacBook for the complete upload when available.

If you need to start on the phone now, create the repository in Safari, use **Add file > Create new file**, enter `README.md`, and paste the root README text. This is only a start; its screenshot links will work after you upload the project folders. Avoid uploading only the ZIP as your main portfolio because recruiters cannot browse its code directly.

## Git alternative (computer with Git installed)
Create an empty repository without an initial README, then run from the extracted folder:
```bash
git init
git add .
git commit -m "Add IT operations lab projects"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/it-operations-labs.git
git push -u origin main
```
Replace YOUR-USERNAME. Authenticate using GitHub's supported sign-in flow; never paste a token into project files.

Official instructions: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
