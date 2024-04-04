document.getElementById('respondentForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию

    this.submit();
});

document.querySelectorAll('input[type="checkbox"]').forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        var selectedObjects = []; // Список выбранных объектов

        // Перебираем все чекбоксы
        document.querySelectorAll('input[type="checkbox"]').forEach(function(checkbox) {
            if (checkbox.checked) {
                // Если чекбокс выбран, добавляем его ID в список выбранных объектов
                selectedObjects.push(checkbox.id);
            }
        });

        // Выводим список выбранных объектов в консоль
        console.log(selectedObjects);
    });
});