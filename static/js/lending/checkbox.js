let selectedObjects = [];
let price_sum = 0
let max_price = 75000000

document.getElementById('respondentForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let selectedObjectsField = document.getElementById('selectedObjectsField');

    selectedObjectsField.value = JSON.stringify(selectedObjects);

    this.submit();
    selectedObjects = [];
    price_sum = 0
});

document.querySelectorAll('input[type="checkbox"]').forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        if (this.checked) {
            selectedObjects.push(this.id);
        } else {
            let index = selectedObjects.indexOf(this.id);
            if (index !== -1) {
                selectedObjects.splice(index, 1);
            }
        }

        //$(".form-check-input").click(function() {if (!this.checked) return false;})

        // Объявляем переменную для суммирования цен
        let sum_price = 0;

        // Перебираем только отмеченные чекбоксы и суммируем цены
        document.querySelectorAll('div.form-check').forEach(function(div) {
            let checkbox = div.querySelector('input[type="checkbox"]');
            let priceInput = div.querySelector('input.price');

            if (checkbox.checked) {
                let price = parseFloat(priceInput.value);
                if (!isNaN(price)) {
                    sum_price += price;
                    console.log(priceInput.value);
                }
            }

            if (sum_price > max_price) {
                //alert("переполнен");
                document.querySelectorAll('div.form-check').forEach(function(div) {
                    let checkbox = div.querySelector('input[type="checkbox"]');
                    let priceInput = div.querySelector('input.price');
                    let price = parseFloat(priceInput.value);
                    if (!checkbox.checked && price!=0)
                        checkbox.disabled = true;
                });
            } else {
                document.querySelectorAll('div.form-check').forEach(function(div) {
                    let checkbox = div.querySelector('input[type="checkbox"]');
                    if (!checkbox.checked)
                        checkbox.disabled = false;
                });
            }
        });

        console.log(selectedObjects);
        console.log(sum_price);
    });
});

