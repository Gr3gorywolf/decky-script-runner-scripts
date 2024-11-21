# Decky Script Runner community scrips

> ⚠️ **Warning**  
> 1. Some scripts require root and unlock the Steam Deck filesystem. In those cases, we are not responsible for Steam Deck damages. (Verify the code before running them)  
> 2. Neither the Plugin or Developer are responsible for anything done by the script runner since the plugin was made just for running scripts. Any script that you run will be at your own risk. 

The community scripts are scripts made by the community to facilitate certain automatizations. These scripts can be downloaded from the GitHub repo and installed by the sideloader.

These scripts provide various functionalities and enhancements for your Steam Deck, allowing you to customize and optimize your gaming experience. However, it's crucial to exercise caution and understand the implications of running third-party scripts on your device.

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

```
----------metadata---------
title: Install Common Nodejs Packages
description: [Requires node] Install common nodejs packages such as expressjs, node-fetch, joi, socket.io, lodash, cheerio, and axios.
image:
author: Gr3gorywolf
version: 1.0.0
root: false
----------metadata---------
```

### Metadata Fields

- **title**: A short, descriptive name for the script.
- **description**: A detailed explanation of what the script does and any requirements.
- **image**: A URL to an image/icon representing the script (optional).
- **author**: The name of the script's author.
- **version**: The version of the script in `x.y.z` format (increment when making updates).
- **root**: Boolean (`true` or `false`), indicating whether the script requires root permissions.

#### **Note:** Every field value should be on 1 line, if exeed it can misformat the metadata

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
