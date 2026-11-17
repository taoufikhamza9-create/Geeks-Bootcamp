const fs = require("fs");

fs.readdir(__dirname, (error, files) => {
    if (error) {
        console.error("Could not read the directory:", error.message);
        process.exitCode = 1;
        return;
    }

    console.log("Files in file-explorer:");
    files.forEach(file => console.log(file));
});
