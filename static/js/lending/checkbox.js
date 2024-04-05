let selectedObjects = [];
let price_sum = 0
let max_price = 750000 //поменяй меня , если я не правильный

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
        price_sum = 0;

        // Перебираем только отмеченные чекбоксы и суммируем цены
        document.querySelectorAll('div.form-check').forEach(function(div) {
            let checkbox = div.querySelector('input[type="checkbox"]');
            let priceInput = div.querySelector('input.price');

            if (checkbox.checked) {
                let price = parseFloat(priceInput.value);
                if (!isNaN(price)) {
                    price_sum += price;
                    console.log(priceInput.value);
                }
            }
            //если достигли лимита - блочим чекбоксы
            if (price_sum == max_price) {
                //alert("переполнен");
                document.querySelectorAll('div.form-check').forEach(function(div) {
                    let checkbox = div.querySelector('input[type="checkbox"]');
                    let priceInput = div.querySelector('input.price');
                    let price = parseFloat(priceInput.value);
                    if (!checkbox.checked && price!=0)
                        checkbox.disabled = true;
                });
            } else { //если меньше лимита - разблочим чекбоксы | если новый объект переполнит лимит - блочим
                document.querySelectorAll('div.form-check').forEach(function(div) {
                    let checkbox = div.querySelector('input[type="checkbox"]');
                    let priceInput = div.querySelector('input.price');
                    let price = parseFloat(priceInput.value);
                    if (!checkbox.checked)
                        checkbox.disabled = false;
                    if (!checkbox.checked && price+price_sum > max_price)
                        checkbox.disabled = true;
                });
            }
        });

        console.log(selectedObjects);
        console.log(price_sum);
        document.getElementById('summa_input').innerText = price_sum;
    });
});

