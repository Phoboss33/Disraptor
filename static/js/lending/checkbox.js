var selectedObjects = [];

document.getElementById('respondentForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Получаем скрытое поле
    var selectedObjectsField = document.getElementById('selectedObjectsField');

    // Устанавливаем его значение в selectedObjects
    selectedObjectsField.value = JSON.stringify(selectedObjects);

    // Отправляем форму
    this.submit();
});

document.querySelectorAll('input[type="checkbox"]').forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {

        document.querySelectorAll('input[type="checkbox"]').forEach(function(checkbox) {
            if (checkbox.checked) {
                selectedObjects.push(checkbox.id);
            }
        });

        console.log(selectedObjects);
    });
});