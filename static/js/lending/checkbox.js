document.getElementById('respondentForm').addEventListener('submit', function(event) {
    event.preventDefault();

    this.submit();
});

document.querySelectorAll('input[type="checkbox"]').forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        var selectedObjects = [];

        document.querySelectorAll('input[type="checkbox"]').forEach(function(checkbox) {
            if (checkbox.checked) {
                selectedObjects.push(checkbox.id);
            }
        });

        console.log(selectedObjects);
    });
});