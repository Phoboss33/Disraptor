document.addEventListener("DOMContentLoaded", function () {
    let draggableElements = document.querySelectorAll(".square");
    let field = document.getElementById("field").getBoundingClientRect();

    draggableElements.forEach(function (elem) {
        elem.addEventListener("mousedown", SelectItem, false);
        //window.addEventListener("mouseup", mouseUp, false);
    });
    let selectedElement = null;
    let diffX = 0;
    let diffY = 0;
    let i = 1;
    const rateX = 8;
    const rateY = 229;
    const SizeSquare = 150;

    function SelectItem(e) {
        if (!selectedElement) {
            console.log("Select");
            selectedElement = e.target;
            selectedElement.style.zIndex = i++;
            diffX = e.clientX - selectedElement.getBoundingClientRect().left;
            diffY = e.clientY - selectedElement.getBoundingClientRect().top;
            window.addEventListener("mousemove", mouseMove, false);
        } else {
            console.log("Diselect");
            window.removeEventListener("mousemove", mouseMove, false);
            selectedElement = null;
        }
    }

    function mouseMove(e) {
        console.log("move");
        if (selectedElement) {
            selectedElement.style.position = "absolute";
            //console.log(e.clientX);
            //console.log(field.right);
            //console.log(diffX);
            //console.log(e.clientY);
            //console.log(field.bottom);
            //console.log(diffY);
            let text = document.getElementById("text"+ selectedElement.id.match(/\d+/)[0]);
            //console.log(text.id);
            //console.log(selectedElement.id.match(/\d+/)[0]);
            //selectedElement.style.left = (e.clientX > field.right ? field.right - SizeSquare : e.clientX < diffX ? diffX - SizeSquare : e.clientX - diffX) + "px";
            selectedElement.style.left = (e.clientX - diffX + window.scrollX) + "px";
            selectedElement.style.top = (e.clientY - window.scrollY > field.bottom ? field.bottom - SizeSquare : e.clientY - window.scrollY < diffY ? diffY - SizeSquare : e.clientY - diffY  + window.scrollY) + "px";
            //selectedElement.style.top = (e.clientY - diffY + window.scrollY) + "px";
            //console.log(window. pageYOffset);
            //console.log(window. scrollY);
            console.log(e.clientY - window.scrollY);
            console.log(field.bottom);
            if (e.clientY - diffY + window.scrollY >= field.top && e.clientX - diffX + window.scrollX >= field.left &&
            selectedElement.getBoundingClientRect().bottom - window.scrollY <= field.bottom &&
            selectedElement.getBoundingClientRect().right - window.scrollX <= field.right) {
                text.value = `${e.clientX - diffX - rateX}, ${e.clientY - diffY - rateY}`;
            } else {
                text.value = "Undefined";
            }
        }

    }
});
