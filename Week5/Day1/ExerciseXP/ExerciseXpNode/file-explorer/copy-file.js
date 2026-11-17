const fs = require("fs");
const path = require("path");

const sourcePath = path.join(__dirname, "source.txt");
const destinationPath = path.join(__dirname, "destination.txt");

async function copyFileContent() {
    try {
        const content = await fs.promises.readFile(sourcePath, "utf8");
        await fs.promises.writeFile(destinationPath, content, "utf8");
        console.log("Copied source.txt to destination.txt");
    } catch (error) {
        console.error("Could not copy the file:", error.message);
        process.exitCode = 1;
    }
}

copyFileContent();
