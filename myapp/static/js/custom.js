
function priceTotal() {
    var price = document.getElementById('price').value;
    var quantity = document.getElementById('quantity').value;
    var totalPrice = parseInt(price) * parseInt(quantity);
    document.getElementById("total").value = totalPrice;
}

function acceptStatus(){
        document.getElementById("status_value").value="Accepted"
    }

function outStatus(){
        document.getElementById("status_value").value="Outfordelivery"
    }

function completeStatus(){
        document.getElementById("status_value").value="Completed"
    }
    


