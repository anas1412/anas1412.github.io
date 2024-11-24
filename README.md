To push a new article to the Hugo site, follow these steps:

1. Create a new markdown file in the content/post directory with the format `YYYYMMDD.md`.
2. Add the following front matter to the top of the file:

   ```markdown
   +++
   author = "The name of the author of the article."
   title ="The title of the article."
   date = "YYYY-MM-DD"
   description = "A brief description of the article."
   tags = [ "A list of tags to categorize the article.", ]
   thumbnail = "posts/thumbnail.jpg"
   +++

   Here you write the content of the article in the markdown file.
   ```

3. Build the site by running the following command:

   ```bash
   hugo
   ```

   This will generate the static files in the public directory.

4. Commit and push the changes with this command:

   ```bash
   git add .; git commit -m "Added article"; git subtree push --prefix public origin gh-pages; git push origin main
   ```

   or for linux:

   ```bash
   git add . && git commit -m "Added article" && git subtree push --prefix public origin gh-pages && git push origin main
   ```
