document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('.dropdown-item input[type="checkbox"]');
    const selectedItems = document.getElementById('selected-items');
    let paragraphCreated = false;

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const dropdownItem = this.closest('.dropdown-item');
            const itemText = dropdownItem.querySelector('span').textContent.trim();

            if (this.checked) {
                if (!paragraphCreated) {
                    const paragraph = document.createElement('p');
                    paragraph.textContent = "MCC's selecionados:";
                    paragraph.id = 'mcc-paragraph';
                    selectedItems.parentNode.insertBefore(paragraph, selectedItems);
                    paragraphCreated = true;
                }
                // Se o checkbox for marcado, cria um novo item na lista
                if (!document.querySelector(`li[data-value="${itemText}"]`)) {
                    const listItem = document.createElement('li');
                    listItem.setAttribute('data-value', itemText);
                    listItem.innerHTML = `${itemText} <span class="remove-item" style="color: red; cursor: pointer;">&times;</span>`;
                    
                    // Adiciona o evento de click para remover o item
                    listItem.querySelector('.remove-item').addEventListener('click', function() {
                        const checkboxToUncheck = dropdownItem.querySelector('input[type="checkbox"]');
                        checkboxToUncheck.checked = false;
                        selectedItems.removeChild(listItem);

                        // Verifica se ainda há itens selecionados, se não houver, remove o parágrafo
                        if (selectedItems.children.length === 0 && paragraphCreated) {
                            const paragraphToRemove = document.getElementById('mcc-paragraph');
                            if (paragraphToRemove) {
                                paragraphToRemove.remove();
                            }
                            paragraphCreated = false;
                        }
                    });

                    selectedItems.appendChild(listItem);
                }
            } else {
                // Se o checkbox for desmarcado, remove o item da lista
                const listItemToRemove = document.querySelector(`li[data-value="${itemText}"]`);
                if (listItemToRemove) {
                    selectedItems.removeChild(listItemToRemove);
                }
                // Verifica se ainda há itens selecionados, se não houver, remove o parágrafo
                if (selectedItems.children.length === 0 && paragraphCreated) {
                    const paragraphToRemove = document.getElementById('mcc-paragraph');
                    if (paragraphToRemove) {
                        paragraphToRemove.remove();
                    }
                    paragraphCreated = false;
                }
            }
        });
    });
});

function toggleCartao(paragraphId, toggleSwitch) {
    const switchTexto = document.getElementById(paragraphId);

    if (toggleSwitch.checked) {
        setTimeout(() => {
            switchTexto.style.color = '#90ee90';
        }, 110);
    } else {
        switchTexto.style.color = '#fff';  // Cor padrão (preto)
    }
};
