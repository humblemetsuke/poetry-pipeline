# release.ps1
# Fully automated version bump + changelog + commit + tag + push

Write-Host "Running pre-commit hooks..."
poetry run pre-commit run --all-files

Write-Host "Bumping version according to conventional commits..."
poetry run cz bump --yes

Write-Host "Pushing commits and tags to origin..."
git push origin main --follow-tags

Write-Host "Release complete!"
