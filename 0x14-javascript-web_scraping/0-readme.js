const fs = require("fs");

const args = process.argv;

if (args.length !== 3) {
    console.log(`Usage: ${args[0]} ${args[1]} <file_path>`);
    process.exit(1);
}

const filePath = args[2];

try {
    const data = fs.readFileSync(filePath, "utf-8");
    console.log(data);
} catch (err) {
    console.error(err);
}
