To push a new article to the Hugo site, follow these steps:

1. Create a new markdown file in the content/post directory with the format `YYYYMMDD.md`.
2. Add the following front matter to the top of the file:
   ```markdown
       +++`

   - author = "The name of the author of the article."
   - title ="The title of the article."
   - date = "YYYY-MM-DD"
   - description = "A brief description of the article."
   - tags = [ "A list of tags to categorize the article.", ]
   - `thumbnail`: The URL of the thumbnail image for the article.
     +++`
   ```
3. Write the content of the article in the markdown file.
4. Commit and push the changes with this command: `git add .; git commit -m "Added article"; git subtree push --prefix public origin gh-pages; git push origin main`
