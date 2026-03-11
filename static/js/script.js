document.addEventListener('DOMContentLoaded', function() {
    // Custom Select Interaction Logic
    const customSelectWrappers = document.querySelectorAll('.custom-select-wrapper');

    customSelectWrappers.forEach(wrapper => {
        const select = wrapper.querySelector('.custom-select');
        const trigger = wrapper.querySelector('.custom-select-trigger');
        const options = wrapper.querySelectorAll('.custom-option');
        const nativeSelect = wrapper.querySelector('select');

        trigger.addEventListener('click', function(e) {
            e.stopPropagation();
            // Close all other selects
            document.querySelectorAll('.custom-select').forEach(s => {
                if (s !== select) s.classList.remove('open');
            });
            select.classList.toggle('open');
        });

        options.forEach(option => {
            option.addEventListener('click', function() {
                const value = this.getAttribute('data-value');
                const text = this.textContent.trim();

                // Update Trigger Display
                trigger.querySelector('span').textContent = text;

                // Update Native Select
                if (nativeSelect) {
                    nativeSelect.value = value;
                    nativeSelect.dispatchEvent(new Event('change', { bubbles: true }));
                }

                // Update UI selection state
                options.forEach(opt => opt.classList.remove('selected'));
                this.classList.add('selected');

                select.classList.remove('open');
            });
        });
    });

    // Close on click outside
    window.addEventListener('click', function() {
        document.querySelectorAll('.custom-select').forEach(s => s.classList.remove('open'));
    });
});
