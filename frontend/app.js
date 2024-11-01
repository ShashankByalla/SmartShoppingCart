async function fetchItems() {
    const response = await fetch('http://localhost:5000/items');
    return await response.json();
}

async function refreshItems() {
    const items = await fetchItems();
    const itemList = document.getElementById('item-list');
    itemList.innerHTML = '';
    items.forEach(item => {
        itemList.innerHTML += `<div>${item.name} - $${item.price} - Weight: ${item.weight} kg</div>`;
    });
}

refreshItems();
