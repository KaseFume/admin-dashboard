function toggleDropdown(itemId, menuId) {
  const sidebar = document.querySelector('.sidebar'); 
  const item = sidebar?.querySelector(`#${itemId}`);
  const menu = sidebar?.querySelector(`#${menuId}`);

  if (item && menu) {
    item.addEventListener('click', (event) => {
      event.stopPropagation(); // Prevent conflicts with global click handlers
      menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
    });
  } else {
    console.error("Item or menu not found:", item, menu);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  toggleDropdown('data-view', 'data-view-menu');
});
