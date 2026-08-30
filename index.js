import jsonfile from "jsonfile";
import moment from "moment";
import simpleGit from "simple-git";

const git = simpleGit();

const path = "./data.json";
const date = moment().subtract(8, "days").toISOString();

const data = {
    date,
};

async function makeCommit() {
    await jsonfile.writeFile(path, data, () => {
       git.add([path]);

         git.commit(date, {
            "--date": date,
        });

         git.push();
    });



    console.log("Commit pushed successfully");
}

makeCommit().catch(console.error);