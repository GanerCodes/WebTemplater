example = () => createElement("div", null, "hi");
document.body.appendChild(createElement('fragment', null, example(), createElement("p", null, "Example")));