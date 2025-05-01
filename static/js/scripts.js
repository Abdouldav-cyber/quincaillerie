// static/js/scripts.js
document.addEventListener('DOMContentLoaded', () => {
    // Ajouter la classe fade-in aux éléments avec la classe .fade-in
    const fadeElements = document.querySelectorAll('.fade-in');
    fadeElements.forEach((el, index) => {
        setTimeout(() => {
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, index * 100);
    });

    // Confirmation pour les actions critiques (par exemple, suppression)
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            if (!confirm('Êtes-vous sûr de vouloir supprimer cet élément ?')) {
                e.preventDefault();
            }
        });
    });

    console.log('Scripts chargés pour Quincaillerie');
});