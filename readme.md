# Decky Script Runner - Scripts Repository

This repository hosts scripts designed for use with the **Decky Plugin Loader**'s **Script Runner Plugin**. Contributions are welcome and encouraged! Below you'll find information on how to structure your scripts and submit them for inclusion in the repository.

---

## Repository Structure

Each script must be placed inside the `scripts/` directory and organized into folders named after the author. For example:  

```
scripts/{author-name}/{script-name}.py
```

**Example:**
```
scripts/Gr3gorywolf/install-node-packages.py
```

---

## Script Metadata

Every script should include the following metadata comment block at the very top of the file. This metadata is automatically generated when creating or editing a new script using the Decky Script Runner plugin or its sideloader.  

```python
# ----------metadata---------
# title: Install Common Nodejs Packages
# description: [Requires node] Install common nodejs packages such as expressjs, node-fetch, joi, socket.io, lodash, cheerio, and axios.
# image:
# author: Gr3gorywolf
# version: 1.0.0
# root: false
# ----------metadata---------
```

### Metadata Fields
- **title**: A short, descriptive name for the script.
- **description**: A detailed explanation of what the script does and any requirements.
- **image**: A URL to an image/icon representing the script (optional).
- **author**: The name of the script's author.
- **version**: The version of the script in `x.y.z` format (increment when making updates).
- **root**: Boolean (`true` or `false`), indicating whether the script requires root permissions.

---

## Contribution Guidelines

### Submitting a New Script

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/{your-username}/decky-script-runner-scripts.git
   cd decky-script-runner-scripts
   ```

2. **Create Your Script:**  
   Add your script to the appropriate folder structure inside the `scripts/` directory.  

3. **Add Metadata:**  
   Ensure your script has the correct metadata block at the top of the file.

4. **Push Changes:**  
   Create a pull request targeting the `main` branch of the repository.  

   Once your pull request is merged, the script will automatically appear in the store for users of the Decky Script Runner.

---

### Updating an Existing Script

1. **Locate Your Script:**  
   Find your script inside the `scripts/{author-name}/` folder.

2. **Make Improvements:**  
   Apply any necessary updates or fixes.

3. **Increment Version:**  
   Update the `version` field in the metadata block to indicate the new version. This is crucial for the plugin to recognize updates.

4. **Submit a Pull Request:**  
   Push your updated script by creating a pull request targeting the `main` branch.

---

## License

By contributing to this repository, you agree to release your work under the repository's license.

---

Feel free to contribute and share your scripts with the Decky Script Runner community!