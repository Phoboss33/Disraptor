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
            //selectedElement.style.left = (e.screenX > field.right ? field.right - SizeSquare : e.screenX < diffX ? diffX - SizeSquare : e.screenX - diffX) + "px";
            selectedElement.style.left = (e.clientX - diffX + document.documentElement.scrollLeft) + "px";
            //selectedElement.style.top = (e.screenY > field.bottom ? field.bottom - SizeSquare : e.screenY < diffY ? diffY - SizeSquare : e.screenY - diffY) + "px";
            selectedElement.style.top = (e.clientY - diffY + document.documentElement.scrollTop) + "px";
            console.log(document.documentElement.scrollTop);
            if (e.clientY - diffY >= field.top && e.clientX - diffX >= field.left &&
            selectedElement.getBoundingClientRect().bottom <= field.bottom &&
            selectedElement.getBoundingClientRect().right <= field.right) {
                text.value = `${e.clientX - diffX - rateX}, ${e.clientY - diffY - rateY}`;
            } else {
                text.value = "Undefined";
            }
        }

    }
});
