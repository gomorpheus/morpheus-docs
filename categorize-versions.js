<script>
// get containers/versions
let container = document.getElementsByClassName("rst-other-versions")[0];
let versions = document.getElementsByClassName("rst-other-versions")[0].querySelectorAll('dd');
let headers = document.getElementsByClassName("rst-other-versions")[0].querySelectorAll('dl');

// create new containers, and add child elements
let lts = document.createElement('div');
lts.id = "m-lts";
lts.innerHTML = "<dl id='lts-versions'><dt>LTS Versions</dt></dl>"

let std = document.createElement('div');
std.id = "m-std";
std.innerHTML = "<dl id='std-versions'><dt>Standard Versions</dt></dl>"

// add them
container.insertBefore(std, container.firstChild);
container.insertBefore(lts, container.firstChild);

// capture for adding dd elements
let stdVersions = document.getElementById("std-versions");
let ltsVersions = document.getElementById("lts-versions");

// iterate versions
versions.forEach((item, index) => {
    let version = item.innerText;
    let splt = version.split(".");
    if(splt.length > 1) {
        let minor = version[2];
        let item2 = item;
        if ((minor === 0) || (minor % 2 === 0)){
            // lts
            ltsVersions.appendChild(item2);
        } else {
            // standard
            stdVersions.appendChild(item2);
        }
    }
});

// remove the existing element which we don't need?
headers[0].remove();

</script>
