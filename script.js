// Example: Add dynamic functionality (optional)
document.getElementById("quantity").addEventListener("input", function () {
    const quantity = parseInt(this.value);
    if (quantity > 10) {
        alert("You can book up to 10 tickets only!");
        this.value = 10;
    }
});
