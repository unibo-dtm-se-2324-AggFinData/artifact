// changing bg color
function changeBgColor(element) {
    document.body.style.backgroundColor = element.value;
}


document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("stock_name");
    const suggestionsBox = document.getElementById("suggestions");

    input.addEventListener("input", async () => {
        const query = input.value;
        if (query.length === 0) {
            suggestionsBox.innerHTML = "";
            return;
        }

        const res = await fetch(`/suggest?q=${query}`);
        const stocks = await res.json();

        suggestionsBox.innerHTML = "";
        stocks.forEach(stock => {
            const item = document.createElement("a");
            item.href = "#";
            item.className = "list-group-item list-group-item-action";
            item.textContent = stock.ticker;
            item.onclick = () => {
                input.value = stock.ticker;
                suggestionsBox.innerHTML = "";
            };
            suggestionsBox.appendChild(item);
        });
    });

    // Hide suggestions when clicking outside
    document.addEventListener("click", (e) => {
        if (!input.contains(e.target)) {
            suggestionsBox.innerHTML = "";
        }
    });
});