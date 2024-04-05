document.addEventListener("DOMContentLoaded", function () {
    let draggableElements = document.querySelectorAll(".square");
    let field = document.getElementById("field").getBoundingClientRect();

    draggableElements.forEach(function (elem) {
        elem.addEventListener("mousedown", SelectItem, false);
    });
    let selectedElement = null;
    let diffX = 0;
    let diffY = 0;
    let i = 1;

    function SelectItem(e) {
        if (!selectedElement) {
            console.log("Select");
            selectedElement = e.target;
            selectedElement.style.zIndex = String(i++);
            diffX = e.clientX - selectedElement.getBoundingClientRect().left;
            diffY = e.clientY - selectedElement.getBoundingClientRect().top;
            window.addEventListener("mousemove", mouseMove, false);
        } else {
            console.log("Cancel");
            window.removeEventListener("mousemove", mouseMove, false);
            selectedElement = null;
        }
    }

    function mouseMove(e) {
        console.log("move");
        if (selectedElement) {
            selectedElement.style.position = "absolute";
            let text = document.getElementById("text"+ selectedElement.id.match(/\d+/)[0]);
            selectedElement.style.left = (e.clientX - diffX + window.scrollX) + "px";
            selectedElement.style.top = (e.clientY - diffY + window.scrollY) + "px";
            if (e.clientY - diffY + window.scrollY >= field.top && e.clientX - diffX + window.scrollX >= field.left &&
                selectedElement.getBoundingClientRect().bottom + window.scrollY <= field.bottom &&
                selectedElement.getBoundingClientRect().right - window.scrollX <= field.right) {
                let resX = selectedElement.getBoundingClientRect().left - field.left;
                let resY = selectedElement.offsetTop - field.top;
                text.value = `${Math.floor(resX)}, ${Math.abs(Math.floor(resY))}`;
            } else {
                console.log("Cancel");
                window.removeEventListener("mousemove", mouseMove, false);
                if (selectedElement.getBoundingClientRect().top < field.top) {
                    selectedElement.style.top = field.top + "px";
                }
                if (selectedElement.offsetTop + 150 > field.bottom) {
                    selectedElement.style.top = field.bottom - 150 + "px";
                }
                if (selectedElement.getBoundingClientRect().right > field.right) {
                    selectedElement.style.left = field.right - 150 + "px";
                }
                if (selectedElement.getBoundingClientRect().left < field.left) {
                    selectedElement.style.left = field.left + "px";
                }
                let resX = selectedElement.getBoundingClientRect().left - field.left;
                let resY = selectedElement.offsetTop - field.top;
                text.value = `${Math.floor(resX)}, ${Math.abs(Math.floor(resY))}`;
                selectedElement = null;
            }
        }

    }
});
